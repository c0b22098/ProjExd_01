import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    tmr = 0

    koukaton_img = pg.image.load("ex01/fig/3.png")
    koukaton_img_flip = pg.transform.flip(koukaton_img, True, False)
    koukaton_img_rotate = pg.transform.rotozoom(koukaton_img_flip, 10, 1.0)
    koukatons_list = [koukaton_img_flip, koukaton_img_rotate]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])

        if tmr % 2 == 0:
            screen.blit(koukatons_list[0], (300, 200))
        else:
            screen.blit(koukatons_list[1], (300, 200))

        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()