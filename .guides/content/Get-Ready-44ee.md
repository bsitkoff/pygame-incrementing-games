## Make a Prediction

Here's a snippet of a game that only has one jellyfish:

```python
jellyfish = Actor('jellyfish')
jellyfish.pos = (100, 200)

def draw():
    jellyfish.draw()

def update():
    if player.colliderect(jellyfish):
        game_over = True
```

Now imagine you want **5** jellyfish. You'd need 5 variables (`jellyfish1`, `jellyfish2`, ...), 5 draw calls, and 5 collision checks. That's a lot of repeated code.

**Before you look at the example, predict:** How might a *list* make this easier? What would change about the `draw()` and `update()` functions?

{Check It!|assessment}(free-text-auto-2732325120)
