import random
from Rip import Rip
from Classes import *
from national_park import main3
from IntervalScreen import interval

class Rock(Obj):
    def __init__(self,x,y,img):
        super().__init__(x,y,img,0.1)
        self.mask=pygame.mask.from_surface(rock)
    def move(self):
        self.y+=1
    def collision(self):
        return collide(self,player)

def draw_game():
    score = calibri.render(f'Score: {player.score}', True, (255, 0, 0))
    target = calibri.render('Target: 30', True, (255, 0, 0))
    wn.blit(cave,(0,0))
    wn.blit(score,(30,30))
    wn.blit(target,(WIDTH-300,30))
    player.draw()
    player.move()
    player.healthbar()
    for rock_ in rocks_list:
        rock_.draw()
        rock_.move()
        if rock_.y>HEIGHT:
            player.score+=1
            rocks_list.remove(rock_)
            rock_obj=Rock(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),rock)
            rocks_list.append(rock_obj)
        if rock_.collision():
            player.health-=10
            hit.play()
            rocks_list.remove(rock_)
            rock_obj = Rock(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), rock)
            rocks_list.append(rock_obj)
    pygame.display.update()

def main2():
    interval('Level 3 : Mines', cave, (450, 250))
    running=True
    global player
    player=Player(300,400,tiger,tiger_scene_2,1)
    global rocks_list
    rocks_list=[]
    while running:
        draw_game()
        pygame_quit()
        if len(rocks_list) < 3:
            for i in range(3):
                rock_obj= Rock(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100),rock)
                rocks_list.append(rock_obj)
        if player.score>30:
            interval('Rocks Stopped Falling',cave, (600, 250))
            main3()
        if player.health<=0:
            Rip()