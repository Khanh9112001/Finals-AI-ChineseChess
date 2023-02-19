

class MoveUtils:
    @staticmethod
    def src(mv):
        return mv & 255

    @staticmethod
    def dst(mv):
        return mv >> 8

    @staticmethod
    def move_in_state(mv):
        src = MoveUtils.src(mv)
        dst = MoveUtils.dst(mv)
        src_x = int(src / 16) - 3
        src_y = int(src % 16) - 3
        dst_x = int(dst / 16) - 3
        dst_y = int(dst % 16) - 3
        return [(src_x, src_y), (dst_x, dst_y)]