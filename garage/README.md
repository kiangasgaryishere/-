# GARAGE cumulative preview
Latest: video/garage-through-030s-v008.mp4. Prior exports are preserved.

V008 changes only the lamp-to-house transition25.4–26.85. The30s duration, lamp's+2s extension, house assembly, Persian text and complete V007soundtrack remain. TREATMENT-v008.md explains the optical handoff. Source frames25/27.2/29.2 were compared against V007 and matched exactly.

## Render this version
Renderer: /workspace/video-tools/lemo-opuscar, commit f2471cacca270963baa2e1c72b8a7b25dfe0d95c. Node20+, Chromium and FFmpeg7+ are installed. From the renderer root:

```bash
PLAYWRIGHT_CHROME=/usr/bin/chromium LEMO_ANGLE=swiftshader node core/render/video.mjs /workspace/-/garage --q start=20 --fps 30 --size 1080x1920 --workers 1 --out /workspace/garage-production-v008/continuation.mp4
bash /workspace/-/garage/assemble30_v008.sh
```

Use one worker for the optical filter pass; a two-worker attempt timed out on screenshots in software graphics. No resolution/quality reduction is used. assemble30_v008.sh concatenates the approved first20 picture and new10 picture without re-encoding, then copies the exact entire V007AAC stream; no audio build is necessary. Validate with full FFmpeg decode,900frames/30s, first600 frame hashes, and V007AAC packet hash equality.

## Assets and production memory
Same photographic-style generated assets and fonts as V007. No new media. Camera optical blur is temporary and resolves by26.85; all assets remain sharp in the final composition. Fixed grain/paper-cut material, black/white/red, sparse Persian type. Current source narration remains outside Git under /workspace/production-inputs/garage. Earlier audio builders need that source and reconstructed score/SFX/VCSL; historical original mastered stems are unavailable. Do not publish source narration, full libraries or caches. Old build scripts correspond to their matching historical source revisions. Canonical timing is timeline.json; decisions and credits are in project Markdown; QC.json records actual validation and unperformed listening/ASR checks.
