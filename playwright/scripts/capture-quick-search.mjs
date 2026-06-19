/**
 * Standalone Playwright capture for the Quick Search docs screenshots.
 *
 * Why a script (not MCP browser_take_screenshot): the live Dashboard auto-refreshes
 * (websocket) so MCP page.screenshot never sees a stable frame and times out. Here we
 * capture via CDP Page.captureScreenshot (immediate raw capture, fs writes the PNG).
 *
 * Clean shots without deleting any data:
 *   - Status filter set to all statuses EXCEPT Error + Rejected (no error rows).
 *   - The status-filter badge row is hidden via CSS (cosmetic only).
 *   - Caret + CSS animations disabled.
 * Browser is relaunched every BATCH shots — headless chromium OOMs after ~14
 * queries on the long-lived dashboard SPA, which closed the page mid-run.
 *
 * Auth: session handed in via the loopback relay (POSTed from the logged-in browser).
 * Run (uses doc2app's playwright):  nvm use 22.22.2 && node playwright/scripts/capture-quick-search.mjs
 * Optional: ONLY=quick_search_10_purchase_order node ... (single shot).
 */
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/Users/daniel/DocBits/doc2app/');
const { chromium } = require('playwright');

const BASE = 'http://localhost:9000';
const QS_LANG = process.env.QS_LANG || '';   // de/es/fr/it/nl/pl/pt/tr ; '' = en (default)
const OUT = '/Users/daniel/DocBits/DocBits/playwright/output/qs' + (QS_LANG ? '-' + QS_LANG : '');
fs.mkdirSync(OUT, { recursive: true });
const session = await fetch('http://127.0.0.1:7799/get').then((r) => r.json());
if (!session.token_details) throw new Error('relay has no session token');

const SHOTS = [
  ['quick_search_01_entry', ''],
  ['quick_search_02_filename_starts', 'filename=invoice'],
  ['quick_search_03_filename_contains', 'filename:invoice'],
  ['quick_search_05_status', 'status=ready_for_validation'],
  ['quick_search_06_date', 'created_on>2026-05-25'],
  ['quick_search_07_amount', 'total_amount>5000'],
  ['quick_search_09_supplier', 'supplier_name=Test'],
  ['quick_search_10_purchase_order', 'purchase_order=PO'],
  ['quick_search_12_empty', 'supplier_name=""'],
  ['quick_search_13_combined', 'supplier_name=Test AND status=ready_for_validation'],
  ['quick_search_14_between', 'total_amount between 1000 and 5000'],
  ['quick_search_16_grouping', 'group by supplier_name'],
  ['quick_search_15_ap_empty', 'ap_assignment_code=""'],
  ['quick_search_17_vector', 'vector: supplier invoice'],
  ['quick_search_18_ocr', 'ocr: demo invoice'],
  ['quick_search_19_ai', 'ai: invoices over 1000 from this year'],
];
const KEEP = ['Pending confirmation', 'Pending Approval', 'Pending second approval',
  'Ready for validation', 'Restart in progress', 'New', 'Exporting', 'Exported'];
const EDITOR = '[contenteditable="true"]';
const ONLY = process.env.ONLY;
const BATCH = 4;

async function cosmetics(page) {
  await page.evaluate(() => {
    if (!document.getElementById('__sc')) {
      const s = document.createElement('style');
      s.id = '__sc';
      s.textContent = `*{animation:none!important;transition:none!important;caret-color:transparent!important}
        [data-test="qs-filter-badges"]{display:none!important}`;
      document.head.appendChild(s);
    }
  });
}

// Switch the in-app UI language at runtime via Tolgee (NOT localStorage — that
// reverts to the user-profile language on reload). Chrome (smart filters, help,
// status pills, chip labels, buttons, column headers) re-translates live.
async function changeLang(page) {
  if (!QS_LANG) return;
  await page.evaluate((lang) => {
    const t = document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee;
    if (t && t.changeLanguage) t.changeLanguage(lang);
  }, QS_LANG);
  await page.waitForTimeout(1500);
}

async function newPage(browser) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 860 }, deviceScaleFactor: 2 });
  const page = await ctx.newPage();
  await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
  await page.evaluate((s) => { for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, session);
  await page.goto(BASE + '/dashboard', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(5000);
  await cosmetics(page);
  // status filter once per page (lost on reload)
  await page.locator('[data-test="qs-toolbar-tune"]').click();
  await page.waitForTimeout(900);
  await page.locator('.q-menu .q-select, [role="menu"] .q-select').first().click();
  await page.waitForTimeout(1000);
  for (const label of KEEP) {
    await page.getByRole('option', { name: label, exact: true }).first().click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(180);
  }
  await page.keyboard.press('Escape');
  await page.waitForTimeout(400);
  await page.locator('[data-test="qs-toolbar-apply-filters"]').click().catch(() => {});
  await page.waitForTimeout(3500);
  await page.keyboard.press('Escape').catch(() => {});
  await cosmetics(page);
  await changeLang(page);
  const client = await ctx.newCDPSession(page);
  return { ctx, page, client };
}

async function shoot(page, client, name) {
  await cosmetics(page);
  await page.waitForTimeout(400);
  const { data } = await client.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data, 'base64'));
  console.log('SHOT', name);
}

async function setQuery(page, q) {
  await page.keyboard.press('Escape').catch(() => {});
  await page.click(EDITOR, { force: true, timeout: 8000 });
  await page.keyboard.press('ControlOrMeta+A');
  await page.keyboard.press('Delete');
  await page.waitForTimeout(250);
  // Commit each AND-predicate separately (chips auto-AND). Typing a literal
  // " AND " made the parser quote the first value -> exact-match -> 0 results.
  const parts = q && q.includes(' AND ') ? q.split(' AND ') : [q];
  for (const part of parts) {
    await page.keyboard.type(part, { delay: 15 });
    await page.waitForTimeout(part ? 1000 : 200);
    await page.keyboard.press('Escape');
    await page.keyboard.press('Enter');
    await page.waitForTimeout(1000);
  }
  await page.waitForTimeout(800);
  await page.waitForFunction(() => {
    const sp = document.querySelector('.q-spinner, .q-loading, [role="progressbar"]');
    return !sp || sp.offsetParent === null;
  }, { timeout: 9000 }).catch(() => {});
  await page.waitForTimeout(1800);
  await changeLang(page);          // language resets on some re-renders
  await cosmetics(page);
  await page.evaluate(() => document.activeElement && document.activeElement.blur());
  await page.waitForTimeout(600);
}

const todo = SHOTS.filter(([n]) => !ONLY || n === ONLY);
for (let i = 0; i < todo.length; i += BATCH) {
  const chunk = todo.slice(i, i + BATCH);
  const browser = await chromium.launch({ headless: true, args: ['--disable-dev-shm-usage'] });
  let pg;
  try {
    pg = await newPage(browser);
    for (const [name, q] of chunk) {
      try { await setQuery(pg.page, q); await shoot(pg.page, pg.client, name); }
      catch (e) { console.log('SKIP', name, String(e).split('\n')[0].slice(0, 70)); }
    }
  } catch (e) { console.log('BATCH_ERR', String(e).split('\n')[0].slice(0, 80)); }
  await browser.close().catch(() => {});
}
console.log('DONE');
