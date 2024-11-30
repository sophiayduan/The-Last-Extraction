# Importing libraries that we'll be using
import pygame

pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_x = int(SCREEN_WIDTH / 2)
player_y = SCREEN_HEIGHT - 100
player_size = 40
player = pygame.Rect(player_x, player_y, player_size, player_size)

front_img = pygame.image.load("images/frontchar.png")
left_img = pygame.image.load("images/leftchar.png")
right_img = pygame.image.load("images/rightchar.png")
back_img = pygame.image.load("images/backchar.png")
front_img = pygame.transform.scale(front_img, (player_size, player_size))
left_img = pygame.transform.scale(left_img, (player_size, player_size))
right_img = pygame.transform.scale(right_img, (player_size, player_size))
back_img = pygame.transform.scale(back_img, (player_size, player_size))

cave_img = pygame.image.load("map/cave.png")
caveore_img = pygame.image.load("map/caveore.png")
path_img = pygame.image.load("map/path.png")
wall_img = pygame.image.load("map/wall.png")
tile_size = player_size + 10

cave_img = pygame.transform.scale(cave_img, (tile_size, tile_size))
caveore_img = pygame.transform.scale(caveore_img, (tile_size, tile_size))
path_img = pygame.transform.scale(path_img, (tile_size, tile_size))
wall_img = pygame.transform.scale(wall_img, (tile_size, tile_size))

fullhp_img = pygame.image.load("images/fullhp.png")
fullhp_img = pygame.transform.scale(fullhp_img, (4*tile_size, 1*tile_size))

player_img = front_img
player_img = pygame.transform.scale(player_img, (player_size, player_size))
game_started = False

grid = [
    [0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 1, 3, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 3, 4, 3, 4, 3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,],
    [0, 0, 0, 3, 4, 4, 4, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 3, 4, 8, 4, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 3, 3, 4, 3, 3, 4, 3, 3, 3, 3, 3, 3, 0, 0, 0,],
    [3, 3, 3, 0, 3, 4, 4, 3, 4, 3, 4, 4, 4, 3, 0, 0, 0, 0,],
    [3, 4, 3, 3, 3, 3, 4, 3, 4, 3, 4, 3, 3, 3, 0, 0, 0, 0,],
    [3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 3, 0, 0, 0, 0,],
    [3, 3, 4, 4, 8, 4, 3, 3, 3, 3, 3, 4, 4, 3, 0, 0, 0, 0,],
    [0, 3, 3, 3, 4, 4, 4, 4, 3, 0, 3, 4, 8, 3, 3, 3, 3, 3,],
    [0, 3, 3, 3, 4, 3, 4, 4, 3, 0, 3, 4, 4, 3, 4, 4, 4, 3,],
    [0, 3, 4, 4, 4, 3, 4, 4, 3, 3, 3, 3, 4, 3, 4, 4, 4, 3,],
    [0, 3, 3, 3, 3, 3, 4, 4, 4, 3, 4, 4, 4, 8, 4, 4, 4, 3,],
    [0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3,],
    [0, 0, 0, 0, 3, 4, 4, 4, 4, 3, 3, 3, 3, 1, 0, 0, 0, 0,],
    [0, 0, 1, 0, 3, 3, 3, 4, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 1,]

]

def draw_grid():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                screen.blit(cave_img, (x * tile_size, y * tile_size))  # White for empty spaces
            elif grid[y][x] == 1:
                screen.blit(caveore_img, (x * tile_size, y * tile_size))
            elif grid[y][x] == 3:
                screen.blit(wall_img, (x * tile_size, y * tile_size))
            elif grid[y][x] == 4:
                screen.blit(path_img, (x * tile_size, y * tile_size))
    screen.blit(fullhp_img, (0, 5))

run = True
while run:
#    for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False

    if game_started == False:
        screen.fill((255, 255, 255))
        key = pygame.key.get_pressed()
        if key[pygame.K_r] == True:
            game_started = True

    else:
        screen.fill((34, 44, 39))
        draw_grid()  # Draw the grid

        if key[pygame.K_a] == True:
            player_img = left_img
            player.move_ip(-2,0)

        elif key[pygame.K_d] == True:
            player_img = right_img
            player.move_ip(2,0)

        elif key[pygame.K_w] == True:
            player_img = back_img
            player.move_ip(0,-2)

        elif key[pygame.K_s] == True:
            player_img = front_img
            player.move_ip(0,2)

        
        screen.blit(player_img, player.topleft)
    
    pygame.display.update()

pygame.quit()