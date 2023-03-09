import pygame
import random

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the player rectangle and the enemy object
player = pygame.Rect(350, 500, 50, 50)
enemy = pygame.Rect(350, 0, 50, 50)

# Set up the game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Move the player rectangle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]: 
        player.y -= 5 
    if keys[pygame.K_DOWN]: 
        player.y += 5

    # Calculate the distance between the enemy and the player
    distance_x = player.x - enemy.x
    distance_y = player.y - enemy.y
    distance = (distance_x ** 2 + distance_y ** 2) ** 0.5

    # Move the enemy towards the player if the player is close
    speed = 2
    if distance < 300:
        if distance != 0:
            enemy.x += speed * distance_x / distance
            enemy.y += speed * distance_y / distance
    

    # Check for collision between player and enemy
    if player.colliderect(enemy):
        running = False
        

    # Draw the player rectangle and the enemy object on the screen
    pygame.draw.rect(screen, black, player)
    pygame.draw.rect(screen, black, enemy)

    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()
