import math
import random
import pygame

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load('background.png')

pygame.display.set_caption("Space Invader")
icon =  pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('player.png')
playerx = player_start_x
playery = player_start_y
player_x_change = 0

enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_enemy = 6

for i in range(number_enemy):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min , enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_img = pygame.image.load('bullet.png')
bulletx = 0
bullety = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 64)
textx = 10
texty = 10

font_over = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = font_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(200,250))
    
def player(x,y):
    screen.blit(player_img , (x,y))
    