from Setup import *
pygame.init()

def interval(text,background,size:tuple):
    run=True
    txtholder = pygame.transform.scale(pygame.image.load('../Assets/txtholder.png'), size)
    while run:
        text2=calibri.render(text,False,(0,0,0))
        wn.blit(background,(0,0))
        wn.blit(txtholder,(WIDTH/2-text2.get_width()/2-50,HEIGHT/2-text2.get_height()/2-100))
        wn.blit(text2,(WIDTH/2-text2.get_width()/2,HEIGHT/2-text2.get_height()/2))
        pygame_quit()
        pygame.display.update()
        pygame.time.wait(1000)
        run=False