import pygame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)
COLORS = [BLACK, RED, GREEN, BLUE]

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extended Paint App")
screen.fill(WHITE)

# Variables
drawing = False
last_pos = None
mode = "pencil"  # Modes: pencil, rect, circle, eraser
color = BLACK
start_pos = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
            
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if mode == "rect":
                rect_width = abs(event.pos[0] - start_pos[0])
                rect_height = abs(event.pos[1] - start_pos[1])
                pygame.draw.rect(screen, color, (min(start_pos[0], event.pos[0]), min(start_pos[1], event.pos[1]), rect_width, rect_height), 2)
            elif mode == "circle":
                radius = int(((event.pos[0] - start_pos[0])**2 + (event.pos[1] - start_pos[1])**2) ** 0.5)
                pygame.draw.circle(screen, color, start_pos, radius, 2)
            
        elif event.type == pygame.MOUSEMOTION and drawing:
            if mode == "pencil":
                pygame.draw.line(screen, color, last_pos, event.pos, 3)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.circle(screen, WHITE, event.pos, 10)
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "pencil"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                color = COLORS[event.key - pygame.K_1]
    
    pygame.display.flip()

pygame.quit()
