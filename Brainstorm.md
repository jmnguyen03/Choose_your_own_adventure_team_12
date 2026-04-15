# Brainstorm.md — Team 12 CYOA Project

## Story Direction
Keep the original "Cave of Time" story from the professor's repo.
The story is already extracted into text files — we just need to present it
as a playable web game.

## Theme & Vibe
- Retro / old-school book feel
- Think aged paper texture, serif fonts, worn edges
- Feels like you're actually flipping through a paperback from the 80s
- Maybe a vintage typewriter or parchment aesthetic

## Website Ideas
- Background: aged/yellowed paper texture
- Font: serif (like Georgia or a typewriter font)
- Page turn animation when moving between story sections
- Display the page number like the real book does ("Page 4")
- Choices appear as clickable buttons styled like old book text
  (e.g., "Turn to Page 12 →")
- A "restart" button at the end of each story path
- Optional: show how many decisions you've made so far

## Technical Approach
- Single HTML page that loads story data via JavaScript
- Story data pulled from the existing `output/cot-pages-ocr-v2/` text files
  and `output/cot-story-graph.mmd` graph
- No backend needed — runs entirely in the browser
- Deploy via GitHub Pages

## Possible Extra Features (if time allows)
- Sound effect on page turn (old paper rustle)
- A "you died / you won" styled ending screen
- Progress tracker showing which endings you've reached

## What Makes Ours Different
- Actually playable in browser (professor's version is just scripts)
- Authentic retro book aesthetic matching the 1979 original
- Clean UX — no technical knowledge needed to play