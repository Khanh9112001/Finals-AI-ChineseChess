PIECE_KING = 0
PIECE_ADVISOR = 1
PIECE_BISHOP = 2
PIECE_KNIGHT = 3
PIECE_ROOK = 4
PIECE_CANNON = 5
PIECE_PAWN = 6
IN_BOARD_ = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
KING_DELTA = [-16, -1, 1, 16]
ADVISOR_DELTA = [-17, -15, 15, 17]
KNIGHT_DELTA = [[-33, -31], [-18, 14], [-14, 18], [31, 33]]
KNIGHT_CHECK_DELTA = [[-33, -18], [-31, -14], [14, 31], [18, 33]]
MVV_VALUE = [50, 10, 10, 30, 40, 30, 20, 0]
PAWN_AWAY_HALF = [-1, 1]


class Checked:
    def __init__(self):
        self.sdPlayer = 0
        self.squares = []
        for sq in range(0, 256):
            self.squares.append(0)

    @staticmethod
    def side_tag(sd):
        return 8 + (sd << 3)

    @staticmethod
    def opp_side_tag(sd):
        return 16 - (sd << 3)

    @staticmethod
    def square_forward(sq, sd):
        return sq - 16 + (sd << 5)

    def checked(self):
        """
        this method check square in checked or not
        :return: boolean
        """
        pc_self_side = Checked.side_tag(self.sdPlayer)
        pc_opp_side = Checked.opp_side_tag(self.sdPlayer)

        for sqSrc in range(256):
            if self.squares[sqSrc] != pc_self_side + PIECE_KING:
                continue
            # check pawn
            if self.squares[Checked.square_forward(sqSrc, self.sdPlayer)] == pc_opp_side + PIECE_PAWN:
                return True

            for i in range(2):
                if self.squares[sqSrc + PAWN_AWAY_HALF[i]] == pc_opp_side + PIECE_PAWN:
                    return True
            # check knight
            for i in range(4):
                if self.squares[sqSrc + ADVISOR_DELTA[i]] != 0:
                    continue

                for j in range(2):
                    pc_dst = self.squares[sqSrc + KNIGHT_CHECK_DELTA[i][j]]
                    if pc_dst == pc_opp_side + PIECE_KNIGHT:
                        return True

            for i in range(4):
                delta = KING_DELTA[i]

                # check rook and king
                sq_dst = sqSrc + delta
                while IN_BOARD_[sq_dst] != 0:
                    pc_dst = self.squares[sq_dst]

                    if pc_dst > 0:
                        if pc_dst == pc_opp_side + PIECE_ROOK or pc_dst == pc_opp_side + PIECE_KING:
                            return True
                        break

                    sq_dst += delta

                # check canon
                sq_dst += delta
                while IN_BOARD_[sq_dst] != 0:
                    pc_dst = self.squares[sq_dst]

                    if pc_dst > 0:
                        if pc_dst == pc_opp_side + PIECE_CANNON:
                            return True
                        break

                    sq_dst += delta

        return False
