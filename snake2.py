import pygame, time
pygame.init()

screen_width = 1000
screen_height = 720
snake_width = 20
snake_length = 20

# Starting coordinates of the snake.
snake_x = round((screen_width - snake_width) / 2)
snake_y = round((screen_height - snake_width) / 2)

# Initializing the display screen.
screen = pygame.display.set_mode((screen_width,screen_height), pygame.RESIZABLE)  # Size of game display screen.

# Customizing the game icon.
game_icon = pygame.image.load('snek.png')
pygame.display.set_icon(game_icon)

# Customising the screen title. 
screen_title = "Snake Game"
pygame.display.set_caption(screen_title)

# Initializing color variables.
green = (188, 227, 199)
red = (255, 0, 51)
blue = (43, 0, 255)
black = (6, 0, 15)
white = (247, 252, 255)

'''
display_duration = 5  # The duration of how long the screen will display for.
time.sleep(display_duration)
'''

# Ensure the game continues running until "quit".
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    
    pygame.draw.rect(screen, red, [snake_x, snake_y, snake_length, snake_width])
    pygame.display.update()
pygame.quit()
quit()



