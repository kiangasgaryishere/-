#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")" && pwd)
WORK=${GARAGE_BUILD_DIR:-/workspace/garage-production-v009}
# Full picture rerender is required for the font change throughout0–33.
ffmpeg -v error -y -i "$WORK/picture-033s.mp4" -i "$ROOT/audio/mix-033s-v009.wav" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -t 33 -movflags +faststart "$ROOT/video/garage-through-033s-v009.mp4"
ffmpeg -v error -i "$ROOT/video/garage-through-033s-v009.mp4" -f null -
