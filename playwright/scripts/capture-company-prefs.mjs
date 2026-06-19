/**
 * Capture Company Information / Preferences settings screenshots (per language).
 * Relay auth + CDP capture + runtime Tolgee language switch.
 *   QS_LANG=de node ...   (default '' = en)
 */
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/Users/daniel/DocBits/doc2app/');
const { chromium } = require('playwright');

const BASE = 'http://localhost:9000';
const QS_LANG = process.env.QS_LANG || '';
const OUT = '/Users/daniel/DocBits/DocBits/playwright/output/comp' + (QS_LANG ? '-' + QS_LANG : '');
fs.mkdirSync(OUT, { recursive: true });
const session = await fetch('http://127.0.0.1:7799/get').then((r) => r.json());
if (!session.token_details) throw new Error('relay has no session token');

const browser = await chromium.launch({ headless: true, args: ['--disable-dev-shm-usage'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();
const client = await ctx.newCDPSession(page);

await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
await page.evaluate((s) => { for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, session);
await page.goto(BASE + '/settings/company-information', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6000);

async function cosmetics() {
  await page.evaluate(() => { if (!document.getElementById('__sc')) { const s = document.createElement('style'); s.id='__sc'; s.textContent='*{animation:none!important;transition:none!important;caret-color:transparent!important}'; document.head.appendChild(s); } });
}
async function changeLang() {
  if (!QS_LANG) return;
  await page.evaluate((l) => { const t = document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee; if (t && t.changeLanguage) t.changeLanguage(l); }, QS_LANG);
  await page.waitForTimeout(1500);
}
await changeLang(); await cosmetics();

async function shotEl(sel, name) {
  try {
    const el = page.locator(sel).first();
    await el.scrollIntoViewIfNeeded({ timeout: 5000 });
    await page.waitForTimeout(500); await cosmetics();
    const box = await el.boundingBox();
    if (!box) throw new Error('no box');
    const pad = 14;
    await client.send('Page.captureScreenshot', { format: 'png', clip: { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad), width: Math.min(1440, box.width + pad * 2), height: box.height + pad * 2, scale: 2 } })
      .then(({ data }) => { fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data, 'base64')); console.log('SHOT', name); });
  } catch (e) { console.log('SKIP', name, String(e).split('\n')[0].slice(0, 70)); }
}
async function shotFull(name) {
  await cosmetics(); await page.waitForTimeout(300);
  const { data } = await client.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data, 'base64')); console.log('SHOT', name);
}

// 1) Company Information page (default view, Company Information expanded)
await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(400);
await shotFull('settings_company_information');

// expand the Company Preferences accordion (2nd settings-accordion header)
await page.locator('.settings-accordion-header').nth(1).click({ timeout: 6000 }).catch(() => {});
await page.waitForTimeout(1600); await cosmetics();

const PANEL = '.settings-accordion:has([data-test="company-date-pattern-select"])';
await shotEl(PANEL, 'company_preferences_1');                                          // whole prefs panel
await shotEl('.cp-field:has([data-test="company-date-pattern-select"])', 'company_preferences_2');   // Date Pattern field
await shotEl('.cp-field:has([data-test="company-amount-format-select"])', 'company_preferences_3');   // Amount Format field
await shotEl('.cp-subsection', 'company_preferences_4');                               // Version Info Dialog toggle
await shotEl('.cp-footer', 'company_preferences_5');                                   // Save

await browser.close();
console.log('DONE');
