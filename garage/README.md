# GARAGE cumulative preview
Latest: video/garage-through-033s-v010.mp4. Prior versions retained.

V010: large one/two-word editorial highlights throughout, Lalezar, physical camera entry through the garage into the lamp, restrained study push/pull and final house settle. No more than two words simultaneously; paired questions leave before final ایده عجیب. Existing33s narration/music and house construction retained. See TREATMENT-v010.md and highlight-audit-v010.json.

## Build this version
Renderer: /workspace/video-tools/lemo-opuscar, commit f2471cacca270963baa2e1c72b8a7b25dfe0d95c. From renderer root:

```bash
mkdir -p /workspace/garage-production-v010
PLAYWRIGHT_CHROME=/usr/bin/chromium LEMO_ANGLE=swiftshader node core/render/video.mjs /workspace/-/garage --fps 30 --size 1080x1920 --workers 1 --out /workspace/garage-production-v010/picture-033s.mp4
bash /workspace/-/garage/assemble33_v010.sh
```

One worker avoids screenshot timeouts during optical transitions. Native1080x1920,30fps,CRF14/JPEG95 picture. Complete48kHz AAC copied from trackedV009 export; no new audio encode. Canonical timeline: timeline.json,990frames,1584000source samples. Text count is enforced in each rendered frame; frame fields use ceiling to match continuous start/end anchors. Text timings are editorial, not verified word-aligned captions.

Genuine Lalezar Regular400/OFL license included. Optical+30% glyph sizing retained; long highlights uniformly fit safe width. Noto retained only as nonvisible measurement reference. House foundation26.05–27.0, body26.8–28.65, roof28.25–30.2, finished hold30.2–33. Original narration/script remain unchanged; source media and dependencies remain outside Git. Historical mastered stems absent; soundtrack reconstruction documented in SOUND_PLAN.md and prior build scripts. QC.json records actual checks and unperformed listening/ASR. This is a cumulative33s preview of a longer film.
