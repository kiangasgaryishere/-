# GARAGE cumulative preview
Latest: video/garage-through-030s-v004.mp4. Earlier exports retained.

Renderer: /workspace/video-tools/lemo-opuscar, commit f2471cacca270963baa2e1c72b8a7b25dfe0d95c.
From renderer root:
PLAYWRIGHT_CHROME=/usr/bin/chromium LEMO_ANGLE=swiftshader node core/render/video.mjs /workspace/-/garage --q start=20 --fps 30 --size 1080x1920 --workers 2 --out /workspace/garage-production-v004/continuation-fixed.mp4

This renders master 20–30 only. Run build_audio30.py with renderer's .venv/bin/python, then bash assemble30.sh. Original safari.mp3 and prepared WAV live outside Git at /workspace/production-inputs/garage; decode approved v003 to /workspace/garage-production-v004/approved-audio.wav first (mono float WAV, 48kHz). SFX Kit at /workspace/video-tools/sfx-kit. Audio files ignored, do not publish source narration or upstream libraries. Historical full soundtrack stems are unavailable.

First 600 picture frames are reused from v003. First twenty seconds of recovered decoded audio are retained before one continuous AAC encode. Continuation uses original voice samples with no wording/speed edits, sparse CC0 Foley and quieter music. Not a full reconstruction of the historical master. Exact phrase alignment and full-speed listening are not verified. Canonical timing is timeline.json; no dense subtitles. extend20.py is a historical one-time migration, not a build step.
