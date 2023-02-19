# class define point
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_position(self, position):
        self.x = position[0]
        self.y = position[1]

    def get_position(self):
        tuple_result = (self.x, self.y)
        return tuple_result
