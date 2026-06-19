/**
 * Renew the Import settings screenshots (per language, redacted).
 *   QS_LANG=de node playwright/scripts/capture-import.mjs
 * Produces: import_settings.png (Import Pipeline overview), ftp_0.png (= same),
 *           document_settins_1.png (Document Settings accordion).
 * FTP/Email source hosts + emails are blurred (real customer data).
 */
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/Users/daniel/DocBits/doc2app/');
const { chromium } = require('playwright');

const BASE = 'http://localhost:9000';
const QS_LANG = process.env.QS_LANG || '';
const OUT = '/Users/daniel/DocBits/DocBits/playwright/output/imp' + (QS_LANG ? '-' + QS_LANG : '');
fs.mkdirSync(OUT, { recursive: true });
const session = await fetch('http://127.0.0.1:7799/get').then((r) => r.json());
if (!session.token_details) throw new Error('relay has no session token');

const browser = await chromium.launch({ headless: true, args: ['--disable-dev-shm-usage'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();
const client = await ctx.newCDPSession(page);
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
await page.evaluate((s) => { for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, session);
await page.goto(BASE + '/settings/import', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6500);

async function cosmetics() {
  await page.evaluate(() => { if (!document.getElementById('__sc')) { const s=document.createElement('style'); s.id='__sc'; s.textContent='*{animation:none!important;transition:none!important;caret-color:transparent!important}'; document.head.appendChild(s);} });
}
async function redact() {
  await page.evaluate(() => {
    const reEmail = /\S+@\S+\.\S+/;
    const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); const hit=[]; let n;
    while ((n = w.nextNode())) { if (reEmail.test(n.nodeValue || '')) hit.push(n.parentElement); }
    hit.forEach((e)=>{ if(e){e.style.filter='blur(5px)';e.style.userSelect='none';} });
    document.querySelectorAll('.pl-source, table tbody tr td, .q-table tbody tr td')
      .forEach((e)=>{ e.style.filter='blur(5px)'; e.style.userSelect='none'; });
  });
}
if (QS_LANG) { await page.evaluate((l)=>{const t=document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee;if(t&&t.changeLanguage)t.changeLanguage(l);},QS_LANG); await page.waitForTimeout(1500); }
await cosmetics();

async function full(name) {
  await redact(); await cosmetics(); await page.waitForTimeout(300);
  const { data } = await client.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
  fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data, 'base64')); console.log('SHOT', name);
}
async function shotEl(sel, name) {
  try {
    const el = page.locator(sel).first();
    await el.scrollIntoViewIfNeeded({ timeout: 5000 }); await page.waitForTimeout(400);
    await redact(); await cosmetics();
    const box = await el.boundingBox(); if (!box) throw new Error('no box');
    const pad = 14;
    const { data } = await client.send('Page.captureScreenshot', { format: 'png', clip: { x: Math.max(0,box.x-pad), y: Math.max(0,box.y-pad), width: Math.min(1440,box.width+pad*2), height: box.height+pad*2, scale: 2 } });
    fs.writeFileSync(`${OUT}/${name}.png`, Buffer.from(data,'base64')); console.log('SHOT', name);
  } catch (e) { console.log('SKIP', name, String(e).split('\n')[0].slice(0,70)); }
}

// 1) Import Pipeline overview (default-expanded, top of page) -> import_settings + ftp_0
await page.evaluate(() => window.scrollTo(0,0)); await page.waitForTimeout(300);
await full('import_settings');
fs.copyFileSync(`${OUT}/import_settings.png`, `${OUT}/ftp_0.png`); console.log('SHOT ftp_0 (copy)');

// 2) Document Settings accordion -> expand (2nd accordion) + element shot
const ds = page.locator('.settings-accordion').nth(1);
const expanded = await ds.evaluate((el) => el.classList.contains('expanded')).catch(() => false);
if (!expanded) { await ds.locator('.settings-accordion-header').click({ timeout: 6000 }).catch(()=>{}); }
await page.waitForTimeout(1400); await ds.scrollIntoViewIfNeeded({ timeout: 5000 }).catch(()=>{});
await page.waitForTimeout(400); await redact(); await cosmetics();
try {
  const box = await ds.boundingBox();
  if (box) {
    const pad = 14;
    const { data } = await client.send('Page.captureScreenshot', { format: 'png', clip: { x: Math.max(0,box.x-pad), y: Math.max(0,box.y-pad), width: Math.min(1440,box.width+pad*2), height: box.height+pad*2, scale: 2 } });
    fs.writeFileSync(`${OUT}/document_settins_1.png`, Buffer.from(data,'base64')); console.log('SHOT document_settins_1');
  } else console.log('SKIP document_settins_1 no box');
} catch (e) { console.log('SKIP document_settins_1', String(e).split('\n')[0].slice(0,60)); }

await browser.close(); console.log('DONE');
