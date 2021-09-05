from Setup import *

class Obj:
    def __init__(self,x,y,img,vel=0):
        self.x=x
        self.y=y
        self.img=img
        self.vel=vel
    def draw(self):
        wn.blit(self.img,(self.x,self.y))

class Player(Obj):
    def __init__(self,x,y,img1,img2,vel):
        super().__init__(x,y,img1,vel)
        self.img1=img1
        self.img2=img2
        self.health=100
        self.mask=pygame.mask.from_surface(self.img)
        self.score = 0
    def move(self,res_right=WIDTH-200,res_left=0):
        key=pygame.key.get_pressed()
        if key[pygame.K_d] and self.x<res_right or key[pygame.K_RIGHT] and self.x<res_right:
            self.img=self.img1
            self.x+=self.vel
        if key[pygame.K_LEFT] and self.x>res_left or key[pygame.K_a] and self.x>res_left:
            self.img=self.img2
            self.x-=self.vel

    def healthbar(self):
        pygame.draw.rect(wn, (255, 0, 0),(self.x, self.y + self.img.get_height() + 10, self.img.get_width(), 10))
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y + self.img.get_height() + 10, self.img.get_width() * (self.health / 100),10))

class Enemy(Obj):
    def __init__(self,x,y,img1,img2="Null",vel=0):
        super().__init__(x,y,img1,vel)
        self.img1=img1
        self.img2=img2
        self.cooldown=0
    def move(self,pred):
        if pred>self.x:
            self.img=self.img2
            self.x+=self.vel
        if pred<self.x:
            self.img=self.img1
            self.x-=self.vel
class Laser(Obj):
    def __init__(self,x,y,img1,vel):
        super().__init__(x,y,img1,vel)
        self.mask=pygame.mask.from_surface(self.img)
    def move(self):
        self.y+=self.vel
    def collision(self, user):
        return collide(self, user)