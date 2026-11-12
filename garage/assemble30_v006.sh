#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")" && pwd)
WORK=${GARAGE_BUILD_DIR:-/workspace/garage-production-v006}
printf "file '%s'\nfile '%s'\n" "$ROOT/video/garage-through-020s-v003.mp4" "$WORK/continuation.mp4" > "$WORK/concat.txt"
ffmpeg -v error -y -f concat -safe 0 -i "$WORK/concat.txt" -map 0:v:0 -an -c:v copy "$WORK/picture-030s.mp4"
ffmpeg -v error -y -i "$WORK/picture-030s.mp4" -i "$ROOT/audio/mix-030s-v006.wav" -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -t 30 -movflags +faststart "$ROOT/video/garage-through-030s-v006.mp4"
ffmpeg -v error -i "$ROOT/video/garage-through-030s-v006.mp4" -f null -
