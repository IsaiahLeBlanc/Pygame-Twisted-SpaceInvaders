import time
import random
import sys
import pygame
import Invaders
import Player
from pygame.locals import *



class GameSpace:
    def main(self):

        # 1) basic initialization
        pygame.init()
        self.font = pygame.font.Font(None, 20)
        self.lfont = pygame.font.Font(None, 60)
        self.size = self.width, self.height = 700, 700
        self.black = 0, 0, 0
        pygame.key.set_repeat(1, 50)
        self.loss=0
        pygame.mixer.init()
        i=0
        self.playerList=[]
        self.LaserList=[]
        self.InvaderList = []
        self.InvaderLaserList=[]
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.player = Player.Player(self)
        self.player2 = Player.Player2(self)
        self.playerList.append(self.player)
        self.playerList.append(self.player2)
        self.level=1
        self.GameOver = self.lfont.render('GAME OVER',0,(255,255,255))
        self.player1wins = self.font.render('Player 1 wins: ',0,(255,255,255))
        self.player2wins = self.font.render('Player 2 Wins',0,(255,255,255))
        self.draw = self.font.render('You are both equally bad',0,(255,255,255))
        self.player1Health = self.font.render('Player 1 Health: ',0,(255,255,255))
        self.player1Score = self.font.render('Player 1 Score: ',0,(255,255,255))
        self.player2Health = self.font.render('Player 2 Health: ',0,(255,255,255))
        self.player2Score = self.font.render('Player 2 Score: ',0,(255,255,255))
        self.player1S = self.font.render(str(self.player.score),0,(255,255,255))
        self.player1HP = self.font.render(str(self.player.health),0,(255,255,255))
        self.player2S = self.font.render(str(self.player2.score),0,(255,255,255))
        self.player2HP = self.font.render(str(self.player2.health),0,(255,255,255))
        self.init_Invaders()
        while 1:
                    # 4) clock tick regulation (framerate)
            if self.check_win():
                self.level=self.level+1
                self.player2.health=self.player2.health+3000
                self.player1.health=self.player1.health+3000
                self.init_Invaders()
            if self.player.health==0 and self.player2.health==0:
                self.loss=1
            if self.loss==1:

                self.screen.fill(self.black)
                self.screen.blit(self.GameOver,(300,350))
                self.screen.blit(self.player1Score,(300,400))
                self.screen.blit(self.player2Score,(300,425))
                self.player1S = self.font.render(str(self.player.score),0,(255,255,255))
                self.player2S = self.font.render(str(self.player2.score),0,(255,255,255))
                self.screen.blit(self.player1S,(400,400))
                self.screen.blit(self.player2S,(400,425))
                if self.player2.score>self.player.score:
                    self.screen.blit(self.player2wins,(400,450))
                elif self.player2.score<self.player.score:
                    self.screen.blit(self.player2wins,(400,450))
                else:
                    self.screen.blit(self.draw,(400,450))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.flip()
                continue
            self.clock.tick(60)
                    # 5) this is where you would handle user inputs...
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    for player in self.playerList:
                        if player.health>0:
                            player.move(pygame.key.get_pressed())
                    #self.player.tick()
            #self.player.tick()
            self.screen.fill(self.black)
            if len(self.LaserList)==0:
                self.player.bullet=0
                self.player2.bullet=0
            self.check_edges()
            for invader in self.InvaderList:
                invader.move(i,self.level)
                if invader.health>0:
                    self.screen.blit(invader.image,invader.rect)
                invader.tick()

            for laser in self.LaserList:
                laser.tick()
                self.screen.blit(laser.image,laser.rect)
                if laser.y<0:
                    self.LaserList.remove(laser)
                    laser.player.bullet=1
                elif self.checkInvaderCollision(laser):
                    self.LaserList.remove(laser)
                    laser.player.bullet=1
            for laser in self.InvaderLaserList:
                laser.tick()
                self.screen.blit(laser.image,laser.rect)
                if laser.y>700:
                    self.InvaderLaserList.remove(laser)
                    laser.finish()
            i=i+1
            self.checkILaserCollison()
            for player in self.playerList:
                if player.health>0:
                    self.screen.blit(player.image, player.rect)
            self.screen.blit(self.player1Health,(0,650))
            self.screen.blit(self.player1Score,(0,665))
            self.screen.blit(self.player2Health,(550,650))
            self.screen.blit(self.player2Score,(550,665))
            self.player1S = self.font.render(str(self.player.score),0,(255,255,255))

            self.player1HP = self.font.render(str(self.player.health),0,(255,255,255))
            self.screen.blit(self.player1HP,(100,650))
            self.screen.blit(self.player1S,(100,665))
            self.player2S = self.font.render(str(self.player2.score),0,(255,255,255))
            self.player2HP = self.font.render(str(self.player2.health),0,(255,255,255))
            self.screen.blit(self.player2HP,(650,650))
            self.screen.blit(self.player2S,(650,665))
            pygame.display.flip()
    def addLaser(self,laser):
        self.LaserList.append(laser)
    def addILaser(self,laser):
        self.InvaderLaserList.append(laser)
    def checkInvaderCollision(self,laser):
        for invader in self.InvaderList:
            if (invader.y+15>=laser.y and laser.y>=invader.y-15) and (invader.x+5>=laser.x and laser.x>=invader.x-5)and invader.health>0:
                invader.reduceHP()
                laser.player.score=laser.player.score+100
                return True
        return False
    def checkILaserCollison(self):
        for laser in self.InvaderLaserList:
            for player in self.playerList:
                if (player.y+15>=laser.y and laser.y>=player.y-15) and (player.x+5>=laser.x and laser.x>=player.x-5)and player.health>0:
                    player.reduceHP()
                    self.InvaderLaserList.remove(laser)
                    laser.finish()
                
    def check_edges(self):

            for invader in self.InvaderList:
                if invader.x >=690 or invader.x <= 9 and invader.health>0:
                    self.changeDirection()
                    for invader in self.InvaderList:
                        invader.move(30,self.level)
                        invader.advance(self.level)
                    return
    def check_loss(self):
        for invader in self.InvaderList:
            if invader.y==600 and invader.health>0:
                self.loss=1
    def check_win(self):
        for invader in self.InvaderList:
            if invader.health>0:
                return False
        return True
    def changeDirection(self):
        for invader in self.InvaderList:
                invader.direction=invader.direction*-1
    def init_Invaders(self):
        x = 10
        y = 200
        self.InvaderList=[]
        for i in range(5):
            for j in range(20):
                self.InvaderList.append(Invaders.InvaderClass1(self,x,y))
                x=x+20
            y=y-20
            x=10
if __name__ == '__main__':
    gs = GameSpace()
    gs.main()