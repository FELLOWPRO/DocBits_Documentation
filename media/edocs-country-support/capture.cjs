const { chromium }=require('/Users/daniel/DocBits/doc2app/node_modules/playwright-core');
const fs=require('node:fs');
const path=require('node:path');
const locale=process.argv[2]||'en';
const ui={en:'en-us',de:'de',es:'es-es',fr:'fr',it:'it',nl:'nl',pl:'pl',pt:'pt',zh:'zh'}[locale];
if(!ui)throw new Error('Unsupported documentation locale');
const out=path.join(__dirname,'screenshots',locale);
fs.mkdirSync(out,{recursive:true});
const countries=JSON.parse(fs.readFileSync(path.join(__dirname,'catalog.json'),'utf8')).countries;
const credentials={};
for(const line of fs.readFileSync('/Users/daniel/DocBits/doc2-api/.env','utf8').split('\n')) {
 const match=line.match(/^(TEST_EMAIL2|TEST_PASSWORD2)=(.*)$/);
 if(match)credentials[match[1]]=match[2].replace(/^["']|["']$/g,'');
}
async function ready(page){
 await page.waitForFunction(()=>![...document.querySelectorAll('.q-loading,.loading-component,.q-inner-loading--showing')].some(el=>el.getBoundingClientRect().width&&el.getBoundingClientRect().height),null,{timeout:120000});
 await page.waitForFunction(()=>!/Loading (master data|documents|settings)/.test(document.body.innerText),null,{timeout:120000});
}
async function clean(page){
 await page.addStyleTag({content:'.q-notification,.q-dialog__inner,.q-overlay,[data-test^="settings-assistant-panel"],[data-test="sidebar-item-user"],.action-menu-btn {visibility:hidden!important;}'});
 await page.evaluate(()=>{
  document.querySelectorAll('a[href^="mailto:"],.col-3 .cursor-pointer.row .col-8 > .col-12:last-child').forEach(el=>el.style.visibility='hidden');
 });
}
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1600,height:1000},deviceScaleFactor:1});
 const page=await context.newPage();
 const evidence=[];
 try{
  await page.goto('https://dev.docbits.com/login',{waitUntil:'domcontentloaded'});
  await page.locator('[data-test="email-input"]').first().fill(credentials.TEST_EMAIL2);
  await page.locator('[data-test="password-input"]').first().fill(credentials.TEST_PASSWORD2);
  await page.keyboard.press('Enter');
  await page.waitForURL(u=>u.pathname.startsWith('/nova/prepare-dashboard'),{timeout:90000});
  await ready(page);
  await page.evaluate(code=>{localStorage.setItem('selected_language','__q_strn|'+code);localStorage.setItem('__tolgee_currentLanguage',code.split('-')[0]);},ui);
  await page.goto('https://dev.docbits.com/nova/settings/manage-xslt/INVOICE?tab=FACTURX',{waitUntil:'domcontentloaded'});
  await page.locator('[data-edoc-format="FACTURX"]').waitFor({state:'visible',timeout:120000});
  await ready(page);
  const actual=await page.evaluate(async code=>{const t=document.querySelector('#q-app')?.__vue_app__?.config?.globalProperties?.$tolgee;if(!t)throw new Error('Tolgee unavailable');await t.changeLanguage(code);return t.getLanguage();},locale);
  if(actual!==locale)throw new Error('Locale mismatch');
  await page.waitForTimeout(900);
  const filter=page.locator('.settings-container input.q-field__native').first();
  for(const country of countries){
   await filter.fill(country.search);
   await page.waitForTimeout(500);
   await ready(page);
   await clean(page);
   const filename=`edocs-support-${country.slug}-${locale}.png`;
   if(country.representative){
    const card=page.locator(`[data-edoc-format="${country.representative}"]`);
    await card.waitFor({state:'visible',timeout:30000});
    if((await card.boundingBox()).height < 200){
     await card.locator('.q-expansion-item__container > .q-item').first().click();
    }
    await page.waitForFunction(name=>document.querySelector('[data-edoc-format="'+name+'"]')?.getBoundingClientRect().height>300,country.representative,{timeout:30000});
    await card.locator('tr.xslt-row').first().waitFor({state:'visible'});
    await page.waitForTimeout(450);
    await page.mouse.move(0,0);
    await page.waitForTimeout(350);
    await card.scrollIntoViewIfNeeded();
    await clean(page);
    const text=await card.innerText();
    const names={en:'Name',de:'Name',es:'Nombre',fr:'Nom',it:'Nome',nl:'Naam',pl:'Nazwa',pt:'Nome',zh:'姓名'};
    if(!text.includes(names[locale]))throw new Error('Localized table gate failed: '+country.slug);
    await card.screenshot({path:path.join(out,filename),animations:"disabled"});
    evidence.push({country:country.slug,locale,runtime_locale:actual,representative:country.representative,rows:await card.locator('tr.xslt-row').count(),filename});
   }else{
    if(await page.locator('[data-edoc-format]').count())throw new Error('Previously unconfirmed country now has entries: refresh evidence');
    await page.locator('.settings-container').first().screenshot({path:path.join(out,filename)});
    evidence.push({country:country.slug,locale,runtime_locale:actual,representative:null,rows:0,filename});
   }
   console.log(JSON.stringify(evidence.at(-1)));
  }
  fs.writeFileSync(path.join(out,'capture.json'),JSON.stringify(evidence,null,2)+'\n');
 }finally{await browser.close();}
})().catch(e=>{console.error(e.message);process.exitCode=1;});
