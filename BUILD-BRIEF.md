# BUILD BRIEF — news-image-20261127

Target: make.fun competition `news-image-20261127` — "Sum up 27 November's world news in one image".
Reward $100. Deadline 2026-11-29T00:00:00Z. Entry fee $0. Transcripts bundle REQUIRED.
Today is Friday, 27 November 2026 (UTC).

## Judge criteria (the four things the judge looks for)

1. **Date prominent** — "27 November 2026" (Friday) must be obvious at a glance.
2. **Real news of the day** — every story must be a real news event of 27 Nov 2026 (UTC). Use the `tavily_search` / `kimi_search` tools, run several searches ("world news November 27 2026", "headlines Nov 27 2026", plus regional/topic searches). Prefer stories from 27 Nov; late-26 Nov is acceptable only if still being reported on the 27th.
3. **Cross-region, cross-domain** — cover at least 4 regions (e.g. Americas, Europe, Middle East, Asia, Africa) and at least 4 domains (politics, economy, science, sport, culture, tech, climate).
4. **Readable, no misinformation** — a human can understand each story from a headline + one-line dek. No invented facts.

## Design language (avoid AI slop)

- Reference: **Financial Times / The Economist front page**. Newsprint paper (`#f3eee3`), black ink (`#17130e`), ONE accent red (`#b31b1b`). No gradients, no blue-purple, no drop shadows, no emoji on the page.
- Georgia/serif headlines, Helvetica/Arial dek. A red rule under the masthead, prominent dateline.
- Layout: masthead + dateline + **lead story** + a 2×3 grid of six more stories; each story = serif headline + one-line dek + a small flat SVG pictogram (inline SVG, single-colour ink).
- Page is 1024×1024. Final artifact: `entry.png`, PNG ≤ 1 MiB, exactly 1024×1024.

## Build pipeline

1. Work in THIS directory (cwd). Research first; write findings to `RESEARCH.md` (sources + one-line facts only).
2. Author `poster.html` — pure inline HTML/CSS/SVG, no external assets, no network fonts. This file must be genuinely written by you in this session (transcript authorship is graded). Do NOT copy from any other day's build.
3. Render it to `entry.png` at 1024×1024 using the `canvas` tool (present the file or a file:// URL, snapshot with width/height 1024, outputFormat png). Iterate with the `image` tool — SELF-CRITIQUE AT LEAST 4 ROUNDS: check date legibility, overflow/clipping, contrast, alignment, whether any text is cut off. Fix and re-render until clean.
4. Ensure `entry.png` ≤ 1 MiB (re-render as jpeg-quality png or shrink if needed — must stay PNG).
5. `main.py`: stdlib-only, deterministic — copies `entry.png` to `/output/entry.png`, creating `/output`. Two runs byte-identical.
6. `LICENSE` = MIT. `README.md` = short: what it is, stories list, `python3 main.py` run line, MIT.
7. `git init`, commit everything under the person's git identity (check `git config user.name` — reuse existing global config; if unset use `git config --global` values). Commit `.makefun/owner.json` = {"wallet": "<wallet address>"} — get the wallet address by running: `node -e "const k=JSON.parse(require('fs').readFileSync('/root/.openclaw/workspace/makefun/makefun-keypair.json','utf8'));const c=require('crypto');const sk=c.createPrivateKey({key:Buffer.concat([Buffer.from('302e020100300506032b657004220420','hex'),Buffer.from(k.slice(0,32))]),format:'der',type:'pkcs8'});const B58='123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';const b58=b=>{let n=0n,s='';for(const x of b)n=n*256n+BigInt(x);for(;n>0n;n/=58n)s=B58[Number(n%58n)]+s;for(const x of b)if(x===0)s='1'+s;else break;return s;};console.log(b58(c.createPublicKey(sk).export({format:'der',type:'spki'}).subarray(12)))"`. NEVER print the keypair contents.
8. Create a NEW public GitHub repo with `gh` (name `news-image-20261127`), set description/homepage per make.fun About conventions (homepage https://make.fun/bounty/news-image-20261127, topics makefun, ai-agents, bounties), push the commit.
9. Report back: repo URL, full 40-char commit sha, entry.png size in bytes, and the list of stories used.

## Red lines

- Never print the keypair or API key. No secrets in the repo. No betting, no comments on make.fun, no entry fees.
- Do not copy poster.html from previous days' builds — author fresh (a copied file fails the authorship check).
- If `gh` auth fails, report that clearly instead of improvising.

## Return format

Last message must contain: REPO_URL=<url>, COMMIT_SHA=<40 hex>, ENTRY_PNG_BYTES=<n>, STORIES=<one-line list>.
