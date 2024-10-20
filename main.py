import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Load images
SPACESHIP_IMAGE = pygame.image.load("assets/spaceship.png")
ASTEROID_IMAGE = pygame.image.load("assets/asteroid.png")
SATELLITE_IMAGE = pygame.image.load("assets/satellite.png")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up fonts
FONT = pygame.font.SysFont("comicsans", 30)

# Spaceship class
class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 4
        self.laser_cooldown = 0

    def draw(self, window):
        window.blit(SPACESHIP_IMAGE, (self.x, self.y))

    def shoot(self):
        if self.laser_cooldown == 0:
            self.laser_cooldown = 120  # 2 seconds cooldown at 60 FPS
            return True
        return False

    def cooldown(self):
        if self.laser_cooldown > 0:
            self.laser_cooldown -= 1

# Object class
class Object:
    def __init__(self, x, y, obj_type):
        self.x = x
        self.y = y
        self.type = obj_type

    def draw(self, window):
        if self.type == "natural":
            window.blit(ASTEROID_IMAGE, (self.x, self.y))
        elif self.type == "artificial":
            window.blit(SATELLITE_IMAGE, (self.x, self.y))

    def move(self, vel):
        self.x -= vel

# Main game loop
def main():
    run = True
    clock = pygame.time.Clock()
    spaceship = Spaceship(50, HEIGHT // 2)
    objects = []
    score = 0

    def redraw_window():
        WIN.fill(WHITE)
        spaceship.draw(WIN)
        for obj in objects:
            obj.draw(WIN)
        score_text = FONT.render(f"Score: {score}", 1, RED)
        health_text = FONT.render(f"Health: {spaceship.health}", 1, GREEN)
        WIN.blit(score_text, (10, 10))
        WIN.blit(health_text, (10, 40))
        pygame.display.update()

    while run:
        clock.tick(60)
        spaceship.cooldown()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    if spaceship.shoot():
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for obj in objects:
                            if obj.x < mouse_x < obj.x + 50 and obj.y < mouse_y < obj.y + 50:
                                if obj.type == "natural":
                                    score += 20
                                elif obj.type == "artificial":
                                    score -= 100
                                objects.remove(obj)

        if random.randrange(0, 60) == 1:
            obj_type = random.choice(["natural", "artificial"])
            obj_y = random.randrange(50, HEIGHT - 50)
            objects.append(Object(WIDTH, obj_y, obj_type))

        for obj in objects:
            obj.move(5)
            if obj.x < 0:
                objects.remove(obj)
                if obj.type == "natural":
                    spaceship.health -= 1
                if spaceship.health == 0:
                    run = False

        redraw_window()

    pygame.quit()

if __name__ == "__main__":
    main()
