# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:52:30 2022

@author: c.s.francis
"""


import pygame
import random

import objects



## initialize, start, begin, creation....


pygame.init()
clock = pygame.time.Clock()
pygame.key.set_repeat(10, 10)

score = 0
pygame.font.init()
scoreFont = pygame.font.SysFont("Times New Roman", 23)




windowSize = (960, 480)
scene = pygame.display.set_mode(windowSize)

player = objects.Character(123, 123, "character.png", 3, (87, 145, 78))




background = objects.Stuff(0, 0, "background.png")


coinX = 567
coinY = 234
coinSprite = pygame.image.load("coin.png")
coinBounds = coinSprite.get_rect()
coinBounds.x = coinX
coinBounds.y = coinY
coinSound = pygame.mixer
coinSound.init()
coinSound.music.load("ca_ching.wav")






## main loop, frame update, next...

playing = True
while playing:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.moveHorizontal(True)
            if event.key == pygame.K_w:
                player.moveVertical(True)
            if event.key == pygame.K_s:
                player.moveVertical()
            if event.key == pygame.K_d:
                player.moveHorizontal()
            
           
    if player.bounds.colliderect(coinBounds):
        coinX = random.randint(40, 920)
        coinY = random.randint(40, 440)
        coinSound.music.play()
        score += 1 
    


    background.show(scene)
    
    
    
    #player.showBounds(scene)
    player.show(scene)

    
    
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








