Global sample timeline, 48kHz. Full supplied voice decoded and compressed once; unchanged speed and word order. Original 94BPM swung draft; real CC0 harmonica responses placed inside measured pauses. Paper, pencil and switch cues listed in timeline.json; synced via source asset sync offsets. Full-length mix mastered once, then samples [0,480000) extracted for ten-second AAC. No narration fade or segment-normalization at ten seconds. Headphones/listening review not performed; audio aesthetic remains for user review.

V003: extend from canonical mix-full-master.wav with new CC0 harmonica responses and physical SFX only after 10 seconds. First 480000 pre-encode mix samples unchanged; current 0–20 PCM encoded into AAC once. The narrator is never spliced at the ten-second boundary. No repeated normalization.

V004: original master stems are absent. Recover first 960000 mono PCM samples from approved v003 AAC and retain them unchanged before encoding a single new continuous 30-second AAC stream. Uploaded narrator aligns at zero lag (checked 15–19s, correlation .925). Continue original source samples 960000–1439999 at measured gain 1.4433, with soft peak compression above .65; no narration time edit, repeated syllables or boundary fade. A .18s residual soundtrack bridge reduces music into a quieter question/sketch passage. Four sparse CC0 SFX Kit cues support paper, pencil and assembly. This does not reproduce the old master losslessly; existing first 600 picture frames are stream-copied. No listening or ASR review claimed.


V005 supersedes V004 music reduction. Reconstruct original rng810 94BPM bass/brush/kick and muted guitar from make_audio.py, full global clock 0–58.25925; no reset at20. Fit narrator and score gains against approved16–20, music gain1.82746, voice1.44285. New music stem measured nonzero in every second20–30. Retain approved first20 decoded PCM, mix continuous narrator source thereafter and four sparse CC0 material cues. No recycled residual speech; 5ms additive join continuity correction, no source-time edit. Historical mastered stems unavailable; final AAC encoded once.


V006: keep continuous reconstructed94BPM bass/percussion/guitar under untouched source timing. VCSL harmonica20.85–21.11 and29.3–29.59 uses measured quiet source intervals20.6–21.47 and29.20–29.79 (RMS<.012); no claim of listening review. Sparse CC0 Foley is synchronized to first target contact of damped arrival, not last settle: base20.955, arm21.624, shade22.340, switch23.05, architectural floor24.205, walls24.902/25.340, roof26.152. Quiet paper bridges20.35/24/28.25. Historical mastered stems absent; first20 decoded approved PCM retained and new continuous AAC encoded once.


V007: source narration and94BPM score remain continuous at original timing, including harmonica in verified quiet source windows20.85/29.3. Keep lamp contact/switch cues. Page-turn shifts24→26; house material first contacts26.181/26.602/27.362, title paper slide27.6. No speech stretch, pause or duplication to extend lamp; total30s maintained. Single continuous AAC encode. No new listening claim.

V007 final timing refinement: the+2s lamp scene is split into+1s assembly (20.8–23.95 versus20.8–22.95) and+1s settled hold. Only visual sample time is mapped; original speech/music remain on the global clock. Lamp first-contact cues21.027/22.007/23.056, light switch24.05. Transition ends26.05 as planned.


V008 is visual only: exact complete V007AAC stream copied into new export; no audio decode/re-encode, effects changes, narration edits or music retiming. Existing soft paper cue at26 remains. Audio payload hashes must match prior version.


V009 extends original source narration and continuous94BPM score to33seconds, samples0–1583999, with no time edits, speed changes, repeated words or music reset. Keep first20 recovered approved PCM; all33 seconds encoded to AAC once. Existing quiet harmonica20.85/29.3 retained. House contact cues retimed to base27.0, body28.65, roof30.2; title paper29.8. Score RMS checked nonzero every second20–33. This is a longer cumulative preview, not a finished58s film.
