# GARAGE opening preview
Latest deliverable: video/garage-through-010s-v002.mp4. Prior v001 export is preserved.
Render: from /workspace/video-tools/lemo-opuscar run PLAYWRIGHT_CHROME=/usr/bin/chromium LEMO_ANGLE=swiftshader node core/render/video.mjs /workspace/projects/garage --fps 30 --size 1080x1920 --workers 2 --out <new-picture.mp4>.
Audio source and full stems are retained locally in /workspace/projects/garage/audio; not committed. make_audio.py expects this source and the installed Opuscar/VCSL/SFX libraries. Font and generated picture assets are included. Never commit credentials, caches or complete upstream libraries.
Canonical timing: timeline.json; motion easing within shots remains in index.html. 10-second export is exactly frames 0–299 and decoded voice samples 0–479999.
