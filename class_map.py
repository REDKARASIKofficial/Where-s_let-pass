import pygame
import pytmx

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
print(screen.get_size())


class Map:
    def __init__(self, filename, free_tiles, finish_tile):
        self.map = pytmx.load_pygame(f'maps/{filename}')
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles


if __name__ == "__main__":
    map = Map('firstmap.tmx', 0, 0)
    while True:
        screen.fill('black')
        map.render(screen)
        pygame.display.flip()