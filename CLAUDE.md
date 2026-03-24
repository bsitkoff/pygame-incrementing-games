# This Assignment: Lesson 6 — Incrementing Games

PRIMM lesson on lists of sprites. `lists.py` is an ocean game with lists of jellyfish and plankton. Students explore list creation, for-loop collision checking, and list modification.

**Student files**: `lists.py` (example), `tryit.py` (student work), `images/`
**Key concepts**: Lists of Actors, for loops in update()/draw(), removing items from lists, range()
**Guide pages**: Get Ready → Try It Out → Change It → Create Your Own → Playtest and Reflect
**Note**: `Page-1-09a5.md` is an orphan page (not in index.json). Two videos not yet recorded (scripts exist).

---

# PyGame Zero Unit — Codio Assignment

This is one assignment in a 7-lesson PyGame Zero unit for 8th graders at Milton Academy, authored by Bridget Sitkoff. The unit teaches game programming concepts incrementally using PyGame Zero in Codio.

## Unit Sequence

| # | Repo | Title | Model | Key Concepts |
|---|------|-------|-------|-------------|
| 1 | `pygame-intro-game-design` | Intro to Game Design | Intro | Actor, draw(), update(), Game Changineer |
| 2 | `pygame-moving-sprites` | Moving Sprites | PRIMM | Keyboard input, boundaries, Actor positioning |
| 3 | `pygame-colliding-sprites` | Colliding Sprites | PRIMM | colliderect(), enemy chasing, collectibles |
| 4 | `pygame-keeping-track` | Keeping Track | PRIMM | global keyword, score, game states, screen.draw.text() |
| 5 | `pygame-polishing-games` | Polishing Games | PRIMM | UI/UX design, Flappy Bird clone, theming |
| 6 | `pygame-incrementing-games` | Incrementing Games | PRIMM | Lists of Actors, for loops, removing from lists |
| 7 | `pygame-game-jam` | Game Jam | Milestone | Capstone assessment, three difficulty tiers |

## Codio Assignment Structure

```
project-root/
├── CLAUDE.md              ← You are here (excluded from student view)
├── .assignmentignore      ← Hides files from students
├── index.json             ← Page ordering and assignment settings
├── .guides/
│   ├── content/           ← Guide pages (paired .md + .json files)
│   ├── assessments/       ← Assessment config JSON files
│   ├── img/               ← Images used in guide pages
│   └── secure/            ← Hidden from students: solutions, grading scripts, video scripts
├── images/                ← Sprite images (students can see and add to this)
└── *.py                   ← Python files students interact with
```

### Guide Pages

Each page is a pair: `PageName-XXXX.md` (content) + `PageName-XXXX.json` (layout/config). The `XXXX` is a 4-character UUID suffix. Pages are ordered by the `order` array in `index.json` (reference pages WITHOUT extensions).

### Assessment Types

- **free-text-auto**: LLM-checked engagement questions (not correctness). Uses `freetext.py` in `.guides/secure/`. Syntax in markdown: `{Check It!|assessment}(free-text-auto-XXXXXXXXXX)`
- **llm-based-auto-rubric**: Automated code grading with rubric items. Points to solution files in `.guides/secure/`. Syntax: `{Check It!|assessment}(llm-based-rubric-XXXXXXXXXX)`
- **free-text**: Manual teacher grading for open-ended reflections. Syntax: `{Submit Answer!|assessment}(free-text-XXXXXXXXXX)`

Assessment configs live in `.guides/assessments/` as JSON. Assessment IDs in the markdown must match the `taskId` in the corresponding JSON file.

### Layouts (in .json files)

- `1-panel-tree` — guides only (planning, reflection pages)
- `4-cell-guides-left` — guides left, code file open, preview, terminal
- `3-columns-tree-guides-left` — guides, code, preview

## Pedagogical Models

### PRIMM (Lessons 2-6)

Pages follow this sequence:
1. **Get Ready** — prediction question or warmup
2. **Try It Out** — explore working example code
3. **Change It** — guided experiments modifying the example
4. **Create Your Own** — build something new (has LLM rubric)
5. **Playtest and Reflect** — peer feedback and self-reflection

### Milestone (Lesson 7)

1. **Planning** — tier choice, design questions, reference table
2. **Coding** — implementation with autograder
3. **Reflecting** — playtesting and reflection

## Conventions

- **Run command**: Always `python3 filename.py` in terminal instructions. Never `pgzrun` in terminal. (`import pgzrun` and `pgzrun.go()` in Python files is correct.)
- **Difficulty tiers**: Mild (green circle), Medium (yellow circle), Spicy (red circle)
- **Tone**: Conversational, direct, age-appropriate for 8th grade. Not condescending. Use "you" not "students will."
- **Teacher name**: Ms. Sitkoff (when referenced in student-facing content)
- **Video embeds**: Screencastify iframes for teacher-recorded videos, YouTube iframes for external videos. Missing videos use: `> 📹 **[VIDEO NOT YET RECORDED — description. Script at path]**`
- **Riot Games videos**: "So You Wanna Make Games??" playlist placeholders use: `> 📹 [RIOT VIDEO: Episode N — Title (from "So You Wanna Make Games??" playlist)]`
- **Assessment placeholders**: `> *[ASSESSMENT NEEDED: Create a ... assessment in the Codio GUI — ...]*` (these need to be created in the Codio GUI, not in code)
- **No AI policy**: Lesson 7 (Game Jam) is a no-AI assessment. Other lessons allow the PyGame Zero Coach button.

## Working with This Repo

- **Don't delete files** without confirming with Bridget
- **Don't modify assessment JSON** files directly — assessments are configured in the Codio GUI
- **Don't create index.json** if it doesn't exist — it's managed by Codio
- **Solution files** go in `.guides/secure/` (hidden from students)
- **Commit to a branch**, not main, unless Bridget says otherwise
- **Test Python files** with `python3 filename.py` if pgzrun is available
