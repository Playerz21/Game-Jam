from Setup import *
pygame.init()

text=calibri.render('Hunters are coming your way you are the',True,(255,0,0))
text2=calibri.render('only tiger left in this entire world Can you ',True,(255,0,0))
text3=calibri.render('overcome the obstacles and reach safety?',True,(255,0,0))

def render():
    run=True
    while run:
        pygame_quit()
        pos=pygame.mouse.get_pos()
        mouse=pygame.mouse.get_pressed()
        if btn_rect.collidepoint(pos) and any(mouse):
            run=False
        wn.blit(bg, (0, 0))
        wn.blit(btn,(btn_rect.x,btn_rect.y))
        wn.blit(about_holder,(-400,50))
        wn.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2-50))
        wn.blit(text2, (WIDTH / 2 - text2.get_width() / 2, HEIGHT / 2 - text2.get_height() / 2+10))
        wn.blit(text3, (WIDTH / 2 - text3.get_width() / 2, HEIGHT / 2 - text3.get_height() / 2 +60))
        pygame.display.update()