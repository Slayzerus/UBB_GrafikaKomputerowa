import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Draw Shapes")

# Define colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Define shapes' dimensions
circle_center = (200, 200)
circle_radius = 150
square_size = 150
square_pos = (200 - square_size // 2, 200 - square_size // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw a black circle
    pygame.draw.circle(screen, BLACK, circle_center, circle_radius)

    # Draw a yellow square inside the circle
    pygame.draw.rect(screen, YELLOW, (*square_pos, square_size, square_size))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
