#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")" && pwd)
WORK=${GARAGE_BUILD_DIR:-/workspace/garage-production-v011}
# Sound-only revision: preserve every V010 picture packet, one continuous new AAC stream.
ffmpeg -v error -y -i "$ROOT/video/garage-through-033s-v010.mp4" -i "$WORK/mix-033s-v011.wav" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -t 33 -movflags +faststart "$ROOT/video/garage-through-033s-v011.mp4"
ffmpeg -v error -i "$ROOT/video/garage-through-033s-v011.mp4" -f null -
