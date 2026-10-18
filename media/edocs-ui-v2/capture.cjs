/* Read-only development UI captures. Never save, create or activate a rule. */
const { chromium } = require('/Users/daniel/DocBits/doc2app/node_modules/playwright-core');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const locale = process.argv[2];
const ui = {en:'en-us',de:'de',es:'es-es',fr:'fr',it:'it',nl:'nl',pl:'pl',pt:'pt',zh:'zh'}[locale];
if (!ui) throw new Error('Choose one of the nine documentation locales');
const out = path.resolve(process.argv[3]);
const format = 'FACTURX 1.0.05 - ZUGFERD 2.1';
fs.mkdirSync(out, {recursive:true});
const credentials = {};
const credentialFile = process.env.DOCBITS_CAPTURE_CREDENTIAL_FILE || '/Users/daniel/DocBits/doc2-api/.env';
for (const line of fs.readFileSync(credentialFile,'utf8').split('\n')) {
  const match=line.match(/^(TEST_EMAIL2|TEST_PASSWORD2)=(.*)$/);
  if(match)credentials[match[1]]=match[2].replace(/^["']|["']$/g,'');
}
async function ready(page) {
  await page.waitForFunction(() => ![...document.querySelectorAll('.q-loading,.loading-component,.q-inner-loading--showing')].some(e=>e.getBoundingClientRect().width&&e.getBoundingClientRect().height),null,{timeout:120000});
  await page.waitForFunction(() => !/Loading (master data|documents|settings)/.test(document.body.innerText),null,{timeout:120000});
}
async function language(page) {
  await page.waitForFunction(()=>!!document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee,null,{timeout:60000});
  const actual=await page.evaluate(async code=>{
    const t=document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee;
    if(!t)throw new Error('Tolgee unavailable');
    await t.changeLanguage(code);return t.getLanguage();
  },locale);
  if(actual!==locale)throw new Error('Runtime language mismatch');
  await page.waitForTimeout(400);
}
async function clean(page) {
  await page.addStyleTag({content:'.q-notification,[data-test^="settings-assistant-panel"],[data-test="sidebar-item-user"],.action-menu-btn {visibility:hidden!important;}'});
  await page.evaluate(()=>document.querySelectorAll('a[href^="mailto:"],.col-3 .cursor-pointer.row .col-8 > .col-12:last-child').forEach(e=>e.style.visibility='hidden'));
}
const evidence={locale,environment:'development',captured_at:new Date().toISOString(),viewport:{width:1600,height:1000,deviceScaleFactor:2},redactions:['user menu','version authors','mailto links','notifications'],mutations:[],captures:[]};
async function shot(page,name,locator,focus,folder=out,receipt=evidence) {
  await ready(page);await clean(page);await page.mouse.move(0,0);await page.waitForTimeout(250);
  const file=path.join(folder,name+'.png');
  if(locator)await locator.screenshot({path:file,animations:'disabled'});
  else await page.screenshot({path:file,clip:{x:320,y:55,width:1280,height:850},animations:'disabled'});
  receipt.captures.push({name,file:path.basename(file),url:page.url(),sha256:crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'),focus:focus||null});
  fs.writeFileSync(path.join(folder,'capture.json'),JSON.stringify(receipt,null,2)+'\n');
  console.log(JSON.stringify({locale,capture:name}));
}
async function seekCode(page,term) {
  return page.evaluate(term=>{
    const surface=document.querySelector('.code-editor-surface');
    let component=surface?.__vueParentComponent;
    while(component&&!component.proxy?.editorInstance)component=component.parent;
    const editor=surface?.env?.editor || component?.proxy?.editorInstance;
    if(!editor)throw new Error('Real code editor unavailable');
    const value=editor.getValue();
    const index=value.toLowerCase().indexOf(term.toLowerCase());
    if(index<0)return {found:false};
    const line=value.slice(0,index).split('\n').length;
    editor.gotoLine(line,0,false);
    editor.renderer.scrollToY(Math.max(0,editor.session.documentToScreenRow(line-1,0)*editor.renderer.lineHeight-35));
    return {found:true,line,term};
  },term);
}
async function main(){
  const browser=await chromium.launch({headless:true});
  const context=await browser.newContext({viewport:{width:1600,height:1000},deviceScaleFactor:2});
  const page=await context.newPage();
  try {
    await page.goto('https://dev.docbits.com/login',{waitUntil:'domcontentloaded'});
    await page.locator('[data-test="email-input"]').first().fill(credentials.TEST_EMAIL2);
    await page.locator('[data-test="password-input"]').first().fill(credentials.TEST_PASSWORD2);
    await page.keyboard.press('Enter');
    await page.waitForURL(u=>!u.pathname.includes('/login'),{timeout:90000});await ready(page);
    await page.evaluate(code=>{localStorage.setItem('selected_language','__q_strn|'+code);localStorage.setItem('__tolgee_currentLanguage',code.split('-')[0]);},ui);
    await page.goto('https://dev.docbits.com/nova/settings/manage-xslt/INVOICE?tab='+encodeURIComponent(format),{waitUntil:'domcontentloaded'});
    await page.locator('[data-edoc-format="'+format+'"]').waitFor({state:'visible',timeout:120000});
    await ready(page);await language(page);
    const card=page.locator('[data-edoc-format="'+format+'"]');
    await card.scrollIntoViewIfNeeded();
    await shot(page,'format-list');await shot(page,'rules',card);
    const rows=await card.locator('tr.xslt-row').all();
    const inventory=await Promise.all(rows.map(async r=>(await r.locator('td').allTextContents()).slice(0,4).map(s=>s.trim())));
    evidence.rows=inventory;
    for(const [index,name,term] of [[0,'transformation','INVOICE_TYPE'],[1,'preview-template',null],[2,'extraction-paths','invoice_type']]) {
      await card.locator('tr.xslt-row').nth(index).locator('td').first().click();
      await ready(page);await language(page);
      await page.locator('.code-editor-surface').waitFor({state:'visible',timeout:60000});
      const focus=term?await seekCode(page,term):null;
      await page.waitForTimeout(400);await shot(page,name,null,focus);
      await shot(page,name+'-code',page.locator('.import-container'),focus);
      if(index===0) {
        await shot(page,'versions',page.locator('.col-3.q-pa-sm').first());
        const previewLabel=await page.evaluate(()=>document.querySelector('#q-app').__vue_app__.config.globalProperties.$t('preview'));
        await page.getByRole('button',{name:previewLabel,exact:true}).first().click();
        await shot(page,'preview-panel');
        await page.getByRole('button',{name:previewLabel,exact:true}).first().click();
      }
      await page.goBack();await ready(page);await language(page);
      await card.waitFor({state:'visible',timeout:60000});await card.scrollIntoViewIfNeeded();
    }
    await page.goto('https://dev.docbits.com/nova/settings/modules/document-integration',{waitUntil:'domcontentloaded'});
    await ready(page);await language(page);
    const signLabel=await page.evaluate(()=>document.querySelector('#q-app').__vue_app__.config.globalProperties.$t('set_negative_sign_for_credit_notes'));
    const sign=page.locator('.settings-card').filter({has:page.locator('.settings-toggle-label').filter({hasText:signLabel})}).first();
    await sign.waitFor({state:'visible',timeout:60000});await sign.scrollIntoViewIfNeeded();
    await shot(page,'negative-sign');await shot(page,'negative-sign-control',sign);
    evidence.runtime_language=locale;
    fs.writeFileSync(path.join(out,'capture.json'),JSON.stringify(evidence,null,2)+'\n');
  } finally {await browser.close();}
}
module.exports={chromium,credentials,ready,language,clean,seekCode,shot,ui};
if(require.main===module)main().catch(error=>{console.error(error.message);process.exitCode=1;});
