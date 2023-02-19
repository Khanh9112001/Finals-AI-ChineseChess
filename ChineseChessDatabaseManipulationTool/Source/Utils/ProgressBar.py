import pygame


class ProgressBar(object):
    def __init__(self, seconds, pos, width, height,
                 inner_colour, border_colour):
        self.maxSeconds = seconds

        self.seconds = seconds
        self.pos = pos
        self.width = width
        self.height = height
        self.finished = False
        self.innerColour = inner_colour
        self.borderColour = border_colour
        self.fullRect = pygame.Rect(pos, (width, height))
        self.rect = pygame.Rect(pos, (width, height))

    def draw(self, surface):
        pygame.draw.rect(surface, self.innerColour, self.rect)

        pygame.draw.rect(surface, self.borderColour, self.fullRect, 2)

        # x, y = self.pos
        # x = x + self.width / 2
        # pos = (x, y)
        # self.text.draw(surface, "%02d" % self.seconds, pos, True)

    def reset(self):
        self.finished = False

        self.seconds = self.maxSeconds

    def update(self, delta_time):
        if self.seconds == 0:
            return

        self.seconds = self.seconds - delta_time
        if self.seconds < 0:
            self.seconds = 0
            self.finished = True

        progress_height = self.height * (self.seconds / self.maxSeconds)

        self.rect = pygame.Rect(self.pos, (self.width, progress_height))
