import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
game_over = False

player = Actor('fish')
player.pos = (WIDTH // 2, HEIGHT // 2)

# A list of plankton to collect
plankton = []
for i in range(5):
    p = Actor('plankton')
    p.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    plankton.append(p)

# A list of jellyfish to avoid
jellyfish = []
for i in range(3):
    j = Actor('jellyfish')
    j.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
    jellyfish.append(j)

# A single shark that patrols back and forth
shark = Actor('shark')
shark.pos = (100, 100)
shark.dx = 2


def update():
    global score, game_over

    if game_over:
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

    # Check each plankton for collision
    for p in plankton:
        if player.colliderect(p):
            score += 1
            p.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    # Check each jellyfish for collision
    for j in jellyfish:
        if player.colliderect(j):
            game_over = True

    # Check shark
    if player.colliderect(shark):
        game_over = True


def draw():
    screen.fill((100, 150, 200))

    player.draw()
    shark.draw()

    for p in plankton:
        p.draw()

    for j in jellyfish:
        j.draw()

    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH // 2, HEIGHT // 2),
                         fontsize=50, color="red")


pgzrun.go()
