# ToDo.md — Team 12 CYOA Project

## Instructions for AI
Read Codebase.md first to understand the existing project structure.
The story text is in `output/cot-pages-ocr-v2/` as .txt files.
The story graph (branching paths) is in `output/cot-story-graph.mmd`.
Do not modify any existing scripts or output files.

---

## Task 1 — Parse the Story Data
- Write a Python script `scripts/build_story_json.py` that:
  - Reads all .txt files from `output/cot-pages-ocr-v2/`
  - Reads the story graph from `output/cot-story-graph.mmd`
  - Outputs a single `output/story.json` file with this structure:
```json
    {
      "2": {
        "text": "You've hiked through Snake Canyon...",
        "choices": [
          { "text": "Turn to page 4", "page": "4" },
          { "text": "Turn to page 5", "page": "5" }
        ]
      }
    }
```
  - Terminal pages (no choices) should have `"choices": []`
  - Start page is page 2

---

## Task 2 — Build the Web Game
- Create `index.html` in the root of the repo
- It should be a single self-contained HTML file (HTML + CSS + JS all in one)
- Load `output/story.json` via fetch()
- Display the current page's text and choices
- When a choice is clicked, navigate to that page
- Show the page number like the real book ("Page 4")
- Track how many decisions the player has made

### Visual Style (retro book aesthetic):
- Background: aged/yellowed parchment color (#f5f0e8 or similar)
- Font: Georgia or a serif font for story text
- Typewriter-style font for the title
- Choices styled as clickable links that look like book text
  e.g. "→ Turn to Page 4"
- A worn/faded border around the text area
- Ending screen when choices = [] with a "Start Over" button

---

## Task 3 — Deploy to GitHub Pages
- Make sure `index.html` is in the root of the repo
- Go to repo Settings → Pages → set source to `main` branch, `/ (root)`
- Confirm the site is live at:
  `https://jmnguyen03.github.io/Choose_your_own_adventure_team_12/`

---

## Task 4 — Update README.md
Replace the current README.md content with:
- Project title
- Short description
- Live site URL
- GitHub repo URL
- Team member names
- How to run locally (just open index.html in a browser)

---

## Task 5 — Update Codebase.md
Ask AI to read the current Codebase.md and append a new section
describing the web game we added, the story.json format, and
how index.html works.