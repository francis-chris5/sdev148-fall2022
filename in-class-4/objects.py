# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:06:54 2022

@author: c.s.francis
"""

import pygame


class Stuff():
    def __init__(self, x, y, imageFile):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(imageFile)
        
        
    def show(self, display):
        display.blit(self.sprite, (self.x, self.y))
        
        
   
    
   
    
class Character(Stuff):
    def __init__(self, x, y, images, speed, color):
        self.x = x
        self.y = y
        self.images = images
        self.sprite = pygame.image.load(images[0])
        self.speed = speed
        self.bounds = self.sprite.get_rect()
        self.bounds.x = self.x
        self.bounds.y = self.y
        self.color = color
        
        
    def animate(self, frame):
        self.sprite = pygame.image.load(self.images[frame])
        
    def moveHorizontal(self, right=False):
        if right:
            self.x -= self.speed
            self.bounds.x = self.x
        else: 
            self.x += self.speed
            self.bounds.x = self.x
  
        
  
    def moveVertical(self, up=False):
        if up:
            self.y -= self.speed
        else:
            self.y += self.speed
        self.bounds.y = self.y
        
        
    def showBounds(self, display):
        pygame.draw.rect(display, self.color, self.bounds)
        
















    