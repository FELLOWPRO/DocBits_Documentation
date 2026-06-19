/**
 * Renew page-level Export settings screenshots (per language).
 *   QS_LANG=de node playwright/scripts/capture-export.mjs
 * Produces: export_list_view.png (redacted list), export_settings_menu_access.png (=copy),
 *           export_create_new_button.png (the New Export configuration form, empty).
 */
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/Users/daniel/DocBits/doc2app/');
const { chromium } = require('playwright');

const BASE = 'http://localhost:9000';
const QS_LANG = process.env.QS_LANG || '';
const OUT = '/Users/daniel/DocBits/DocBits/playwright/output/exp' + (QS_LANG ? '-' + QS_LANG : '');
fs.mkdirSync(OUT, { recursive: true });
const session = await fetch('http://127.0.0.1:7799/get').then((r) => r.json());
if (!session.token_details) throw new Error('relay has no session token');

const browser = await chromium.launch({ headless: true, args: ['--disable-dev-shm-usage'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();
const client = await ctx.newCDPSession(page);
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
await page.evaluate((s) => { for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, session);
await page.goto(BASE + '/settings/export', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6500);

async function cosmetics() { await page.evaluate(() => { if (!document.getElementById('__sc')) { const s=document.createElement('style'); s.id='__sc'; s.textContent='*{animation:none!important;transition:none!important;caret-color:transparent!important}'; document.head.appendChild(s);} }); }
async function redactTables() {
  await page.evaluate(() => {
    const re = /\S+@\S+\.\S+/;
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); const hit=[]; let n;
    while ((n = w.nextNode())) { if (re.test(n.nodeValue || '')) hit.push(n.parentElement); }
    hit.forEach((e)=>{ if(e){e.style.filter='blur(5px)';} });
    document.querySelectorAll('table tbody tr td, .q-table tbody tr td').forEach((e)=>{ e.style.filter='blur(5px)'; });
  });
}
async function lang() { if (QS_LANG) { await page.evaluate((l)=>{const t=document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee;if(t&&t.changeLanguage)t.changeLanguage(l);},QS_LANG); await page.waitForTimeout(1500);} }
async function full(name) { await cosmetics(); await page.waitForTimeout(250); const { data } = await client.send('Page.captureScreenshot', { format:'png', captureBeyondViewport:false }); fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data,'base64')); console.log('SHOT', name); }

await lang();
// 1) export list (redacted)
await redactTables(); await cosmetics();
await full('export_list_view');
fs.copyFileSync(`${OUT}/export_list_view.png`, `${OUT}/export_settings_menu_access.png`); console.log('SHOT export_settings_menu_access (copy)');

// 2) New Export configuration form (empty, no PII)
await page.getByRole('button', { name: /new|neu|nouveau|nuevo|nieuw|nowy|novo|yeni/i }).first().click({ timeout: 6000 }).catch(()=>{});
await page.waitForTimeout(2500); await cosmetics();
await full('export_create_new_button');

await browser.close(); console.log('DONE');
