import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# State variables — same pattern as the last lesson
state = "start"
score = 0

player = Actor('fish')
player.pos = (WIDTH // 2, HEIGHT // 2)

# A list of plankton to collect
plankton = []
for i in range(5):
    p = Actor('plankton')
    p.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    plankton.append(p)

# A list of jellyfish to avoid
jellyfish = []
for i in range(3):
    j = Actor('jellyfish')
    j.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    jellyfish.append(j)

# A single shark that patrols back and forth
shark = Actor('shark')
shark.pos = (100, 100)
shark.dx = 2

def reset_game():
    global score
    score = 0
    player.pos = (WIDTH // 2, HEIGHT // 2)
    for p in plankton:
        p.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    for j in jellyfish:
        j.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
    shark.pos = (100, 100)

def update():
    global state, score

    if state != "playing":
        return

    # Player movement
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Wrap around screen
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y > HEIGHT:
        player.y = 0
    if player.y < 0:
        player.y = HEIGHT

    # Shark moves back and forth
    shark.x += shark.dx
    if shark.x < 0 or shark.x > WIDTH:
        shark.dx = -shark.dx

    # Jellyfish drift downward
    for j in jellyfish:
        j.y += 1
        if j.y > HEIGHT:
            j.y = 0
            j.x = random.randint(50, WIDTH - 50)

    # Check each plankton for collision
    for p in plankton:
        if player.colliderect(p):
            score += 1
            p.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    # Check each jellyfish for collision
    for j in jellyfish:
        if player.colliderect(j):
            state = "game_over"

    # Check shark
    if player.colliderect(shark):
        state = "game_over"


def draw():
    screen.fill((100, 150, 200))

    if state == "start":
        screen.draw.text("Ocean Explorer", center=(WIDTH // 2, HEIGHT // 2 - 30),
                         fontsize=40, color="white")
        screen.draw.text("Press SPACE to play!", center=(WIDTH // 2, HEIGHT // 2 + 30),
                         fontsize=24, color="cyan")

    elif state == "playing":
        player.draw()
        shark.draw()

        for p in plankton:
            p.draw()

        for j in jellyfish:
            j.draw()

        screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

    elif state == "game_over":
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2 - 30),
                         fontsize=50, color="red")
        screen.draw.text(f"Final Score: {score}", center=(WIDTH // 2, HEIGHT // 2 + 30),
                         fontsize=28, color="yellow")
        screen.draw.text("Press R to try again", center=(WIDTH // 2, HEIGHT // 2 + 80),
                         fontsize=22, color="white")

def on_key_down(key):
    global state
    if state == "start" and key == keys.SPACE:
        reset_game()
        state = "playing"
    elif state == "game_over" and key == keys.R:
        state = "start"

pgzrun.go()
