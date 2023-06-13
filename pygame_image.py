import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0

    bg_img_flip = pg.transform.flip(bg_img, True, False)

    koukaton_img = pg.image.load("ex01/fig/3.png")
    koukaton_img_flip = pg.transform.flip(koukaton_img, True, False)
    
    koukatons_list = []
    nameraka_max = 70
    for i in range(nameraka_max):
        koukatons_list.append(pg.transform.rotozoom(koukaton_img_flip, 10.0 / nameraka_max * i, 1.0))
    for i in range(nameraka_max, 0, -1):
        koukatons_list.append(pg.transform.rotozoom(koukaton_img_flip, 10.0 / nameraka_max * i, 1.0))
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        bg_width = 3200
        screen.blit(bg_img, [-(tmr % bg_width), 0])
        screen.blit(bg_img_flip, [-(tmr % bg_width) + bg_width / 2, 0])
        screen.blit(bg_img_flip, [-(tmr % bg_width) + bg_width, 0])
        screen.blit(bg_img, [-(tmr % bg_width) + bg_width, 0])
            
        

        
        screen.blit(koukatons_list[tmr % (nameraka_max * 2)], (300, 200))

        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()