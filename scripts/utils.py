import pygame

BASE_IMG_PATH = 'data/images/'
def load_img(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


if __name__ == '__main__':
    print ('"utils" Is the Main')