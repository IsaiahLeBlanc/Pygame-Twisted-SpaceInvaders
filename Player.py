import time
import random
import sys
import pygame
from pygame.locals import *
class Player(pygame.sprite.Sprite):
    def __init__(self, gs=None):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center=(350,600)
        self.x = 350
        self.y = 600
        self.health = 9000
        self.score = 0
        self.bullet = 0
        # keep original image to limit resize errors
        self.orig_image = self.image
        # if I can fire laser beams, this flag will say
        # whether I should be firing them /right now
    def tick(self):
        #self.image = pygame.transform.rotate(self.orig_image,10) # Rotate the image 
        # get the mouse x and y position on the screen  
        pass
    def move(self, keycode):
        if keycode[K_LEFT]:
            if self.x>20:
                self.rect = self.rect.move(-5,0)
                self.x=self.x-5
        if keycode[K_RIGHT]:
            if self.x < 680:
                self.rect = self.rect.move(5,0)
                self.x=self.x+5
        if keycode[K_UP]:
            if self.y>550:
                self.rect = self.rect.move(0,-5)
                self.y=self.y-5
        if keycode[K_DOWN]:
            if self.y < 600:
                self.rect = self.rect.move(0,5)
                self.y=self.y+5
        if keycode[K_SPACE]:
            if self.bullet==0:
                self.bullet = 1
                laser =  PlayerLaser(self.gs,self)
                self.gs.addLaser(laser)
    def reduceHP(self):
        self.health=self.health-3000
    def fire(self):
        pass
class Player2(pygame.sprite.Sprite):
    def __init__(self, gs=None):
        pygame.sprite.Sprite.__init__(self)
        self.gs = gs
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center=(400,600)
        self.x = 400
        self.y = 600
        self.health = 9000
        self.score = 0
        self.bullet = 0
        # keep original image to limit resize errors
        self.orig_image = self.image
        # if I can fire laser beams, this flag will say
        # whether I should be firing them /right now
    def tick(self):
        #self.image = pygame.transform.rotate(self.orig_image,10) # Rotate the image 
        # get the mouse x and y position on the screen  
        pass
    def move(self, keycode):
        if keycode[K_a]:
            if self.x>20:
                self.rect = self.rect.move(-5,0)
                self.x=self.x-5
        if keycode[K_d]:
            if self.x < 680:
                self.rect = self.rect.move(5,0)
                self.x=self.x+5
        if keycode[K_w]:
            if self.y>550:
                self.rect = self.rect.move(0,-5)
                self.y=self.y-5
        if keycode[K_x]:
            if self.y < 600:
                self.rect = self.rect.move(0,5)
                self.y=self.y+5
        if keycode[K_q]:
            if self.bullet==0:
                self.bullet = 1
                laser =  PlayerLaser(self.gs,self)
                self.gs.addLaser(laser)
    def reduceHP(self):
        self.health=self.health-3000
    def fire(self):
        pass
class PlayerLaser(pygame.sprite.Sprite):
    def __init__(self, gs = None, player=None):
        pygame.sprite.Sprite.__init__(self)
        self.gs =gs
        self.image = pygame.image.load("Missile_Player.png")
        mx, my = pygame.mouse.get_pos()
        self.rect = self.image.get_rect()
        self.player=player
        self.rect.center=player.rect.center
        self.x,self.y = self.rect.center
    def tick(self):
        self.y=self.y-5
        self.rect.center=(self.x,self.y)
#       print "Sin of angle %f is %f" % (math.degrees(self.angle),x)
#       print "Sin of pi/2 is %f" % (math.sin(math.pi/2))