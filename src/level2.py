import math
from Rip import Rip
from Classes import *
from Level import main2
from IntervalScreen import interval

class Bullet(Obj):
    def __init__(self,x,y,img):
        super().__init__(x,y,img)
        self.i=0
        self.mask=pygame.mask.from_surface(self.img)
        shoot.play()
    def move(self):
        while self.i<1:
            self.angle=math.atan2(player.x+50-self.x,player.y+50-self.y)
            self.vel_x=math.sin(self.angle)*1.5
            self.vel_y=math.cos(self.angle)*1.5
            self.i=i+1
            self.img = pygame.transform.rotate(self.img, self.angle*57.2958)
        self.x+=self.vel_x
        self.y+=self.vel_y
    def collision(self):
        return collide(self,player)

def draw_wn():
    score = calibri.render(f'Score: {player.score}', True, (0, 0, 0))
    target = calibri.render('Target: 10', True, (0, 0, 0))
    wn.blit(bg,(0,0))
    wn.blit(score, (30, 30))
    wn.blit(target, (WIDTH - 300, 30))
    wn.blit(tower,(750,100))
    wn.blit(hunter,(770,100))
    player.draw()
    player.move(500,0)
    player.healthbar()
    for bullet__ in bullets:
        bullet__.draw()
        bullet__.move()
        if bullet__.y>HEIGHT:
            player.score+=1
            bullets.remove(bullet__)
            bullet_=Bullet(850,110,bullet)
            bullets.append(bullet_)
        if bullet__.collision():
            player.health-=10
            bullets.remove(bullet__)
            bullet_ = Bullet(850, 110, bullet)
            bullets.append(bullet_)
    pygame.display.update()

def main3():
    running=True
    global player
    player=Player(100,400,tiger,tiger_scene_2,2.5)
    global bullets
    bullets=[]
    while running:
        draw_wn()
        pygame_quit()
        if len(bullets)==0:
            bullet_ = Bullet(850, 110, bullet)
            bullets.append(bullet_)
        if player.health<=0:
            Rip()
        if player.score>10:
            interval('Hunter Ran Out of Ammo', cave, (680, 250))
            main2()