/**
 * Renew Dashboard settings screenshots (per language, redacted).
 *   QS_LANG=de node playwright/scripts/capture-dashboard-settings.mjs
 * Produces: dashboard_settings.png (hero), settings_dashboard.png (=copy),
 *           dashboard_settings_3.png (General), dashboard_settings_4.png (Export History).
 * Export-History emails + org-ids are blurred.
 */
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/Users/daniel/DocBits/doc2app/');
const { chromium } = require('playwright');

const BASE = 'http://localhost:9000';
const QS_LANG = process.env.QS_LANG || '';
const OUT = '/Users/daniel/DocBits/DocBits/playwright/output/dash' + (QS_LANG ? '-' + QS_LANG : '');
fs.mkdirSync(OUT, { recursive: true });
const session = await fetch('http://127.0.0.1:7799/get').then((r) => r.json());
if (!session.token_details) throw new Error('relay has no session token');

const browser = await chromium.launch({ headless: true, args: ['--disable-dev-shm-usage'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();
const client = await ctx.newCDPSession(page);
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
await page.evaluate((s) => { for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, session);
await page.goto(BASE + '/settings/dashboard', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6500);

async function cosmetics() { await page.evaluate(() => { if (!document.getElementById('__sc')) { const s=document.createElement('style'); s.id='__sc'; s.textContent='*{animation:none!important;transition:none!important;caret-color:transparent!important}'; document.head.appendChild(s);} }); }
async function redact() {
  await page.evaluate(() => {
    const re = /\S+@\S+\.\S+|[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}/i; // emails + org-id UUIDs
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); const hit=[]; let n;
    while ((n = w.nextNode())) { if (re.test(n.nodeValue || '')) hit.push(n.parentElement); }
    hit.forEach((e)=>{ if(e){e.style.filter='blur(5px)';e.style.userSelect='none';} });
    document.querySelectorAll('table tbody tr td, .q-table tbody tr td').forEach((e)=>{ e.style.filter='blur(5px)'; e.style.userSelect='none'; });
  });
}
if (QS_LANG) { await page.evaluate((l)=>{const t=document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee;if(t&&t.changeLanguage)t.changeLanguage(l);},QS_LANG); await page.waitForTimeout(1500); }
await cosmetics();

async function full(name) {
  await redact(); await cosmetics(); await page.waitForTimeout(300);
  const { data } = await client.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data, 'base64')); console.log('SHOT', name);
}
async function shotLoc(loc, name) {
  try {
    await loc.scrollIntoViewIfNeeded({ timeout: 5000 }); await page.waitForTimeout(400);
    await redact(); await cosmetics();
    const box = await loc.boundingBox(); if (!box) throw new Error('no box');
    const pad = 14;
    const { data } = await client.send('Page.captureScreenshot', { format: 'png', clip: { x: Math.max(0,box.x-pad), y: Math.max(0,box.y-pad), width: Math.min(1440,box.width+pad*2), height: box.height+pad*2, scale: 2 } });
    fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data,'base64')); console.log('SHOT', name);
  } catch (e) { console.log('SKIP', name, String(e).split('\n')[0].slice(0,60)); }
}

await page.evaluate(() => window.scrollTo(0,0)); await page.waitForTimeout(300);
await full('dashboard_settings');
fs.copyFileSync(`${OUT}/dashboard_settings.png`, `${OUT}/settings_dashboard.png`); console.log('SHOT settings_dashboard (copy)');

// General accordion (1st) + Export History (the accordion containing a table)
const general = page.locator('.settings-accordion').nth(0);
await shotLoc(general, 'dashboard_settings_3');
const exportHist = page.locator('.settings-accordion:has(table), .settings-accordion:has(.q-table)').first();
await shotLoc(exportHist, 'dashboard_settings_4');

await browser.close(); console.log('DONE');
