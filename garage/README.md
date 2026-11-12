# GARAGE cumulative preview
Latest: video/garage-through-033s-v009.mp4. Prior versions retained.

V009: Lalezar throughout Persian type, optically+30% visible headline height,33s total, slower precisely aligned house construction and longer finished hold. English GARAGE unchanged. See TREATMENT-v009.md and font-metrics-v009.json. Genuine Lalezar/OFL license included. Old Noto is retained for nonvisible optical metric reference only.

## Build this version
Renderer: /workspace/video-tools/lemo-opuscar, commit f2471cacca270963baa2e1c72b8a7b25dfe0d95c. Python is its .venv/bin/python. From renderer root:

```bash
mkdir -p /workspace/garage-production-v009
PLAYWRIGHT_CHROME=/usr/bin/chromium LEMO_ANGLE=swiftshader node core/render/video.mjs /workspace/-/garage --fps 30 --size 1080x1920 --workers 1 --out /workspace/garage-production-v009/picture-033s.mp4
.venv/bin/python /workspace/-/garage/build_audio33_v009.py
bash /workspace/-/garage/assemble33_v009.sh
```

Full0–33 rerender is necessary for the global font change. Do not concatenate the old first20 video, which has old typography. One worker avoids screenshot timeouts during the optical transition. Output remains native1080x1920,30fps,CRF14/JPEG95 picture and48kHz AAC.

Audio prerequisites: original prepared voice at /workspace/production-inputs/garage/voice-prepared.wav; recovered approved first20 PCM at /workspace/garage-production-v004/approved-audio.wav; reconstructed full score at /workspace/garage-production-v005/audio/music-full-draft.wav (reconstruct_score_v005.py), SFX Kit and VCSL under /workspace/video-tools. Original narration stays outside Git. Never publish source audio, libraries or caches. Canonical timeline is timeline.json:990frames,1584000 samples. No source-time edits. House finishes30.2 and holds to33. Original historical audio stems remain absent. Prior build scripts require their matching source revisions. QC.json distinguishes verified media/visual checks from unperformed listening/ASR.
