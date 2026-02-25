import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0
game_over = False

class Player:
    def __init__(self, x, y):
        self.image = "fish"
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40

class Collectible:
    def __init__(self, x, y):
        self.image = "plankton"
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30

class Obstacle:
    def __init__(self, x, y):
        self.image = "jellyfish"
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40

class Shark:
    def __init__(self, x, y):
        self.image = "shark"
        self.x = x
        self.y = y
        self.dx = 2
        self.width = 50
        self.height = 50

player = Player(WIDTH // 2, HEIGHT // 2)
plankton = Collectible(random.randint(0, WIDTH), random.randint(0, HEIGHT))
jellyfish = Obstacle(random.randint(0, WIDTH), random.randint(0, HEIGHT))
shark = Shark(100, 100)

def update():
    global score, game_over
    
    if game_over:
        return
    
    # Move shark back and forth
    shark.x += shark.dx
    if shark.x < 0 or shark.x > WIDTH:
        shark.dx = -shark.dx
    
    # Check collision with plankton
    if (abs(player.x - plankton.x) < 40 and 
        abs(player.y - plankton.y) < 40):
        score += 1
        plankton.x = random.randint(0, WIDTH)
        plankton.y = random.randint(0, HEIGHT)
    
    # Check collision with jellyfish
    if (abs(player.x - jellyfish.x) < 40 and 
        abs(player.y - jellyfish.y) < 40):
        game_over = True
    
    # Check collision with shark
    if (abs(player.x - shark.x) < 50 and 
        abs(player.y - shark.y) < 50):
        game_over = True

def draw():
    screen.clear((100, 150, 200))
    
    screen.blit(player.image, (player.x, player.y))
    screen.blit(shark.image, (shark.x, shark.y))
    screen.blit(plankton.image, (plankton.x, plankton.y))
    screen.blit(jellyfish.image, (jellyfish.x, jellyfish.y))
    
    screen.draw.text(f"Score: {score}", (10, 10), color="white")
    
    if game_over:
        screen.draw.text("GAME OVER", (WIDTH // 2 - 100, HEIGHT // 2), 
                        color="red", fontsize=50)

def on_key_down(key):
    if key == keys.UP:
        player.y -= 10
    elif key == keys.DOWN:
        player.y += 10
    elif key == keys.LEFT:
        player.x -= 10
    elif key == keys.RIGHT:
        player.x += 10
    
    # Wrap around screen
    if player.x < 0:
        player.x = WIDTH
    elif player.x > WIDTH:
        player.x = 0
    if player.y < 0:
        player.y = HEIGHT
    elif player.y > HEIGHT:
        player.y = 0

pgzrun.go()
