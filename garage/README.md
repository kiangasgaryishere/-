# GARAGE cumulative preview
Latest: video/garage-through-030s-v007.mp4. Earlier exports retained.

Renderer: /workspace/video-tools/lemo-opuscar, commit f2471cacca270963baa2e1c72b8a7b25dfe0d95c.
From renderer root:
PLAYWRIGHT_CHROME=/usr/bin/chromium LEMO_ANGLE=swiftshader node core/render/video.mjs /workspace/-/garage --q start=20 --fps 30 --size 1080x1920 --workers 2 --out /workspace/garage-production-v005/continuation-final.mp4

This renders master 20–30 only. Run build_audio30_v005.py with renderer's .venv/bin/python, then bash assemble30_v005.sh. Original safari.mp3 and prepared WAV live outside Git at /workspace/production-inputs/garage; decode approved v003 to /workspace/garage-production-v004/approved-audio.wav first (mono float WAV, 48kHz). SFX Kit at /workspace/video-tools/sfx-kit. Audio files ignored, do not publish source narration or upstream libraries. Historical full soundtrack stems are unavailable.

First 600 picture frames are reused from v003. First twenty seconds of recovered decoded audio are retained before one continuous AAC encode. Continuation uses original voice samples with no wording/speed edits, sparse CC0 Foley and continuous reconstructed original 94BPM music. Not a full reconstruction of the historical master. Exact phrase alignment and full-speed listening are not verified. Canonical timing is timeline.json; no dense subtitles. extend20.py is a historical one-time migration, not a build step.

V005 preparation: reconstruct_score_v005.py writes the original full music/FX draft into /workspace/garage-production-v005/audio (create that directory first). Then build_audio30_v005.py uses that music and recovered approved v003 PCM. The two new generated photographic assets and three preproduction style frames are documented in TREATMENT-v005.md and style-review-v005.jpg.

V006 revision: REFERENCES.md and TREATMENT-v006.md record analysis of three uploaded videos and the motion/shot plan. Independent lamp and architectural component atlases replace chair imagery after20. From renderer root render with --q start=20 and --out /workspace/garage-production-v006/continuation.mp4, then run build_audio30_v006.py and bash assemble30_v006.sh. It reuses the reconstructed score from reconstruct_score_v005.py, adds VCSL harmonica in measured voice gaps, and regenerates material-contact cues. Assets remain original alpha atlases, cropped only by Canvas. The final Persian invitation is visual only; no speech edits.

V007: lamp scene extended by2seconds within30second total; complete photorealistic house assembles from masked parts of house-v007.png, new questions and final ایده عجیب. Render with --q start=20 --out /workspace/garage-production-v007/continuation-final.mp4 from library root. Run build_audio30_v007.py then bash assemble30_v007.sh. Source/music prerequisites same as V006. See TREATMENT-v007.md for targeted plan and timing. Old assembly/build scripts reproduce old versions only with corresponding old source revisions.
