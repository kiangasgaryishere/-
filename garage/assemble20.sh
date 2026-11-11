#!/usr/bin/env bash
set -euo pipefail
cd /workspace/projects/garage
printf "file '/workspace/projects/garage/video/picture-010s-v002.mp4'\nfile '/workspace/projects/garage/video/picture-010-020s-v003.mp4'\n" > video/concat-020s-v003.txt
ffmpeg -v error -y -f concat -safe 0 -i video/concat-020s-v003.txt -an -c:v copy video/picture-020s-v003.mp4
ffmpeg -v error -y -i video/picture-020s-v003.mp4 -i audio/mix-020s-v003.wav -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart video/garage-through-020s-v003.mp4
ffmpeg -v error -i video/garage-through-020s-v003.mp4 -f null -
ffmpeg -v error -y -ss 9 -i video/garage-through-020s-v003.mp4 -t 2 -vf 'fps=4,scale=216:384,tile=4x2' -frames:v 1 join-review-v003.jpg
ffmpeg -v error -y -i video/garage-through-020s-v003.mp4 -vf 'fps=1/2,scale=216:384,tile=5x2' -frames:v 1 contact-sheet-v003.jpg
