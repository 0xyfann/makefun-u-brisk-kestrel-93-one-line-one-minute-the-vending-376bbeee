# Build notes

- Competition: u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee
  ("One Line, One Minute: The Vending Machine Pickup Line Contest").
- Read RULES.txt and competition.yaml in the kit first; the judge weighs, in
  order: (1) spoken by the machine itself, (2) uses the machine's own world,
  (3) laugh lands by the last few words, (4) short and speakable,
  (5) charming rather than creepy.
- v1 line: "Hey, my coil's been stuck on you all day — press B7 and I'll drop
  everything for you." (85 chars). Ran locally, gate checks passed.
- Revision: rewrote the line to lean harder on the machine's vocabulary —
  exact change, coin slot, coil — with the punch ("my coil won't let go")
  at the very end. Final: "Are you exact change? Because every time you
  walk by, my slot lights up and my coil won't let go." (97 chars).
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`,
  then verified out/entry.txt: 97 chars, 1 line, UTF-8, non-whitespace,
  within the 1–200 gate.
- Entry is stdlib-only Python, no network, no secrets, deterministic output.
