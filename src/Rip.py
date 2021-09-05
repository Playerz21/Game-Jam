from Setup import *
pygame.init()

text=calibri.render('You Lost',True,(255,255,255))
text2=calibri.render('Your species are extinct',True,(255,255,255))

def Rip():
    run=True
    while run:
        wn.blit(rip_bg, (0, 0))
        wn.blit(rip,(WIDTH/2-rip.get_width()/2,HEIGHT-300))
        wn.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2-text2.get_height()/2-100))
        wn.blit(text2,(WIDTH/2-text2.get_width()/2,HEIGHT/2-text2.get_height()/2+text.get_height()/2-100))
        pygame.display.update()
        pygame_quit()