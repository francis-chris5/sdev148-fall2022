# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:52:30 2022

@author: c.s.francis
"""


import pygame
import random



## initialize, start, begin, creation....


pygame.init()
clock = pygame.time.Clock()
pygame.key.set_repeat(10, 10)

score = 0
pygame.font.init()
scoreFont = pygame.font.SysFont("Times New Roman", 23)




windowSize = (960, 480)
scene = pygame.display.set_mode(windowSize)

playerSpeed = 3
playerX = 123
playerY = 123
playerSprite = pygame.image.load("character.png")
playerBounds = playerSprite.get_rect()
playerBounds.x = playerX
playerBounds.y = playerY


backgroundSprite = pygame.image.load("background.png")


coinX = 567
coinY = 234
coinSprite = pygame.image.load("coin.png")
coinBounds = coinSprite.get_rect()
coinBounds.x = coinX
coinBounds.y = coinY
coinSound = pygame.mixer
coinSound.init()
coinSound.music.load("ca_ching.wav")
#@todo add audio to this game --sound effect
# pygame.mixer.init()
# pygame.mixer.music.load("ca_ching.wav")





## main loop, frame update, next...

playing = True
while playing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX -= playerSpeed
            if event.key == pygame.K_w:
                playerY -= playerSpeed
            if event.key == pygame.K_s:
                playerY += playerSpeed
            if event.key == pygame.K_d:
                playerX += playerSpeed
            
           
    if playerBounds.colliderect(coinBounds):
        coinX = random.randint(40, 920)
        coinY = random.randint(40, 440)
        # pygame.mixer.music.play()
        coinSound.music.play()
        score += 1 
    


    scene.blit(backgroundSprite, (0, 0))
    
    #pygame.draw.rect(scene, (87, 145, 78), playerBounds)
    scene.blit(playerSprite, (playerX, playerY))
    playerBounds.x = playerX
    playerBounds.y = playerY
    
    
    #pygame.draw.rect(scene, (187, 185, 78), coinBounds)
    scene.blit(coinSprite, (coinX, coinY))
    coinBounds.x = coinX
    coinBounds.y = coinY
    
    showScore = scoreFont.render("COINS: " + str(score), False, (255, 255, 255))
    scene.blit(showScore, (700, 45))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()





















############## white space for scrolling








