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

frameCounter = 0
left = False
playing = True

score = 0
pygame.font.init()
scoreFont = pygame.font.SysFont("Times New Roman", 23)




windowSize = (960, 480)
scene = pygame.display.set_mode(windowSize)
playerImages = ["char_walk_0.png", "char_walk_1.png", "char_walk_2.png", "char_walk_3.png"]
player = objects.Character(-70, 123, playerImages, 3, (87, 145, 78))





background1 = objects.Stuff(0, 0, "background.png")
background2 = objects.Stuff(0, 0, "background2.png")


coinX = 567
coinY = 234
coinSprite = pygame.image.load("coin.png")
coinBounds = coinSprite.get_rect()
coinBounds.x = coinX
coinBounds.y = coinY
coinSound = pygame.mixer
coinSound.init()
coinSound.music.load("ca_ching.wav")



### LEVELS
def level1(frameCounter, coinX, coinY):
        
    global score, left, playing
    
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.moveHorizontal(True)
                    left = True
                if event.key == pygame.K_w:
                    player.moveVertical(True)
                if event.key == pygame.K_s:
                    player.moveVertical()
                if event.key == pygame.K_d:
                    player.moveHorizontal()
                    left = False
                
               
        if player.bounds.colliderect(coinBounds):
            coinX = random.randint(40, 920)
            coinY = random.randint(40, 440)
            coinSound.music.play()
            score += 1 
        
    
    
        background1.show(scene)
        
        
        
        #player.showBounds(scene)
        if(frameCounter % 7 == 0):
            player.animate(frameCounter % 4)
            if left:
                player.sprite = pygame.transform.flip(player.sprite, True, False)
        player.show(scene)
    
        
        
        #pygame.draw.rect(scene, (187, 185, 78), coinBounds)
        scene.blit(coinSprite, (coinX, coinY))
        coinBounds.x = coinX
        coinBounds.y = coinY
        
        showScore = scoreFont.render("COINS: " + str(score), False, (25, 25, 25))
        scene.blit(showScore, (700, 45))
        
        if(frameCounter > 700):
            level2(frameCounter, coinX, coinY)
        
        frameCounter += 1
        pygame.display.flip()
        clock.tick(60)



def level2(frameCounter, coinX, coinY):
        
    global score, left, playing
        

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.moveHorizontal(True)
                    left = True
                if event.key == pygame.K_w:
                    player.moveVertical(True)
                if event.key == pygame.K_s:
                    player.moveVertical()
                if event.key == pygame.K_d:
                    player.moveHorizontal()
                    left = False
                
               
        if player.bounds.colliderect(coinBounds):
            coinX = random.randint(40, 920)
            coinY = random.randint(40, 440)
            coinSound.music.play()
            score += 1 
        
    
    
        background2.show(scene)
        
        
        
        #player.showBounds(scene)
        if(frameCounter % 7 == 0):
            player.animate(frameCounter % 4)
            if left:
                player.sprite = pygame.transform.flip(player.sprite, True, False)
        player.show(scene)
    
        
        
        #pygame.draw.rect(scene, (187, 185, 78), coinBounds)
        scene.blit(coinSprite, (coinX, coinY))
        coinBounds.x = coinX
        coinBounds.y = coinY
        
        showScore = scoreFont.render("COINS: " + str(score), False, (25, 25, 25))
        scene.blit(showScore, (700, 45))
            
        
        if frameCounter > 1300:
            scene.fill((134, 134, 134))
            finished()
            
            
        frameCounter += 1
        pygame.display.flip()
        clock.tick(60)



def finished():
    global score, left, playing
    
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            
            
        showScore = scoreFont.render("Congratulations, it looks like you collected " + str(score) + " coins.", False, (47, 152, 47))
        scene.blit(showScore, (250, 220))
                
        pygame.display.flip()
        clock.tick(60)
        
        
def start(frameCounter, coinX, coinY):
    global score, left, playing
    
    while playing:
        scene.fill((134, 134, 134))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            
            
        player.x += 7
        
        if(frameCounter % 7 == 0):
            player.animate(frameCounter % 4)
            if left:
                player.sprite = pygame.transform.flip(player.sprite, True, False)
        player.show(scene)
        
        
        showScore = scoreFont.render("GET READY TO PLAY", False, (47, 152, 47))
        scene.blit(showScore, (250, 220))
                
        if frameCounter > 100:
            level1(frameCounter, coinX, coinY)
            
        frameCounter += 1
        pygame.display.flip()
        clock.tick(60)

## main loop, frame update, next...



if __name__ == "__main__":
    
    start(frameCounter, coinX, coinY)
    
    pygame.quit()





















############## white space for scrolling








