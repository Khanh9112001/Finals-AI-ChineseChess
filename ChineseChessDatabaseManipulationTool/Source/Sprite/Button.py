# import class
from Const.GuiConst import *

BLACK_PIECES_IMAGES = (
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/bk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/ba.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/bb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/bn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/br.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/bc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/bp.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/deleteBtn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/reset.png"), PIECE_SIZE),
)

CLICKED_BLACK_PIECES_IMAGES = (
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedBk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedBa.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedBb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedBn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedBr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedBc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedBp.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedDeleteBtn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/reset.png"), PIECE_SIZE),
)

RED_PIECES_IMAGES = (
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/rk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/ra.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/rb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/rn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/rr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/rc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/rp.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/saveBtn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/play.png"), PIECE_SIZE),
)

CLLCKED_RED_PIECES_IMAGES = (
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedRk.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedRa.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedRb.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedRn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedRr.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedRc.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedRp.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/clickedSaveBtn.png"), PIECE_SIZE),
    pygame.transform.smoothscale(pygame.image.load(RESOURCE_PATH + "/images/play.png"), PIECE_SIZE),
)


class Button(pygame.sprite.Sprite):
    """
    this class to create piece in computer screen
    """

    def __init__(self, piece_name, position_in_screen: Point, piece_size, leftside, position_in_state=Point()):
        """
        constructor of class
        :param piece_name: chinese chess piece type
        :param position_in_screen: position in computer screen
        :param piece_size: size of piece
        :param leftside: true if left, else : false
        :param position_in_state: index in state of board
        """
        super(Button, self).__init__()
        # position in state
        self.position_in_state = position_in_state

        # name attribute
        self.name = piece_name
        # image of sprite
        if leftside:
            self.images = [BLACK_PIECES_IMAGES[BLACK_PIECES.index(piece_name)],
                           CLICKED_BLACK_PIECES_IMAGES[BLACK_PIECES.index(piece_name)]]
            self.image = self.images[0]
        else:
            self.images = [RED_PIECES_IMAGES[RED_PIECES.index(piece_name)],
                           CLLCKED_RED_PIECES_IMAGES[RED_PIECES.index(piece_name)]]
            self.image = self.images[0]

        # rect of  sprite, it's position of sprite in screen
        self.rect = None

        # set position in screen
        self.set_position_in_screen(position_in_screen, piece_size)

    # set position of sprite in screen
    def set_position_in_screen(self, position_in_screen: Point, piece_size):
        # set position of sprite
        self.rect = pygame.Rect(position_in_screen.get_position(), piece_size)

        # centering image
        self.rect.center = position_in_screen.get_position()

    # function to call each frame
    def update(self):
        pass

    def setClicked(self, isClicked: bool):
        """
        :param isClicked: true if button is clicked
        :return:
        """
        if isClicked:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

    def get_position(self):
        point = Point()
        point.set_position(self.rect.center)
        return point