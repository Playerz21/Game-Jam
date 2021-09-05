from Setup import *
pygame.init()

def main3():
    run=True
    while run:
        wn.blit(na_bg, (0, 0))
        text=calibri.render("You reached the national park.",True,(0,255,255))
        text2=calibri.render("Wohoo! You are safe from extinction",True,(0,255,255))
        wn.blit(badge,(WIDTH/2-badge.get_width()/2,HEIGHT/2-badge.get_height()/2+100))
        wn.blit(text,(WIDTH/2-text.get_width()/2,100))
        wn.blit(text2,(WIDTH/2-text2.get_width()/2,100+text.get_height()))
        wn.blit(smiling_tiger,(30,300))
        pygame.display.update()
        pygame_quit()