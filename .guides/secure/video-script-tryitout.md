# Video Script: Lists of Actors

**File on screen:** `lists.py`
**Objective:** I can create a list of sprites and use a for loop to draw and check them all.
**Length target:** 3-4 minutes

---

## INTRO (camera or screen — ~20 seconds)

"In the last lesson, we used `state` and `score` to manage our game's flow — a start screen, gameplay, and a game over screen. That pattern is back in this project. But now we've got a new problem: what if you want a whole *swarm* of jellyfish instead of just one?"

---

## PART 1: The problem with single variables (~30 seconds)

**Show:** Scroll to the top of `lists.py`, but first talk through the hypothetical.

"Imagine you had one jellyfish variable, then you needed five. You'd write `jellyfish1`, `jellyfish2`, `jellyfish3`… then five separate draw calls, five collision checks — it gets out of hand fast. Lists solve this."

---

## PART 2: State variables — quick callback (~30 seconds)

**Show:** Highlight lines 8-9 of `lists.py` (line 7 is the comment above):

```python
# State variables — same pattern as the last lesson
state = "start"
score = 0
```

"Before we get to lists, notice these two lines. `state` and `score` — same pattern as the last lesson. The game starts in the `"start"` state, and we change it to `"playing"` when you press SPACE, or `"game_over"` when you hit a jellyfish. This controls which screen the player sees."

**Show:** Briefly scroll to `draw()` and point out the three `if/elif` blocks.

"In `draw()`, we check the state — if it's `"start"`, show the title. If it's `"playing"`, draw the game. If it's `"game_over"`, show the final score. You've seen this before."

---

## PART 3: Creating a list of sprites (~60 seconds)

**Show:** Highlight lines 15-19:

```python
plankton = []
for i in range(5):
    p = Actor('plankton')
    p.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    plankton.append(p)
```

"Here's where lists come in. We start with an empty list — `plankton = []`. Then a `for` loop runs 5 times. Each time through, it creates a new Actor, gives it a random position, and appends it to the list. When we're done, `plankton` is a list of 5 separate sprites."

**Show:** Highlight lines 22-26:

```python
jellyfish = []
for i in range(3):
    j = Actor('jellyfish')
    j.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    jellyfish.append(j)
```

"Same thing for jellyfish — 3 of them this time. Want more? Just change the number in `range()`. That's it."

---

## PART 4: Drawing with a for loop (~30 seconds)

**Show:** Highlight the for loops in `draw()`, around lines 103-107:

```python
for p in plankton:
    p.draw()

for j in jellyfish:
    j.draw()
```

"In `draw()`, instead of calling `.draw()` on five separate variables, we loop through the list. `for p in plankton` — that goes through each plankton in the list, one at a time, and draws it. Same for jellyfish. If the list has 3 items, it draws 3. If it has 30, it draws 30. The code doesn't change."

---

## PART 5: Collision checking with a for loop (~40 seconds)

**Show:** Highlight lines 74-78:

```python
for p in plankton:
    if player.colliderect(p):
        score += 1
        p.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
```

"Collision checking works the same way. This loop goes through every plankton in the list and checks: did the player touch this one? If yes, add a point and move it to a new random position."

**Show:** Highlight lines 81-83:

```python
for j in jellyfish:
    if player.colliderect(j):
        state = "game_over"
```

"For jellyfish, same loop structure — but instead of adding points, we change `state` to `"game_over"`. See how the state variable and the list work together? The loop checks every jellyfish, and if any of them touch the player, the game ends."

---

## PART 6: Run the game (~30 seconds)

**Show:** Switch to terminal, run `python3 lists.py`.

"Let's see it in action."

*Play the game briefly — collect some plankton, show the score going up, then get hit by a jellyfish.*

"Start screen, gameplay with a score, game over with a final score — that's our state pattern. And all those jellyfish and plankton? Managed by two lists and a few for loops."

---

## WRAP-UP (~15 seconds)

"Your job on this page is to play the game and look through the code. Find the lists, find the for loops, and think about what you'd change to add more jellyfish or plankton. Answer the question below when you're ready."
