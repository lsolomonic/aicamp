import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Cube")

# Define cube vertices (x, y, z)
vertices = [
    (-50, -50, -50),
    (50, -50, -50),
    (50, 50, -50),
    (-50, 50, -50),
    (-50, -50, 50),
    (50, -50, 50),
    (50, 50, 50),
    (-50, 50, 50)
]

# Define edges of the cube (indices of vertices)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Cube rotation parameters
angle_x = 0
angle_y = 0
angle_z = 0

# Background color transition parameters
target_color = BLACK  # Target color to transition to
current_color = WHITE  # Current background color
transition_speed = 0.5  # Speed of color transition (adjust as needed)

# Function to rotate a point around the x-axis
def rotate_x(point, angle):
    x, y, z = point
    rad = math.radians(angle)
    new_y = y * math.cos(rad) - z * math.sin(rad)
    new_z = y * math.sin(rad) + z * math.cos(rad)
    return x, new_y, new_z

# Function to rotate a point around the y-axis
def rotate_y(point, angle):
    x, y, z = point
    rad = math.radians(angle)
    new_x = x * math.cos(rad) + z * math.sin(rad)
    new_z = -x * math.sin(rad) + z * math.cos(rad)
    return new_x, y, new_z

# Function to rotate a point around the z-axis
def rotate_z(point, angle):
    x, y, z = point
    rad = math.radians(angle)
    new_x = x * math.cos(rad) - y * math.sin(rad)
    new_y = x * math.sin(rad) + y * math.cos(rad)
    return new_x, new_y, z

# Function to transition between colors gradually
def lerp_color(color1, color2, alpha):
    r = int(color1[0] + (color2[0] - color1[0]) * alpha)
    g = int(color1[1] + (color2[1] - color1[1]) * alpha)
    b = int(color1[2] + (color2[2] - color1[2]) * alpha)
    return (r, g, b)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate alpha value for color transition
    alpha = min(1, transition_speed / 100.0)
    
    # Transition background color gradually
    current_color = lerp_color(current_color, target_color, alpha)
    screen.fill(current_color)

    # Calculate rotated vertices
    rotated_vertices = []
    for vertex in vertices:
        rotated = rotate_x(vertex, angle_x)
        rotated = rotate_y(rotated, angle_y)
        rotated = rotate_z(rotated, angle_z)
        rotated_vertices.append(rotated)

    # Project and draw edges
    for edge in edges:
        start = rotated_vertices[edge[0]]
        end = rotated_vertices[edge[1]]
        start_2d = (start[0] + SCREEN_WIDTH // 2, start[1] + SCREEN_HEIGHT // 2)
        end_2d = (end[0] + SCREEN_WIDTH // 2, end[1] + SCREEN_HEIGHT // 2)
        pygame.draw.line(screen, WHITE, start_2d, end_2d)

    # Update rotation angles for animation
    angle_x += 1
    angle_y += 1
    angle_z += 1

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
