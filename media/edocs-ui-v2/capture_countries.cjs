/* One locale per run; real read-only country-specific eDocs views. */
const {chromium,credentials,ready,language,clean,seekCode,shot,ui}=require('./capture.cjs');
const fs=require('node:fs'),path=require('node:path');
const locale=process.argv[2],out=path.resolve(process.argv[3]);
const catalogue=JSON.parse(fs.readFileSync(process.argv[4],'utf8'));
const only=process.argv[5]?.split(',');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const context=await browser.newContext({viewport:{width:1600,height:1000},deviceScaleFactor:2});
 const page=await context.newPage();
 try{
  await page.goto('https://dev.docbits.com/login',{waitUntil:'domcontentloaded'});
  await page.locator('[data-test="email-input"]').first().fill(credentials.TEST_EMAIL2);
  await page.locator('[data-test="password-input"]').first().fill(credentials.TEST_PASSWORD2);
  await page.keyboard.press('Enter');
  await page.waitForURL(u=>!u.pathname.includes('/login'),{timeout:90000});await ready(page);
  await page.evaluate(code=>{localStorage.setItem('selected_language','__q_strn|'+code);localStorage.setItem('__tolgee_currentLanguage',code.split('-')[0]);},ui);
  const list='https://dev.docbits.com/nova/settings/manage-xslt/INVOICE?tab=FACTURX';
  try { await page.goto(list,{waitUntil:'domcontentloaded'}); }
  catch(error) {
   // Login can still finish its own dashboard navigation after the first URL
   // change. Resume once after that navigation, without changing any settings.
   if(!error.message.includes('ERR_ABORTED'))throw error;
   await page.waitForLoadState('domcontentloaded');await ready(page);
   await page.goto(list,{waitUntil:'domcontentloaded'});
  }
  await page.locator('[data-edoc-format="FACTURX"]').waitFor({state:'visible',timeout:120000});
  await ready(page);await language(page);
  for(const country of catalogue.countries){
   if(only&&!only.includes(country.slug))continue;
   const folder=path.join(out,country.slug);fs.mkdirSync(folder,{recursive:true});
   if(fs.existsSync(path.join(folder,'complete.json'))) {console.log(JSON.stringify({locale,country:country.slug,resumed:true}));continue;}
   const evidence={locale,country:country.slug,representative:country.representative,environment:'development',runtime_language:locale,captured_at:new Date().toISOString(),viewport:{width:1600,height:1000,deviceScaleFactor:2},redactions:['version authors','user menu','notifications','mailto links'],mutations:[],captures:[]};
   const take=(name,locator,focus)=>shot(page,name,locator,focus,folder,evidence);
   const filter=page.locator('.settings-container input.q-field__native').first();
   await filter.fill(country.search);await page.waitForTimeout(600);await ready(page);await clean(page);
   if(!country.representative){
    if(await page.locator('[data-edoc-format]').count())throw new Error('Previously unconfirmed country has results; review catalogue');
    await take('rules',page.locator('.settings-container').first());
   }else{
    const card=page.locator(`[data-edoc-format="${country.representative}"]`);
    await card.waitFor({state:'visible',timeout:60000});await card.scrollIntoViewIfNeeded();
    if((await card.boundingBox()).height<200)await card.locator('.q-expansion-item__container > .q-item').first().click();
    await card.locator('tr.xslt-row').first().waitFor({state:'visible',timeout:60000});
    await card.scrollIntoViewIfNeeded();
    evidence.rows=await Promise.all((await card.locator('tr.xslt-row').all()).map(async r=>(await r.locator('td').allTextContents()).slice(0,4).map(s=>s.trim())));
    // Preserve the real Default/Custom state. Review every captured source before
    // publication; custom configuration is part of the explanation, not an error.
    await take('rules',card);
    for(const [rowName,name,term] of [['TRANSFORMATION','transformation-code','INVOICE_TYPE'],['EXTRACTION PATHS','extraction-paths-code','invoice_type']]){
     const rows=await card.locator('tr.xslt-row').all();
     let selected;
     for(const row of rows)if((await row.locator('td').first().innerText()).trim()===rowName){selected=row;break;}
     if(!selected)throw new Error('Missing '+rowName+' for '+country.slug);
     await selected.locator('td').first().click();await ready(page);await language(page);
     await page.locator('.code-editor-surface').waitFor({state:'visible',timeout:60000});
     const focus=await seekCode(page,term);await page.waitForTimeout(200);
     await take(name,page.locator('.import-container'),focus);
     if(rowName==='TRANSFORMATION'){
      const preview=await page.evaluate(()=>document.querySelector('#q-app').__vue_app__.config.globalProperties.$t('preview'));
      await page.getByRole('button',{name:preview,exact:true}).first().click();await take('preview-panel');
      await page.getByRole('button',{name:preview,exact:true}).first().click();
     }
     await page.goBack();await ready(page);await language(page);
     await card.waitFor({state:'visible',timeout:60000});await card.scrollIntoViewIfNeeded();
     if((await card.boundingBox()).height<200)await card.locator('.q-expansion-item__container > .q-item').first().click();
     await card.locator('tr.xslt-row').first().waitFor({state:'visible',timeout:60000});
    }
   }
   fs.writeFileSync(path.join(folder,'capture.json'),JSON.stringify(evidence,null,2)+'\n');
   fs.writeFileSync(path.join(folder,'complete.json'),JSON.stringify({locale,country:country.slug,captures:evidence.captures.length})+'\n');
   console.log(JSON.stringify({locale,country:country.slug,complete:true}));
  }
 }finally{await browser.close();}
})().catch(error=>{console.error(error.message);process.exitCode=1;});
