import pygame, sys, random, pandas as pd
from rock import rock

screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()

pygame.init()

info = pd.read_csv("data.csv")
numlevels = info["level"].min()
level = info["level"].min()
levelInfo = info.iloc[level]
rocks = []

def init():
    rocks.clear()
    for i in range(levelInfo["numrocks"]):
        rock.append(rock(random.randint(300,500), random.randint(200,300), random.randint(-5,5), random.randint(-5,5), random.randint(10,50)))

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit("Thanks for playing!")
    screen.fill((0,0,0))
    pygame.display.flip()
    for rock in rocks:
        pygame.draw.rect(screen, (200,200,200), pygame.Rect(rock.x + (rock.size/2), rock.y + (rock.size/2), rock.size, rock.size), 0)