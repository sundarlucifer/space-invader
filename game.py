import pygame
from pygame import mixer
import random

pygame.init()
fps = pygame.time.Clock()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Space invader')

mixer.music.load('background.wav')
mixer.music.play(-1)

bg = pygame.image.load('space.jpg')
player = pygame.image.load('invaders.png')
bullet = pygame.image.load('bullet.png')

playerX = 400
playerY = 400

bulletX = playerX
bulletY = playerY
status = 'ready'

enemyImg = []
enemyX = []
enemyY = []
enemyDirection = []
enemyCount = 3

for _ in range(enemyCount):
    enemyImg.append(pygame.image.load('transportation.png'))
    enemyX.append(random.randint(30, 720))
    enemyY.append(random.randint(50, 200))

def bullet_fire():
    global status, playerX, playerY, bulletX, bulletY
    if status == 'fire':
        return
    bulletX = playerX + 13
    bulletY = playerY
    status = 'fire'
    bullet_sound = mixer.Sound('laser.wav')
    bullet_sound.play()

def check_and_fire():
    global bulletX, bulletY, status
    if status == 'ready':
        return
    window.blit(bullet, (bulletX, bulletY))
    bulletY-=10
    if bulletY <= 50:
        status = 'ready'

def show_enemies():
    for i in range(enemyCount):
        window.blit(enemyImg[i], (enemyX[i], enemyY[i]))
        

def check_collision():
    global bulletX, bulletY, enemyX, enemyY, enemyCount, status
    for i in range(enemyCount):
        xHit = False
        yHit = False
        if bulletX >= enemyX[i] and bulletX <= enemyX[i]+45:
            xHit = True
        if bulletY >= enemyY[i] and bulletY <= enemyY[i]+30:
            yHit = True
            
        if xHit and yHit:
            enemyImg.pop(i)
            enemyX.pop(i)
            enemyY.pop(i)
            enemyCount -= 1
            status = 'ready'
            explosion_music = mixer.Sound('explosion.wav')
            explosion_music.play()
            return

run = True
while run:
    window.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX += 10
                if playerX>=700:
                    playerX = 700
            elif event.key == pygame.K_LEFT:
                playerX -= 10
                if playerX<=10:
                    playerX = 10
            elif event.key == pygame.K_SPACE:
                bullet_fire()

    window.blit(player, (playerX, playerY))
    show_enemies()
    check_and_fire()
    check_collision()

    pygame.display.update()

    fps.tick(30)
