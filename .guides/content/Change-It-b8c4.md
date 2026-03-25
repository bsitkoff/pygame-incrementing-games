## Change It


### 1: Change the Count

Find where the `jellyfish` list and the `plankton` list are created in `lists.py`. Change the numbers in `range()` — try 8 jellyfish, or just 1 piece of plankton. Run it again with `python3 lists.py`. How does the difficulty change?

### 2: Make the Jellyfish Move

Right now the jellyfish just sit still. The shark already moves back and forth — find that code and use it as a model. Can you make each jellyfish drift downward? You'll need a `for` loop in `update()` that moves every jellyfish in the list.

Think about: what should happen when a jellyfish drifts past the bottom of the screen?

<details><summary>Hint: how does the shark move?</summary>

Look at how the shark's position changes each frame. The shark uses `shark.x += shark.dx` to move horizontally. For jellyfish drifting down, you'd change their `y` position instead. When a jellyfish goes past the bottom of the screen (`HEIGHT`), you could reposition it back to the top at a random `x` position.

</details>

### 3: Remove Instead of Reposition

When the player collects plankton, the code repositions it to a random spot. What if you *removed* it from the list instead? Here's an example of removing an item from a list:

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ["apple", "cherry"]
```

Try adapting this idea so collected plankton disappears for good. What happens when the list is empty?

---
{Check It!|assessment}(free-text-auto-2943975147)
