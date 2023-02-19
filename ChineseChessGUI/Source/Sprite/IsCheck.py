from Const.GuiConst import *
IMAGES_CHECK= [
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/1.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/2.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/3.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/4.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/5.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/6.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/7.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/8.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/9.png"), CHECK_SIZE_IMAGE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/Check/10.png"), CHECK_SIZE_IMAGE)
]


class IsCheck(pygame.sprite.Sprite):
    def __init__(self):
        super(IsCheck, self).__init__()
        self.index = 0
        self.image = IMAGES_CHECK[self.index]
        self.rect = pygame.Rect(BOARD_HEIGHT/4, BOARD_HEIGHT/4, 55,55)
        self.time = 0

    def update(self):
        self.time += 1
        if self.time % 9 == 0 and self.index <= len(IMAGES_CHECK)-1:
            print('index=',self.index)
            self.image = IMAGES_CHECK[self.index]
            self.index += 1


