#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")" && pwd)
WORK=${GARAGE_BUILD_DIR:-/workspace/garage-production-v010}
# Full picture rerender for new highlights and camera; preserve the complete prior AAC.
ffmpeg -v error -y -i "$WORK/picture-033s.mp4" -i "$ROOT/video/garage-through-033s-v009.mp4" -map 0:v:0 -map 1:a:0 -c copy -t 33 -movflags +faststart "$ROOT/video/garage-through-033s-v010.mp4"
ffmpeg -v error -i "$ROOT/video/garage-through-033s-v010.mp4" -f null -
