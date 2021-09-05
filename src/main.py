'''Imports and Inits'''
import Rip
from IntervalScreen import interval
from About import render
from Classes import *
from level2 import main3
pygame.init()

'''Fonts'''
calibri2=pygame.font.SysFont('Calibri', 70, bold=True)


def draw_main_game():
    score = calibri.render(f'Score: {player.score}', True, (0, 0, 0))
    target = calibri.render(f'Target: 20', True, (0, 0, 0))
    wn.blit(bg,(0,0))
    wn.blit(score, (10, 30))
    wn.blit(target, (WIDTH - 300, 30))
    player.draw()
    player.move()
    enemy.draw()
    enemy.move(player.x)
    player.healthbar()
    for bullet in bullets:
        bullet.draw()
        bullet.move()
        if bullet.collision(player):
            grenade.play()
            bullets.remove(bullet)
            player.health-=10
            bullets.append(Laser(enemy.x+20, enemy.y+enemy.img.get_height()/2, missile,1))
        if bullet.y>HEIGHT:
            bullets_no.append(1)
            bullets.remove(bullet)
            bullets.append(Laser(enemy.x+20, enemy.y+enemy.img.get_height()/2, missile,1))
            player.score += 1
    pygame.display.update()

def main1():
    interval('Level 1 : Helicopter', bg,(550, 250))
    run=True
    player_x=WIDTH/2-tiger.get_width()/2
    player_y = 350
    enemy_x=WIDTH+40
    enemy_y=0+40
    global player
    player=Player(player_x,player_y,tiger,tiger_scene_2,1.2)
    global enemy
    enemy=Enemy(enemy_x,enemy_y,helicopter,helicopter_scene_2,0.2)
    global bullets
    bullets=[]
    cooldown=0
    global bullets_no
    bullets_no = []
    while run:
        draw_main_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if player.health==0:
            Rip.Rip()
        if cooldown<1:
            bullets.append(Laser(enemy.x+20, enemy.y+enemy.img.get_height()/2, missile,1))
            cooldown+=1
        if player.score>20:
            interval("What! they retreated", bg,(WIDTH-270, 250))
            main3()
def draw_menu():
    text2 = calibri2.render("Tiger Surivival", True, (255, 0, 255))
    wn.blit(bg, (0, 0))
    wn.blit(header_img,(WIDTH / 2 - header_img.get_width() / 2-30, 50))
    wn.blit(text2, (WIDTH / 2 - text2.get_width() / 2 + 10, 100))
    play_rect.x, play_rect.y = WIDTH / 2 - play.get_width() / 2 + 10, HEIGHT / 2 - play.get_height() / 2+40
    about_rect.x, about_rect.y = WIDTH / 2 - about.get_width() / 2 + 10, HEIGHT / 2 - about.get_height() / 2 + play.get_height()
    wn.blit(play, (play_rect.x, play_rect.y))
    wn.blit(about, (about_rect.x, about_rect.y))
    about_txt=calibri2.render('About', True, (255,255,255))
    wn.blit(about_txt,(about_rect.x+60,about_rect.y+70))
    pygame_quit()
    pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()
    if play_rect.collidepoint(pos) and any(mouse):
        main1()
    if about_rect.collidepoint(pos) and any(mouse):
        render()
    pygame.display.update()


def game():
    game=True
    clock=pygame.time.Clock()
    while game:
        draw_menu()
        clock.tick(FPS)
        pygame_quit()
if __name__=='__main__':
    try:
        game()
    except:
        pass