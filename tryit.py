import pgzrun
import random

WIDTH = 800
HEIGHT = 600

state = "start"
score = 0

player = Actor('fish')
player.pos = (WIDTH // 2, HEIGHT // 2)

# One jellyfish to start — your job: put multiple in a list!
jellyfish = Actor('jellyfish')
jellyfish.pos = (100, 100)

# One piece of plankton — your job: put multiple in a list!
plankton = Actor('plankton')
plankton.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

def reset_game():
    global score
    score = 0
    player.pos = (WIDTH // 2, HEIGHT // 2)

def update():
    global state, score

    if state != "playing":
        return

    if keyboard.left:
        player.x -= 4
    if keyboard.right:
        player.x += 4
    if keyboard.up:
        player.y -= 4
    if keyboard.down:
        player.y += 4

    player.x = max(0, min(WIDTH, player.x))
    player.y = max(0, min(HEIGHT, player.y))

    if player.colliderect(plankton):
        score += 1
        plankton.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    if player.colliderect(jellyfish):
        state = "game_over"

    # TODO: replace jellyfish and plankton with lists, and loop through them

def draw():
    screen.fill((20, 80, 160))  # ocean blue

    if state == "start":
        screen.draw.text("Deep Sea Dash", center=(WIDTH // 2, HEIGHT // 2 - 30), fontsize=40, color="white")
        screen.draw.text("Press SPACE to dive in!", center=(WIDTH // 2, HEIGHT // 2 + 30), fontsize=24, color="cyan")

    elif state == "playing":
        player.draw()
        jellyfish.draw()
        plankton.draw()
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=24, color="white")

    elif state == "game_over":
        screen.draw.text("Stung!", center=(WIDTH // 2, HEIGHT // 2 - 30), fontsize=50, color="red")
        screen.draw.text(f"Final Score: {score}", center=(WIDTH // 2, HEIGHT // 2 + 30), fontsize=28, color="yellow")
        screen.draw.text("Press R to try again", center=(WIDTH // 2, HEIGHT // 2 + 80), fontsize=22, color="white")

def on_key_down(key):
    global state
    if state == "start" and key == keys.SPACE:
        reset_game()
        state = "playing"
    elif state == "game_over" and key == keys.R:
        state = "start"

pgzrun.go()
