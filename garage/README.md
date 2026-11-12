# GARAGE cumulative preview
Latest: video/garage-through-033s-v011.mp4. Prior versions retained.

V011 adds material sound design over unchangedV010 picture. See TREATMENT-v011.md.

V010: large one/two-word editorial highlights throughout, Lalezar, physical camera entry through the garage into the lamp, restrained study push/pull and final house settle. No more than two words simultaneously; paired questions leave before final ایده عجیب. Existing33s narration/music and house construction retained. See TREATMENT-v010.md and highlight-audit-v010.json.

## Build V011 audio revision
V010 picture is copied exactly. Selected CC0 effects are included under audio/sfx-v011; timeline.json contains canonical revision=v011 cues and source hashes. Build with installed renderer Python:

```bash
/workspace/video-tools/lemo-opuscar/.venv/bin/python /workspace/-/garage/build_audio33_v011.py
bash /workspace/-/garage/assemble33_v011.sh
```

Outputs and separate effects/mix stems go to /workspace/garage-production-v011 (override GARAGE_BUILD_DIR). Source prerequisites: existing lossless audio/mix-033s-v009.wav (SHA verified) and /workspace/production-inputs/garage/voice-prepared.wav for effects ducking. Sources remain outside Git; prior scripts document reconstruction if needed. Do not silently replace the lossless master with an AAC decode. Imported WAV hashes/licenses are checked at build. Standard−3.01dB stereo center pan maintains reference mono loudness; narrator/music source samples and timing remain fixed. Effects-only shaping, speech duck and headroom control. One AAC192k encode, native1080x1920/30fps/990frames,33s. Prior picture build: TREATMENT-v010.md. No video rerender needed.

Lalezar enlarged sparse1–2word highlights, physical doorway entry and house construction remainV010. Canonical timeline990frames/1584000samples; this is a cumulative33s preview of a longer film. QC.json separates media/measurement checks from unperformed listening. V011 measures−15.57LUFS and−3.83dBTP on encoded AAC; no full-speed listening claim.
