const {chromium} = require('/Users/daniel/DocBits/doc2app/node_modules/playwright-core');
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const locale = process.argv[2];
if (!['en','de','es','fr','it','nl','pl','pt','zh'].includes(locale)) throw new Error('Choose one locale');
const out = path.resolve(process.argv[3] || ('output/edocs-ui-v2/browser/'+locale));
fs.mkdirSync(out, {recursive:true});
(async () => {
  const browser = await chromium.launch({headless:true});
  const page = await browser.newPage({viewport:{width:1100,height:1000}});
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  try {
    await page.goto(`http://127.0.0.1:8765/media/edocs-credit-note/review.html?lang=${locale}`);
    await page.waitForFunction(() => document.querySelector('video').readyState >= 2);
    await page.waitForFunction(() => document.querySelector('track').readyState === 2);
    const metadata = await page.locator('video').evaluate(video => {
      video.textTracks[0].mode='showing';
      return {duration:video.duration,width:video.videoWidth,height:video.videoHeight,language:video.textTracks[0].language,cues:video.textTracks[0].cues.length};
    });
    assert((await page.locator('video').evaluate(v=>v.currentSrc)).endsWith('-v2.mp4')); assert.equal(metadata.width,1280); assert.equal(metadata.height,720); assert.equal(metadata.language,locale); assert(metadata.cues>0); assert(metadata.duration<=120);
    await page.locator('video').evaluate(async video => {video.muted=true; await video.play();});
    await page.waitForFunction(() => { const video=document.querySelector('video'); return video.currentTime>0.3 && video.getVideoPlaybackQuality().totalVideoFrames>0; },null,{timeout:30000});
    const playback = await page.locator('video').evaluate(video => ({time:video.currentTime,frames:video.getVideoPlaybackQuality().totalVideoFrames}));
    assert(playback.time>0.3 && playback.frames>0);
    await page.locator('video').evaluate(async video => {
      video.pause();
      await new Promise(resolve => {video.addEventListener('seeked',resolve,{once:true}); video.currentTime=video.duration/2;});
    });
    const seek = await page.locator('video').evaluate(video => ({time:video.currentTime,ready:video.readyState}));
    assert(Math.abs(seek.time-metadata.duration/2)<0.15); assert(seek.ready>=2);
    await page.setViewportSize({width:380,height:950});
    await page.locator('video').evaluate(async video => {
      await new Promise(resolve => {video.addEventListener('seeked',resolve,{once:true}); video.currentTime=3.5;});
    });
    await page.waitForTimeout(250);
    const mobile = await page.evaluate(() => ({scroll:document.documentElement.scrollWidth,width:innerWidth,captions:[...document.querySelector('video').textTracks[0].activeCues].map(cue=>cue.text),focusable:document.querySelector('video').tabIndex}));
    assert(mobile.scroll<=mobile.width); assert(mobile.captions.length>0);
    await page.screenshot({path:path.join(out, 'browser-380.png'),fullPage:true});
    await page.locator('video').focus();
    await page.keyboard.press('Space');
    await page.waitForTimeout(250);
    const keyboardPlays = await page.locator('video').evaluate(video=>!video.paused);
    assert(keyboardPlays,'Native player Space key should start playback');
    await page.locator('video').evaluate(async video => {
      video.pause();
      await new Promise(resolve => {video.addEventListener('seeked',resolve,{once:true}); video.currentTime=video.duration-0.7;});
      await video.play();
    });
    await page.waitForFunction(()=>document.querySelector('video').ended,null,{timeout:30000});
    assert.deepEqual(errors,[]);
    const range=await page.request.get(await page.locator('video').evaluate(video=>video.currentSrc),{headers:{Range:'bytes=0-1023'}});
    assert.equal(range.status(),206); assert.equal((await range.body()).length,1024);
    const result={locale,metadata,playback,seek,mobile,keyboardPlays,ended:true,range206:true,errors};
    fs.writeFileSync(path.join(out,'browser.json'),JSON.stringify(result,null,2)+'\n');
    console.log(JSON.stringify(result));
  } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
