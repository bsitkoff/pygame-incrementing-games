# Video Script: Changing a List While the Game Runs

**File on screen:** `lists.py` (modified live during recording)
**Pre-made demo files:** `lists_moving.py`, `lists_remove.py` (in case live-coding goes wrong)
**Objective:** I can add and remove sprites from a list during gameplay.
**Length target:** 4-5 minutes

---

## INTRO (~15 seconds)

"Now that you've seen how lists and for loops work together, let's change things. We're going to make three modifications to `lists.py` — change the count, add movement, and remove items from a list."

---

## PART 1: Change the count (~60 seconds)

**Show:** `lists.py`, highlight the jellyfish creation loop (lines 22-26):

```python
jellyfish = []
for i in range(3):
```

"The easiest change — this number in `range()` controls how many jellyfish get created. Let's crank it up."

**Live edit:** Change `range(3)` to `range(8)`.

"Eight jellyfish. And while we're at it…"

**Show:** Highlight plankton creation (lines 16-19).

**Live edit:** Change `range(5)` to `range(1)`.

"Just one plankton. Let's run it."

**Show:** Run `python3 lists.py` in terminal. Play briefly.

"Way harder — eight jellyfish filling the screen and only one piece of plankton to chase. We didn't touch the for loops at all. They still loop through whatever's in the list. The list is just bigger now."

**Live edit:** Change back to `range(3)` and `range(5)` before moving on (or note that students should do this).

---

## PART 2: Make the jellyfish move (~90 seconds)

**Show:** Highlight the shark movement code in `update()` (lines 70-72):

```python
shark.x += shark.dx
if shark.x < 0 or shark.x > WIDTH:
    shark.dx = -shark.dx
```

"The shark already moves — it has a `dx` property that gets added to its `x` position every frame. When it hits the edge, `dx` flips direction. We want to do something similar for jellyfish, but simpler: just drift them downward."

**Live edit:** Add this code in `update()`, after the shark movement block (after line 72, before the plankton collision loop):

```python
    # Jellyfish drift downward
    for j in jellyfish:
        j.y += 1
        if j.y > HEIGHT:
            j.y = 0
            j.x = random.randint(50, WIDTH - 50)
```

"We loop through every jellyfish and add 1 to its `y` position — that moves it down. When it drifts past the bottom of the screen, we send it back to the top at a random `x` position. It's like they're raining down."

**Show:** Run `python3 lists.py`. Play and show the jellyfish drifting.

"Now the jellyfish are moving. The game feels completely different — you can't just sit still anymore. And notice: we wrote this code once in a for loop, and it moves *all* the jellyfish. If we change `range(3)` to `range(10)`, they'd all move too."

---

## PART 3: Remove instead of reposition (~90 seconds)

**Show:** Highlight the plankton collision code (lines 74-78):

```python
for p in plankton:
    if player.colliderect(p):
        score += 1
        p.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
```

"Right now, when you collect plankton, it jumps to a new random position — infinite plankton. But what if we wanted plankton to disappear for good when you collect it?"

**Live edit:** Replace that block with:

```python
    for p in list(plankton):
        if player.colliderect(p):
            score += 1
            plankton.remove(p)
```

"Two changes. First, we call `plankton.remove(p)` instead of repositioning — that takes this specific plankton out of the list permanently. Second — and this is important — we loop over `list(plankton)` instead of just `plankton`. That creates a copy of the list to loop through, because you can't safely remove items from a list while you're looping over it."

**Show:** Run `python3 lists.py`. Collect all the plankton, showing them disappear one by one.

"Watch — each one I collect disappears. The score goes up, the plankton goes away. And when they're all gone… no more plankton. The list is empty."

"This gives you a totally different game mechanic. Collect all 5 plankton to win, instead of an endless score chase. You could even check `if len(plankton) == 0` to trigger a victory screen."

---

## WRAP-UP (~20 seconds)

"Those are three ways to modify a list-based game: change how many sprites you start with, move them with a for loop, and remove them during gameplay. Your turn — try these changes yourself, and describe what you did in the box below."
