/**
 * Standalone Playwright capture for the Quick Search docs screenshots.
 *
 * Why a script (not the MCP browser_take_screenshot): the live Dashboard
 * auto-refreshes (websocket) so MCP page.screenshot never sees a stable frame
 * and times out. Here we freeze the page (clear timers + kill CSS animation),
 * exclude error/rejected docs via the toolbar Status filter, and capture each
 * documented query via CDP Page.captureScreenshot (fs available → writes PNG).
 *
 * Auth: the session is handed in via the loopback relay (POST'd from the
 * logged-in browser earlier). We fetch it and inject into localStorage.
 *
 * Run:  (uses doc2app's playwright)
 *   nvm use 22.22.2 && node playwright/scripts/capture-quick-search.mjs
 */
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/Users/daniel/DocBits/doc2app/');
const { chromium } = require('playwright');

const RELAY = 'http://127.0.0.1:7799/get';
const BASE = 'http://localhost:9000';
const OUT = '/Users/daniel/DocBits/DocBits/playwright/output/qs';
fs.mkdirSync(OUT, { recursive: true });

const session = await fetch(RELAY).then((r) => r.json());
if (!session.token_details) throw new Error('relay has no session token');

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 860 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
await page.evaluate((s) => { for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, session);
await page.goto(BASE + '/dashboard', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6000);

// Freeze live updates so the frame stabilises.
async function freeze() {
  // ONLY cosmetic (no animations / no text caret). Do NOT clear timers — that
  // kills the app's data fetch and leaves the table empty. CDP captureScreenshot
  // is an immediate raw capture (no stability wait), so freezing isn't needed.
  await page.evaluate(() => {
    if (!document.getElementById('__freeze')) {
      const s = document.createElement('style');
      s.id = '__freeze';
      s.textContent = '*{animation:none!important;transition:none!important;caret-color:transparent!important}';
      document.head.appendChild(s);
    }
  });
}
await freeze();

const client = await ctx.newCDPSession(page);
async function shot(name) {
  await freeze();
  await page.waitForTimeout(400);
  const { data } = await client.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data, 'base64'));
  console.log('SHOT', name);
}

// (No tune-menu status filter — it proved fragile and blanked the SPA. The recent
// dev docs at the top of created_on-desc are clean; error EDI fixtures are older.
// Any shot that still shows an error row gets handled per-query afterwards.)

// ── Query → filename map (matches the documented page) ──
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
  ['quick_search_13_combined', 'status=ready_for_validation AND supplier_name=Test'],
  ['quick_search_14_between', 'total_amount between 1000 and 5000'],
  ['quick_search_15_ap_empty', 'ap_assignment_code=""'],
  ['quick_search_17_vector', 'vector: invoices about office supplies'],
  ['quick_search_18_ocr', 'ocr: demo invoice'],
  ['quick_search_19_ai', 'ai: invoices over 1000 from this year'],
];

const EDITOR = '[contenteditable="true"]';
async function setQuery(q) {
  // Fresh dashboard each shot → clean state, no carry-over navigation.
  await page.goto(BASE + '/dashboard', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4500);
  await freeze();
  await page.click(EDITOR, { force: true, timeout: 8000 });
  await page.keyboard.press('ControlOrMeta+A');
  await page.keyboard.press('Delete');
  await page.waitForTimeout(200);
  if (q) {
    await page.keyboard.type(q, { delay: 15 });
    await page.waitForTimeout(500);
    await page.keyboard.press('Escape');   // dismiss autocomplete popup
    await page.keyboard.press('Enter');
    await page.waitForTimeout(2600);       // results refresh
  }
  // Blur WITHOUT clicking (a click in the table opens a document).
  await page.evaluate(() => document.activeElement && document.activeElement.blur());
  await page.waitForTimeout(800);
}

for (const [name, q] of SHOTS) {
  try {
    await setQuery(q);
    await shot(name);
  } catch (e) {
    console.log('SKIP', name, String(e).split('\n')[0].slice(0, 80));
  }
}

await browser.close();
console.log('DONE');
