#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")" && pwd)
WORK=${GARAGE_BUILD_DIR:-/workspace/garage-production-v008}
printf "file '%s'\nfile '%s'\n" "$ROOT/video/garage-through-020s-v003.mp4" "$WORK/continuation.mp4" > "$WORK/concat.txt"
ffmpeg -v error -y -f concat -safe 0 -i "$WORK/concat.txt" -map 0:v:0 -an -c:v copy "$WORK/picture-030s.mp4"
# This is a visual-only revision: retain the exact complete approved AAC payload.
ffmpeg -v error -y -i "$WORK/picture-030s.mp4" -i "$ROOT/video/garage-through-030s-v007.mp4" -map 0:v:0 -map 1:a:0 -c copy -t 30 -movflags +faststart "$ROOT/video/garage-through-030s-v008.mp4"
ffmpeg -v error -i "$ROOT/video/garage-through-030s-v008.mp4" -f null -
