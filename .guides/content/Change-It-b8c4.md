## Change It

> 📹 **Watch:** Changing a List While the Game Runs
> *Record in Screencastify — show adding and removing sprites from a list during gameplay*
> *Objective: I can add and remove sprites from a list during gameplay.*
> **[ADD VIDEO URL WHEN RECORDED]**

---

## 1: Change the Count

Find the list of jellyfish and the list of plankton in `lists.py`. Change the numbers — try 8 jellyfish, or 1 piece of plankton. How does it feel?

## 2: Add a New Jellyfish When One Is Avoided

When the player avoids a jellyfish (passes it without touching), it would be cool to add another. Try:

```python
if jellyfish.y > HEIGHT:
    jellyfish_list.append(Actor('jellyfish'))
    jellyfish_list[-1].pos = (random.randint(0, WIDTH), 0)
```

*(This only works if jellyfish are moving — you might need to add that first!)*

## 3: Remove a Plankton When Collected

Right now collected plankton probably gets repositioned. Try removing it from the list instead:

```python
if player.colliderect(p):
    plankton_list.remove(p)
    score += 1
```

What happens when the list is empty?

---

> *[TODO: insert free-text-auto assessment — "What did you change? What did you notice about using lists vs single variables?"]*
