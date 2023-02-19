from Const.const import *


class FenUtils:

    @staticmethod
    def fen2matrix(fen):
        """
        convert FEN string to state
        :param fen: input FEN
        :return: state
        """
        state = np.array(
            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.'])
        i = 0
        for e in fen:
            if e in NUMSTRING:
                i += int(e)
            elif e in CHESSMAN:
                state[i] = e
                i += 1
        # print(id(state))
        return state.reshape(10, 9)

    @staticmethod
    def matrix2fen(matrix):
        """
        convert state to FEN
        :param matrix: state
        :return: FEN
        """
        fen = ""
        count_row = 0
        for row in matrix:
            i = 0
            count_row += 1
            for e in row:
                if e == '.':
                    i += 1
                elif i != 0:
                    fen += str(i)
                    fen += e
                    i = 0
                else:
                    fen += e
            if i != 0:
                fen += str(i)
            if count_row != 10:
                fen += '/'

        return fen
