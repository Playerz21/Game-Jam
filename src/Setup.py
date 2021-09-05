'''Imports'''
import pygame
pygame.init()

'''Vars'''
WIDTH=1000
HEIGHT=600
FPS=60
i=0
wn=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Jam Project")

'''Images'''
#Background Images
bg=pygame.image.load('../Assets/background.jpg')
bg=pygame.transform.scale(bg, (WIDTH, HEIGHT))
cave=pygame.image.load('../Assets/cave.jpg')
cave=pygame.transform.scale(cave,(WIDTH,HEIGHT))
rip_bg=pygame.image.load('../Assets/bg.jpg')
rip_bg=pygame.transform.scale(rip_bg, (WIDTH, HEIGHT))
rip=pygame.image.load('../Assets/rip.png')
rip=pygame.transform.scale(rip,(300,300))
na_bg=pygame.transform.scale(pygame.image.load('../Assets/nationalpark.png'), (WIDTH, HEIGHT))

#Player
tiger_scene_2=pygame.image.load('../Assets/tiger.png')
tiger=pygame.transform.flip(pygame.transform.scale(tiger_scene_2,(200,100)),True,False)
tiger_scene_2=pygame.transform.scale(tiger_scene_2,(200,100))
smiling_tiger=pygame.transform.scale(pygame.image.load('../Assets/smiling tiger.png'),(200,200))

#Enemies
helicopter=pygame.image.load('../Assets/enemy.png')
helicopter=pygame.transform.scale(helicopter,(170,120))
helicopter_scene_2=pygame.image.load('../Assets/enemy.png')
helicopter_scene_2=pygame.transform.scale(helicopter,(170,120))
helicopter_scene_2=pygame.transform.flip(helicopter_scene_2,True,False)
hunter=pygame.image.load('../Assets/hunter.png')
hunter=pygame.transform.scale(pygame.transform.flip(hunter,True,False),(100,100))
hunter=pygame.transform.rotate(hunter,20)

#Obj
bullet=pygame.image.load('../Assets/bullet.png')
bullet=pygame.transform.scale(pygame.transform.rotate(bullet,-90),(10,30))
missile=pygame.image.load('../Assets/missile.png')
missile=pygame.transform.scale(missile,(80,80))
rock=pygame.image.load('../Assets/rock.png')
rock=pygame.transform.scale(rock,(80,80))

#Additional Background
badge=pygame.transform.scale(pygame.image.load('../Assets/badge.png'),(300,300))
tower=pygame.image.load('../Assets/tower.png')
tower=pygame.transform.scale(tower,(200,400))

#Btn
btn=pygame.transform.scale(pygame.image.load('../Assets/return.png'),(100,100))
btn_rect=btn.get_rect()
play = pygame.transform.scale(pygame.image.load('../Assets/play.png'), (200, 200))
play_rect = play.get_rect()
about = pygame.transform.scale(pygame.image.load('../Assets/about.png'), (300, 200))
about_rect = about.get_rect()

#TxtHolder
header_img=pygame.transform.scale(pygame.image.load('../Assets/txtholder2.png'),(600,200))
about_holder=pygame.transform.scale(pygame.image.load('../Assets/txtholder3.png'),(2000,650))

'''Text'''
calibri=pygame.font.SysFont('Verdana', 40,bold=True,italic=True)

'''Audio'''
shoot=pygame.mixer.Sound('../Assets/shoot.mp3')
grenade=pygame.mixer.Sound('../Assets/Grenade+1.mp3')
hit=pygame.mixer.Sound('../Assets/hit.wav')

'''Functions'''
def collide(laser,player):
    offset_x=int(player.x-laser.x)
    offset_y=int(player.y-laser.y)
    return laser.mask.overlap(player.mask,(offset_x,offset_y))!=None

def pygame_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()