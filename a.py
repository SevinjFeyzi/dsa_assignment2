import pygame

# Load spritesheets for players
p1spritesheet = pygame.image.load('blue.png')
p2spritesheet = pygame.image.load('pink.png')

p1_sprites = []
p2_sprites = []

player_id = [1, -1]

# Create sprites for both players
for i in range(8):
    curr_sprite = pygame.Rect(32 * i, 0, 32, 32)
    p1_sprites.append(p1spritesheet.subsurface(curr_sprite))
    p2_sprites.append(p2spritesheet.subsurface(curr_sprite))

# Define gem class for animation
class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 0))  # Replace with gem image or color
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 2  # Adjust the velocity as needed

    def update(self):
        self.rect.y += self.velocity

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

gems = pygame.sprite.Group()  # Group to hold gem instances

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill screen with white (background color)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update gems' positions and animate their movement
    for gem in gems:
        gem.update()
        screen.blit(gem.image, gem.rect)

    # Add new gems when needed (for example, when overflow occurs)
    # Replace these conditions with your logic for gem appearance
    if len(gems) < 10:
        new_gem = Gem(32 * len(gems), 0)  # Create a new gem at the top
        gems.add(new_gem)  # Add the gem to the group

   
