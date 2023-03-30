import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Dodge the Obstacles")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the character
character_width = 50
character_height = 50
character_x = 175
character_y = 350

# Set up the obstacles
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, 350)
obstacle_y = 0
obstacle_speed = 0.09

# Set up the score
score = 0
font = pygame.font.Font(None, 30)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= 0.09
    if keys[pygame.K_RIGHT] and character_x < 350:
        character_x += 0.09
    
    # Move the obstacles
    obstacle_y += obstacle_speed
    if obstacle_y > 400:
        obstacle_x = random.randint(0, 350)
        obstacle_y = 0
        score += 1
    
    # Check for collision
    if obstacle_y + obstacle_height > character_y and obstacle_y < character_y + character_height and obstacle_x + obstacle_width > character_x and obstacle_x < character_x + character_width:
        running = False
    
    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [character_x, character_y, character_width, character_height])
    pygame.draw.rect(screen, BLACK, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, [10, 10])
    pygame.display.flip()
try:
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # ... rest of the code ...
        
        pygame.time.wait(10)

except Exception as e:
    print(e)
    pygame.quit()

# Clean up
#pygame.quit()
