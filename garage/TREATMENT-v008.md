# V008 — cinematic lamp-to-house handoff
Scope: transition only. Preserve30s total, lamp assembly/comprehension extension, real-material house assembly timing, all three Persian text labels and source soundtrack. Keep previous versions.

Problem: three white strips and a branch at26.05 produce an abrupt wipe and a near-empty incoming floor frame. Replace that with a continuous, motivated optical handoff.

25.4–26.85: long S-curve overlap. The settled lamp receives a restrained3.5% push and30px drift while its edges progressively defocus and its layer gently fades. No white bars or full-frame flash. The existing localized red light contracts and travels toward the house's red door region, bridging the visual idea without spreading red over the frame. Incoming foundation/body retain26.05/26.4 assembly start times; their complete photographic layer resolves from slight defocus with a small matching settle in scale. No false3D orbit. Continue natural roof assembly27.1–28.2 and untouched final composition.

Technique: independent transparent offscreen render layers, per-frame clear, explicit context arguments and group compositing so alpha/blur do not get overridden by child sprites. Quintic smoothstep for zero endpoint velocity/acceleration. Transition blur is temporary; full sharpness restored by26.85. Exact original source render outside25.4–26.85. Text stays sharp and at original times.

Audio: stream-copy the complete approved V007AAC soundtrack; no narration/music/Foley retiming, extra whoosh, re-master or duplicate speech. The existing quiet paper cue remains as the subtle material bridge.

Preproduction: review three transitional frames and closer motion strip; confirm no cut-to-black, bright white bars, hard edge wipe, floating duplicated house/lamps or lingering blur after transition. Validate300 new frames,900 cumulative,30s, full decode; first600 approved picture frame hashes unchanged and copied audio packet hashes equal V007. Save version and verified commit-pinned download.
