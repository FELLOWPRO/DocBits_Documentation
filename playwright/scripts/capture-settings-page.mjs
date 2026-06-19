/**
 * Generic settings-page screenshotter (relay auth + CDP + Tolgee lang switch).
 *   ROUTE=/settings/users NAME=users_full QS_LANG=de node ...
 * REDACT=1 applies PII redaction (blur emails / hide sensitive cells) before shot.
 */
import { createRequire } from 'module';
import fs from 'fs';
const require = createRequire('/Users/daniel/DocBits/doc2app/');
const { chromium } = require('playwright');

const BASE = 'http://localhost:9000';
const ROUTE = process.env.ROUTE || '/settings/users';
const NAME = process.env.NAME || 'page_full';
const QS_LANG = process.env.QS_LANG || '';
const REDACT = process.env.REDACT === '1' || process.env.REDACT === '2';
const REDACT_ALL = process.env.REDACT === '2';
const OUT = '/Users/daniel/DocBits/DocBits/playwright/output/set' + (QS_LANG ? '-' + QS_LANG : '');
fs.mkdirSync(OUT, { recursive: true });
const session = await fetch('http://127.0.0.1:7799/get').then((r) => r.json());
if (!session.token_details) throw new Error('relay has no session token');

const browser = await chromium.launch({ headless: true, args: ['--disable-dev-shm-usage'] });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();
const client = await ctx.newCDPSession(page);
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded' });
await page.evaluate((s) => { for (const [k, v] of Object.entries(s)) localStorage.setItem(k, v); }, session);
await page.goto(BASE + ROUTE, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(6500);

async function cosmetics() {
  await page.evaluate(() => { if (!document.getElementById('__sc')) { const s=document.createElement('style'); s.id='__sc'; s.textContent='*{animation:none!important;transition:none!important;caret-color:transparent!important}'; document.head.appendChild(s);} });
}
if (QS_LANG) { await page.evaluate((l)=>{const t=document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee;if(t&&t.changeLanguage)t.changeLanguage(l);},QS_LANG); await page.waitForTimeout(1500); }

if (REDACT) {
  // Blur PII: emails anywhere + the user table's Name (col 1) & E-Mail (col 2) cells.
  await page.evaluate((REDACT_ALL_FLAG) => {
    const reEmail = /\S+@\S+\.\S+/;
    const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    const hit = []; let n;
    while ((n = walk.nextNode())) { if (reEmail.test(n.nodeValue || '')) hit.push(n.parentElement); }
    hit.forEach((el) => { if (el) { el.style.filter = 'blur(5px)'; el.style.userSelect = 'none'; } });
    const aggressive = REDACT_ALL_FLAG;
    const sel = aggressive
      ? 'table tbody tr td, .q-table tbody tr td'                          // every data cell (FTP/IMAP hosts, users)
      : 'table tbody tr td:nth-child(1), table tbody tr td:nth-child(2), .q-table tbody tr td:nth-child(1), .q-table tbody tr td:nth-child(2)';
    document.querySelectorAll(sel).forEach((el) => { el.style.filter = 'blur(5px)'; el.style.userSelect = 'none'; });
    if (aggressive) {
      // Import Pipeline source cards (FTP/SFTP hosts, dirs) live in divs, not tables.
      document.querySelectorAll('.pl-source')
        .forEach((el) => { el.style.filter = 'blur(5px)'; el.style.userSelect = 'none'; });
    }
  }, REDACT_ALL);
  await page.waitForTimeout(300);
}
await cosmetics();
const info = await page.evaluate(() => ({ url: location.href, loggedIn: !location.href.includes('login'),
  heads: [...document.querySelectorAll('h1,h2,h3,.text-h6,.text-h5,th,.q-th')].map(e=>e.innerText.trim()).filter(Boolean).slice(0,25) }));
console.log('PAGEINFO', JSON.stringify(info));
await page.evaluate(()=>window.scrollTo(0,0)); await page.waitForTimeout(300);
const { data } = await client.send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
fs.writeFileSync(`${OUT}/${NAME}.png`, Buffer.from(data,'base64')); console.log('SHOT', NAME);
await browser.close(); console.log('DONE');
