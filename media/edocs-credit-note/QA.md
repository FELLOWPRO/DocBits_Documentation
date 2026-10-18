# Local QA record

Nine localized films and caption tracks accompany the documentation. Each film has eight scenes and synthesized narration in the requested language. The language request and exact narration text were verified against the cached speech metadata.

| Language | Duration | MP4 bytes | Visual / browser / media checks |
| --- | ---: | ---: | --- |
| en | 88.367 s | 2,927,877 | Passed |
| de | 113.167 s | 3,987,235 | Passed |
| es | 116.767 s | 4,196,546 | Passed |
| fr | 99.567 s | 3,487,470 | Passed |
| it | 109.667 s | 3,853,243 | Passed |
| nl | 97.133 s | 3,479,916 | Passed |
| pl | 102.500 s | 3,738,339 | Passed |
| pt | 116.533 s | 4,143,007 | Passed |
| zh | 96.033 s | 2,972,897 | Passed |

Media checks cover H.264 Main/yuv420p 1280×720 at 30 fps, AAC-LC 48 kHz stereo, full decoding, faststart, duration and size, final loudness and peak, exact captions and speech coverage, silent joins, and source freshness. No narration was trimmed or stretched.

Visual review covers all eight scenes, setup/action/result frames, localized labels and 380 px samples. Browser checks cover real playback, seeking, end of playback, native captions, keyboard Space control, a 380 px viewport without horizontal overflow, and local HTTP Range 206 responses. Contact sheets, mobile samples and browser captures are retained per language.

**Listening was not performed.** The available audio-file reader rejected the worktree path. These checks do not certify pronunciation or native-speaker listening quality. The local player allows the narration to be reviewed.

Documentation checks cover all nine live languages: navigation and matching titles, all new relative links and media references, original content and metadata preservation, balanced GitBook blocks, screenshot bytes, approved video hashes, and exact parity between each local language source branch and its main-language mirror.

The source package was reapplied to the recorded API commit and compared byte for byte with the renderer inputs. The original toolchain, font, brand and voice locks remain unchanged. The complete hashes and measurements are in [report.json](qa/report.json). Detailed audio and caption checks are in [media-checks.json](qa/media-checks.json). Full speech caches, native provider alignments, timing plans, render logs and provenance remain in the local build output.

Renderer tests: 57 passed in the locked environment with the final sources present: 53 pipeline regressions and 4 eDocs manifest contract checks. Logs: [pipeline](qa/renderer-tests.txt), [eDocs manifest](qa/edocs-manifest-tests.txt). All nine new variants were separately rendered and reviewed.

All results are local. Public GitBook rendering, anonymous CDN playback, deployment and publication gates have not been evaluated.
