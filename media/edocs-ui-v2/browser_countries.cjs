const { chromium }=require('/Users/daniel/DocBits/doc2app/node_modules/playwright-core');
const fs=require('node:fs');
const path=require('node:path');
const assert=require('node:assert/strict');
const locale=process.argv[2];
const attachments=true;
const subset=process.argv.find(value=>value.startsWith('--countries='))?.split('=')[1].split(',');
const folders={en:'docbits',de:'deutsch',es:'espanol',fr:'french',it:'italian',nl:'dutch',pl:'polish',pt:'portuguese',zh:'chinese'};
assert(folders[locale]);
const countries=JSON.parse(fs.readFileSync(path.join(__dirname,'../edocs-country-support/evidence/catalog.json'),'utf8')).countries;
const dest=path.resolve('output/edocs-ui-v2/browser-countries/'+locale);
fs.mkdirSync(dest,{recursive:true});
(async()=>{
 let browser;
 for(let attempt=1;attempt<=3;attempt++){
  try{browser=await chromium.launch({headless:true,timeout:60000});break;}
  catch(error){if(attempt===3)throw error;console.error(JSON.stringify({locale,stage:'browser-launch-retry',attempt,error:error.message.split('\n')[0]}));}
 }
 const results=[];
 async function check(country){
  const page=await browser.newPage({viewport:{width:380,height:800}});
  const errors=[];page.on('pageerror',e=>errors.push(e.message));
  try{
   await page.goto(`http://127.0.0.1:8765/${attachments?'media/edocs-country-support':'output/edocs-support'}/review.html?lang=${locale}&country=${country.slug}`);
   await page.waitForFunction(()=>Boolean(document.querySelector('video').currentSrc));
   await page.locator('video').evaluate(v=>{v.preload='auto';v.load();});
   await page.waitForFunction(()=>document.querySelector('video').readyState>=2,null,{timeout:60000});
   await page.locator('video').evaluate(v=>v.textTracks[0].mode='showing');
   await page.waitForFunction(()=>document.querySelector('track').readyState===2,null,{timeout:60000});
   const metadata=await page.locator('video').evaluate(v=>{
    v.textTracks[0].mode='showing';
    return {duration:v.duration,width:v.videoWidth,height:v.videoHeight,language:v.textTracks[0].language,cues:v.textTracks[0].cues.length};
   });
   assert((await page.locator('video').evaluate(v=>v.currentSrc)).endsWith('-v2.mp4'));assert.equal(metadata.width,1280);assert.equal(metadata.height,720);assert.equal(metadata.language,locale);assert(metadata.cues>0);assert(metadata.duration<=120);
   await page.locator('video').evaluate(async v=>{v.muted=true;await v.play();});
   await page.waitForFunction(()=>{const v=document.querySelector('video');return v.currentTime>.3&&v.getVideoPlaybackQuality().totalVideoFrames>0;});
   const playback=await page.locator('video').evaluate(v=>({time:v.currentTime,frames:v.getVideoPlaybackQuality().totalVideoFrames}));
   await page.locator('video').evaluate(async v=>{v.pause();await new Promise(resolve=>{v.addEventListener('seeked',resolve,{once:true});v.currentTime=v.duration/2;});});
   const seek=await page.locator('video').evaluate(v=>({time:v.currentTime,ready:v.readyState}));
   assert(Math.abs(seek.time-metadata.duration/2)<.15);assert(seek.ready>=2);
   await page.locator('video').evaluate(async v=>{await new Promise(resolve=>{v.addEventListener('seeked',resolve,{once:true});v.currentTime=3.5;});});
   await page.waitForTimeout(180);
   const mobile=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,width:innerWidth,captions:[...document.querySelector('video').textTracks[0].activeCues].map(c=>c.text)}));
   assert(mobile.scroll<=mobile.width);assert(mobile.captions.length>0);
   await page.screenshot({path:path.join(dest,country.slug+'-browser.png'),fullPage:true});
   await page.locator('video').focus();await page.keyboard.press('Space');
   await page.waitForTimeout(150);assert(await page.locator('video').evaluate(v=>!v.paused));
   await page.locator('video').evaluate(async v=>{v.pause();await new Promise(resolve=>{v.addEventListener('seeked',resolve,{once:true});v.currentTime=v.duration-.4;});await v.play();});
   await page.waitForFunction(()=>document.querySelector('video').ended,null,{timeout:30000});
   assert.deepEqual(errors,[]);
   const range=await page.request.get(await page.locator('video').evaluate(v=>v.currentSrc),{headers:{Range:'bytes=0-1023'}});
   assert.equal(range.status(),206);assert.equal((await range.body()).length,1024);
   const result={country:country.slug,locale,metadata,playback,seek,mobile,ended:true,range206:true,keyboard:true,errors};
   results.push(result);console.log(JSON.stringify({country:country.slug,locale,stage:'browser-passed'}));
  }catch(error){console.error(JSON.stringify({country:country.slug,locale,error:error.message}));throw error;}finally{await page.close();}
 }
 try{
  // Three independent players, all in the one selected language.
  let next=0;await Promise.all(Array.from({length:3},async()=>{while(next<countries.length){const country=countries[next++];if(!subset||subset.includes(country.slug))await check(country);}}));
  fs.writeFileSync(path.join(dest,'browser.json'),JSON.stringify(results,null,2)+'\n');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1;});
