import pygame, sys, random, pandas as pd
from rock import Rock
from ship import ship

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

pygame.init()

info = pd.read_csv("data.csv")
numlevels = info["level"].min()
level = info["level"].min()
levelInfo = info.iloc[level]
rocks = []
player = ship(20, 250)


def init():
    global rocks, player
    player.x = 20
    player.y = 250
    rocks = []
    levelInfo = info.iloc[level]
    for i in range(levelInfo["numrock"]):
        rocks.append(Rock(random.randint(300, 500), random.randint(200, 300), random.randint(-5, 5), random.randint(-5, 5), random.randint(20, 50)))

init()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit("Thanks for playing!")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.yvelocity -= ship.speed
            if event.key == pygame.K_s:
                player.yvelocity += ship.speed
            if event.key == pygame.K_a:
                player.xvelocity -= ship.speed
            if event.key == pygame.K_d:
                player.xvelocity += ship.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.yvelocity += ship.speed
            if event.key == pygame.K_s:
                player.yvelocity -= ship.speed
            if event.key == pygame.K_a:
                player.xvelocity += ship.speed
            if event.key == pygame.K_d:
                player.xvelocity -= ship.speed
    pygame.draw.polygon(screen, (250, 0, 0),
                        [[player.x - ship.size / 2, player.y + ship.size / 2], [player.x + ship.size / 2, player.y],
                         [player.x - ship.size / 2, player.y - ship.size / 2]], 1)
    player.move()
    for rock in rocks:
        pygame.draw.rect(screen, (91, 229, 227),
                         pygame.Rect(rock.x + (rock.size / 2), rock.y + (rock.size / 2), rock.size, rock.size), 1)
        rock.move()
        rock.bounce()
        if player.y > rock.y and player.y < rock.y + rock.size and player.x > rock.x and player.x < rock.x + rock.size:
            init()
    if player.x > 780:
        level += 1
        if level == 30:
            sys.exit("You win!")
        init()
    pygame.display.flip()
    screen.fill((0, 0, 0))
