import pygame
from Button_class import Button
from main_functions import terminate
from main_functions import load_image

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
all_sprites = pygame.sprite.Group()


def dead(screen, current_level):
    pygame.mouse.set_visible(True)
    color = pygame.Color('black')
    color.hsva = (100, 0, 100, 100)
    image = pygame.Surface((screen.get_width(), screen.get_height()))
    image.set_alpha(150)
    pygame.draw.rect(image, color, (0, 0, screen.get_width(), screen.get_width()))
    screen.blit(image, (0, 0))
    exit = Button('Выйти из игры', 0, 0, all_sprites)
    continuing = Button('Начать игру заново', 0, 0, all_sprites)
    exit.rect.x = screen.get_width() // 2 - exit.rect.w // 2
    exit.rect.y = screen.get_height() // 2 + exit.rect.h // 2 + 50
    continuing.rect.x = screen.get_width() // 2 - continuing.rect.w // 2
    continuing.rect.y = screen.get_height() // 2 - continuing.rect.h - 40
    menu = Button('Вернуться в меню', 0, 0, all_sprites)
    menu.rect.x = screen.get_width() // 2 - menu.rect.w // 2
    menu.rect.y = screen.get_height() // 2 - continuing.rect.h + 55
    while True:
        for event in pygame.event.get():
            all_sprites.update(event)
            if exit.click(event):
                terminate()
            if continuing.click(event):
                pygame.mouse.set_visible(False)
                pygame.mixer.stop()
                return current_level
            if menu.click(event):
                pygame.mouse.set_visible(False)
                pygame.mixer.stop()
                return 'start_screen'
        all_sprites.draw(screen)
        screen.blit(pygame.transform.scale(load_image('Game_over.png'), (600, 600)),
                    (screen.get_width() / 2 - 300, -100))
        pygame.display.flip()
