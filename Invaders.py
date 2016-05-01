import time
import random
import sys
import pygame
class InvaderClass1(pygame.sprite.Sprite):
    def __init__(self, gs=None,x=0,y=0):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.image_name="Alien1a"
        self.image = pygame.image.load("Alien1a.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center=(self.x,self.y)
        self.prev_direction=-1
        self.direction=1
        self.health = 1
        self.bullet = 0
        # keep original image to limit resize errors
        self.orig_image = self.image
        # if I can fire laser beams, this flag will say
        # whether I should be firing them /right now/
    def reduceHP(self):
        self.health=self.health-1
    def tick(self):
        """if self.bullet == 0:
            shoot = random.randint(0,1000)
            if shoot < 300:
                self.bullet = 1
                laser =  InvaderLaser(self.gs,self)
                self.gs.addILaser(laser)"""
        pass
    def move(self,i,level):
        if self.bullet == 0:
            shoot = random.randint(0,500000)
            if shoot < 30 and self.health>0:
                self.bullet = 1
                laser =  InvaderLaser(self.gs,self)
                self.gs.addILaser(laser)
        if i%30==0:
            if self.image_name=="Alien1a":
                self.image = pygame.image.load("Alien1b.png")
                self.image_name="Alien1b"
            else:
                self.image = pygame.image.load("Alien1a.png")
                self.image_name="Alien1a"
            self.x=self.x+self.direction*level*10
            self.rect.center=(self.x,self.y)
    def advance(self, level):
            self.y=self.y+level*5
            self.rect.center = (self.x,self.y)
    def changeDirection(self):
        self.direction=self.direction*-1

class InvaderLaser:
    def __init__(self,gs = None, invader = None):
        self.gs = gs
        self.invader = invader
        self.damage  = self.invader.health*100
        self.image = pygame.image.load("Missile_Alien.png")
        self.rect = self.image.get_rect()
        self.y = self.invader.y
        self.x = self.invader.x
        self.rect.center = (self.invader.x,self.invader.y)
    def tick(self):
        self.y=self.y+3
        self.rect.center=(self.x,self.y)
    def finish(self):
        self.invader.bullet=0