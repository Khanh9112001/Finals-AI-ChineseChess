from Const.GuiConst import *
IMAGES_MATE = [
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/1.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/2.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/3.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/4.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/5.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/6.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/7.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/8.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/9.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/10.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/11.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/12.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/13.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/14.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/15.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/16.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/17.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/18.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Mate/19.png"), CHECK_SIZE_IMAGE)

]


class IsMate(pygame.sprite.Sprite):
    def __init__(self):
        super(IsMate, self).__init__()
        self.index = 0
        self.image = IMAGES_MATE[self.index]
        self.rect = pygame.Rect(BOARD_HEIGHT/4, BOARD_HEIGHT/4, 55,55)
        self.time = 0

    def update(self):
        self.time += 1
        if self.time % 9 == 0 and self.index <= len(IMAGES_MATE)-1:
            print('index=',self.index)
            self.image = IMAGES_MATE[self.index]
            self.index += 1


