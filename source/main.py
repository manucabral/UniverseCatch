"""Main module for the application."""

import pygame as pg

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 600))
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((255, 255, 255))
        pg.display.flip()
    pg.quit()