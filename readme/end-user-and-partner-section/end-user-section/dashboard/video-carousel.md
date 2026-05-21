# Video Carousel

The Video Carousel on the Prepare Dashboard shows short, narrated product tips while documents are being prepared for processing. Each clip introduces a feature or workflow you can try next.

## Where to find it

The Video Carousel appears on the [Prepare Dashboard](README.md) — the page you see when documents are being imported and prepared. On wide screens it sits in the right column next to the progress indicator. On smaller screens it is hidden to keep the layout focused on the progress information.

<figure><img src="../../../.gitbook/assets/video-carousel-prepare-dashboard.png" alt="Video Carousel on Prepare Dashboard"><figcaption><p>The Video Carousel shows short product tips while documents are being prepared.</p></figcaption></figure>

## How it works

Each visit to the Prepare Dashboard picks six tips at random from the current catalog. Videos autoplay one after the other, muted by default. Each clip runs for roughly seven seconds. The dot indicator below the video fills as the timer counts down, then advances to the next clip.

The clip currently playing is the only one fetched in full — subsequent clips begin preloading after the first one starts so the transition is smooth.

## Navigating between videos

Click any of the dots below the video to jump to that clip immediately. The hint text under the video updates to describe what the current clip shows.

## Why videos rotate

The product team uses the carousel to surface less-discovered features without adding more icons to the sidebar. New videos are added with each release and the catalog is refreshed automatically — there is nothing to install.

<mark>Videos play muted with a tip caption underneath. If you want sound, click the video to focus it and use the standard browser playback controls.</mark>

## Privacy

Video clips are pre-rendered marketing content. Nothing about you, your documents, or your organisation is sent when a clip plays — the carousel is read-only and stateless.
