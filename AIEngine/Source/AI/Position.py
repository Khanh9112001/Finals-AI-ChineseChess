import randomfrom Const.Const import *from Database.Book import BOOK_DATfrom Database.RC4 import RC4from Utils.SearchUtils import SearchUtilsclass Position:    def __init__(self):        self.squares = \            [                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,            ]        self.black_value = 0        self.red_value = 0        self.sd_player = LOWER_SIDE        self.piece_list = []        self.depth = 0        self.depthByQuiesc = 0        self.allNode = 0        # RC4 algorithm        self.zobristLock = 0        self.zobristKey = 0        self.PreGen_zobristKeyTable = []        self.PreGen_zobristLockTable = []        self.PreGen_zobristLockPlayer = 0        self.PreGen_zobristKeyPlayer = 0        self.init_zobrist()    def init_value(self):        for i in range(256):            pc = self.squares[i]            if pc == 0:                continue            if pc >= 16:                pc_adjust = pc - 16                self.black_value += PIECE_VALUE[pc_adjust][self.square_flip(i)]            else:                pc_adjust = pc - 8                self.red_value += PIECE_VALUE[pc_adjust][i]    def init_zobrist(self):        rc4 = RC4()        self.PreGen_zobristKeyPlayer = rc4.nextLong()        rc4.nextLong()        self.PreGen_zobristLockPlayer = rc4.nextLong()        for i in range(0, 14):            keys = []            locks = []            for j in range(0, 256):                keys.append(rc4.nextLong())                rc4.nextLong()                locks.append(rc4.nextLong())            self.PreGen_zobristKeyTable.append(keys)            self.PreGen_zobristLockTable.append(locks)    @staticmethod    def char_to_piece(c):        if c == "K":            return PIECE_KING        elif c == "A":            return PIECE_ADVISOR        elif c == "B" or c == "E":            return PIECE_BISHOP        elif c == "H" or c == "N":            return PIECE_KNIGHT        elif c == "R":            return PIECE_ROOK        elif c == "C":            return PIECE_CANNON        elif c == "P":            return PIECE_PAWN        return -1    @staticmethod    def coord_xy(x, y):        """        ------>x        |        |        y        from x, y => index of square        :param x:        :param y:        :return:        """        return x + (y << 4)    def to_fen(self):        fen = ''        for y in range(RANK_TOP, RANK_BOTTOM + 1):            k = 0            for x in range(FILE_LEFT, FILE_RIGHT + 1):                pc = self.squares[Position.coord_xy(x, y)]                if pc > 0:                    if k > 0:                        fen += str(k)                        k = 0                    fen += FEN_PIECE[pc]                else:                    k += 1            if k > 0:                fen += str(k)            fen += '/'        return fen[0:len(fen) - 1]    def fromFen(self, fen):        y = RANK_TOP        x = FILE_LEFT        index = 0        c = fen[index]        while c != ' ':            if c == '/':                x = FILE_LEFT                y += 1                if y > RANK_BOTTOM:                    break            elif c in NUMSTRING:                for i in range(0, int(c)):                    if x >= FILE_RIGHT:                        break                    x += 1            elif c in CHESSMAN1:  # chu hoa                if x <= FILE_RIGHT:                    pt = self.char_to_piece(c)                    if pt >= 0:                        self.add_piece(self.coord_xy(x, y), pt + 8)                    x += 1            elif c in CHESSMAN2:  # chu thuong                if x <= FILE_RIGHT:                    pt = self.char_to_piece(c.upper())                    if pt >= 0:                        self.add_piece(self.coord_xy(x, y), pt + 16)                    x += 1            index += 1            c = fen[index]        index += 1        if index == len(fen):            return        if fen[index] == 'b' and self.sd_player == 0:            self.change_side()        elif fen[index] == 'w' and self.sd_player == 1:            self.change_side()    @staticmethod    def in_board(sq):        return IN_BOARD[sq] != 0    @staticmethod    def in_port(sq):        return IN_FORT[sq] != 0    @staticmethod    def square_flip(sq):        return 254 - sq    @staticmethod    def square_forward(sq, sd):        return sq - 16 + (sd << 5)    @staticmethod    def home_half(sq, sd):        return (sq & 0x80) != (sd << 7)    @staticmethod    def away_half(sq, sd):        return (sq & 0x80) == (sd << 7)    @staticmethod    def side_tag(sd):        return 8 + (sd << 3)    @staticmethod    def opp_side_tag(sd):        return 16 - (sd << 3)    @staticmethod    def src(mv):        return mv & 255    @staticmethod    def dst(mv):        return mv >> 8    @staticmethod    def move(square_source, dest_source):        """        this method calculate move        :param square_source: square source        :param dest_source: dest source        :return:        """        return square_source + (dest_source << 8)    def change_side(self):        """        this method change side's turn        :return:        """        self.sd_player = 1 - self.sd_player        self.zobristLock ^= self.PreGen_zobristLockPlayer        self.zobristKey ^= self.PreGen_zobristKeyPlayer    def evaluate_board(self):        """        this method evaluate board        :return: a number        """        if self.sd_player == 1:            return self.black_value - self.red_value        else:            return self.red_value - self.black_value    def checked(self):        """        this method check square in checked or not        :return: boolean        """        pc_self_side = Position.side_tag(self.sd_player)        pc_opp_side = Position.opp_side_tag(self.sd_player)        for sqSrc in range(256):            if self.squares[sqSrc] != pc_self_side + PIECE_KING:                continue            # check pawn            if self.squares[Position.square_forward(sqSrc, self.sd_player)] == pc_opp_side + PIECE_PAWN:                return True            for i in range(2):                if self.squares[sqSrc + PAWN_AWAY_HALF[i]] == pc_opp_side + PIECE_PAWN:                    return True            # check knight            for i in range(4):                if self.squares[sqSrc + ADVISOR_DELTA[i]] != 0:                    continue                for j in range(2):                    pc_dst = self.squares[sqSrc + KNIGHT_CHECK_DELTA[i][j]]                    if pc_dst == pc_opp_side + PIECE_KNIGHT:                        return True            for i in range(4):                delta = KING_DELTA[i]                # check rook and king                sq_dst = sqSrc + delta                while IN_BOARD[sq_dst]:                    pc_dst = self.squares[sq_dst]                    if pc_dst > 0:                        if pc_dst == pc_opp_side + PIECE_ROOK or pc_dst == pc_opp_side + PIECE_KING:                            return True                        break                    sq_dst += delta                # check canon                sq_dst += delta                while IN_BOARD[sq_dst]:                    pc_dst = self.squares[sq_dst]                    if pc_dst > 0:                        if pc_dst == pc_opp_side + PIECE_CANNON:                            return True                        break                    sq_dst += delta        return False    def generate_moves(self):        """        this method generate moves        :return: list of move        """        moves = []        piece_self_side = Position.side_tag(self.sd_player)        piece_opp_side = Position.opp_side_tag(self.sd_player)        for sq_source in range(len(self.squares)):            piece_src = self.squares[sq_source]            if piece_src & piece_self_side == 0:                continue            switch = piece_src - piece_self_side            if switch == PIECE_KING:                for i in range(4):                    sq_dst = sq_source + KING_DELTA[i]                    if not Position.in_port(sq_dst):                        continue                    piece_dest = self.squares[sq_dst]                    if piece_dest == 0:                        moves.append([Position.move(sq_source, sq_dst), 0])                    elif piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                sq_dst = Position.square_forward(sq_source, self.sd_player)                king_opp = Position.opp_side_tag(self.sd_player)                while Position.in_board(sq_dst):                    piece_dest = self.squares[sq_dst]                    if piece_dest > 0:                        if piece_dest == king_opp:                            moves.append(                                [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                        break                    sq_dst = Position.square_forward(sq_dst, self.sd_player)            elif switch == PIECE_ADVISOR:                for i in range(4):                    sq_dst = sq_source + ADVISOR_DELTA[i]                    if not Position.in_port(sq_dst):                        continue                    piece_dest = self.squares[sq_dst]                    if piece_dest == 0:                        moves.append([Position.move(sq_source, sq_dst), 0])                    elif piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])            elif switch == PIECE_BISHOP:                for i in range(4):                    sq_dst = sq_source + ADVISOR_DELTA[i]                    if not (Position.in_board(sq_dst) and Position.home_half(sq_dst, self.sd_player) and self.squares[                        sq_dst] == 0):                        continue                    sq_dst += ADVISOR_DELTA[i]                    piece_dest = self.squares[sq_dst]                    if piece_dest == 0:                        moves.append([Position.move(sq_source, sq_dst), 0])                    elif piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])            elif switch == PIECE_KNIGHT:                for i in range(4):                    sq_dst = sq_source + KING_DELTA[i]                    if self.squares[sq_dst] > 0:                        continue                    for j in range(2):                        sq_dst = sq_source + KNIGHT_DELTA[i][j]                        if not Position.in_board(sq_dst):                            continue                        piece_dest = self.squares[sq_dst]                        if piece_dest == 0:                            moves.append([Position.move(sq_source, sq_dst), 0])                        elif piece_dest & piece_opp_side != 0:                            moves.append(                                [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])            elif switch == PIECE_ROOK:                for i in range(4):                    delta = KING_DELTA[i]                    sq_dst = sq_source + delta                    while Position.in_board(sq_dst):                        piece_dest = self.squares[sq_dst]                        if piece_dest == 0:                            moves.append([Position.move(sq_source, sq_dst), 0])                        else:                            if piece_dest & piece_opp_side != 0:                                moves.append([Position.move(sq_source, sq_dst),                                              PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                            break                        sq_dst += delta            elif switch == PIECE_CANNON:                for i in range(4):                    delta = KING_DELTA[i]                    sq_dst = sq_source + delta                    while Position.in_board(sq_dst):                        piece_dest = self.squares[sq_dst]                        if piece_dest == 0:                            moves.append([Position.move(sq_source, sq_dst), 0])                        else:                            break                        sq_dst += delta                    sq_dst += delta                    while Position.in_board(sq_dst):                        piece_dest = self.squares[sq_dst]                        if piece_dest > 0:                            if piece_dest & piece_opp_side != 0:                                moves.append([Position.move(sq_source, sq_dst),                                              PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                            break                        sq_dst += delta            elif switch == PIECE_PAWN:                sq_dst = Position.square_forward(sq_source, self.sd_player)                if Position.in_board(sq_dst):                    piece_dest = self.squares[sq_dst]                    if piece_dest == 0:                        moves.append([Position.move(sq_source, sq_dst), 0])                    elif piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                if Position.away_half(sq_source, self.sd_player):                    for i in range(2):                        sq_dst = sq_source + PAWN_AWAY_HALF[i]                        if Position.in_board(sq_dst):                            piece_dest = self.squares[sq_dst]                            if piece_dest == 0:                                moves.append([Position.move(sq_source, sq_dst), 0])                            elif piece_dest & piece_opp_side != 0:                                moves.append([Position.move(sq_source, sq_dst),                                              PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])        return moves    def generate_capture_moves(self):        """        this method generate capture moves        :return: list of move        """        moves = []        piece_self_side = Position.side_tag(self.sd_player)        piece_opp_side = Position.opp_side_tag(self.sd_player)        for sq_source in range(len(self.squares)):            piece_src = self.squares[sq_source]            if piece_src & piece_self_side == 0:                continue            switch = piece_src - piece_self_side            if switch == PIECE_KING:                for i in range(4):                    sq_dst = sq_source + KING_DELTA[i]                    if not Position.in_port(sq_dst):                        continue                    piece_dest = self.squares[sq_dst]                    if piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                sq_dst = Position.square_forward(sq_source, self.sd_player)                king_opp = Position.opp_side_tag(self.sd_player)                while Position.in_board(sq_dst):                    piece_dest = self.squares[sq_dst]                    if piece_dest > 0:                        if piece_dest == king_opp:                            moves.append(                                [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                        break                    sq_dst = Position.square_forward(sq_dst, self.sd_player)            elif switch == PIECE_ADVISOR:                for i in range(4):                    sq_dst = sq_source + ADVISOR_DELTA[i]                    if not Position.in_port(sq_dst):                        continue                    piece_dest = self.squares[sq_dst]                    if piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])            elif switch == PIECE_BISHOP:                for i in range(4):                    sq_dst = sq_source + ADVISOR_DELTA[i]                    if not (Position.in_board(sq_dst) and Position.home_half(sq_dst, self.sd_player) and self.squares[                        sq_dst] == 0):                        continue                    sq_dst += ADVISOR_DELTA[i]                    piece_dest = self.squares[sq_dst]                    if piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])            elif switch == PIECE_KNIGHT:                for i in range(4):                    sq_dst = sq_source + KING_DELTA[i]                    if self.squares[sq_dst] > 0:                        continue                    for j in range(2):                        sq_dst = sq_source + KNIGHT_DELTA[i][j]                        if not Position.in_board(sq_dst):                            continue                        piece_dest = self.squares[sq_dst]                        if piece_dest & piece_opp_side != 0:                            moves.append(                                [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])            elif switch == PIECE_ROOK:                for i in range(4):                    delta = KING_DELTA[i]                    sq_dst = sq_source + delta                    while Position.in_board(sq_dst):                        piece_dest = self.squares[sq_dst]                        if piece_dest != 0:                            if piece_dest & piece_opp_side != 0:                                moves.append([Position.move(sq_source, sq_dst),                                              PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                            break                        sq_dst += delta            elif switch == PIECE_CANNON:                for i in range(4):                    delta = KING_DELTA[i]                    sq_dst = sq_source + delta                    while Position.in_board(sq_dst):                        piece_dest = self.squares[sq_dst]                        if piece_dest != 0:                            break                        sq_dst += delta                    sq_dst += delta                    while Position.in_board(sq_dst):                        piece_dest = self.squares[sq_dst]                        if piece_dest > 0:                            if piece_dest & piece_opp_side != 0:                                moves.append([Position.move(sq_source, sq_dst),                                              PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                            break                        sq_dst += delta            elif switch == PIECE_PAWN:                sq_dst = Position.square_forward(sq_source, self.sd_player)                if Position.in_board(sq_dst):                    piece_dest = self.squares[sq_dst]                    if piece_dest & piece_opp_side != 0:                        moves.append(                            [Position.move(sq_source, sq_dst), PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])                if Position.away_half(sq_source, self.sd_player):                    for i in range(2):                        sq_dst = sq_source + PAWN_AWAY_HALF[i]                        if Position.in_board(sq_dst):                            piece_dest = self.squares[sq_dst]                            if piece_dest & piece_opp_side != 0:                                moves.append([Position.move(sq_source, sq_dst),                                              PIECE_VALUE[piece_dest - piece_opp_side][sq_dst]])        return moves    def make_move(self, move):        self.move_piece(move)        if self.checked():            self.allNode -= 1            self.undo_move_piece(move)            return False        self.change_side()        return True    def undo_make_move(self, move):        self.undo_move_piece(move)        self.change_side()    def undo_move_piece(self, move):        sq_src = self.src(move)        pc_src = self.squares[sq_src]        sq_dst = self.dst(move)        pc_dst = self.squares[sq_dst]        self.remove_piece(sq_dst, pc_dst)        self.add_piece(sq_src, pc_dst)        self.depth -= 1        if self.piece_list:            pc = self.piece_list.pop()            if pc > 0:                self.add_piece(sq_dst, pc)    def move_piece(self, move):        """        this method move piece from square source to dest source        :param move:        :return:        """        self.depth += 1        if self.depthByQuiesc < self.depth:            self.depthByQuiesc = self.depth        self.allNode += 1        sq_src = self.src(move)        pc_src = self.squares[sq_src]        sq_dst = self.dst(move)        pc_dst = self.squares[sq_dst]        self.piece_list.append(pc_dst)        if pc_dst > 0:            self.remove_piece(sq_dst, pc_dst)        self.remove_piece(sq_src, pc_src)        self.add_piece(sq_dst, pc_src)    def add_piece(self, sq, pc):        """        this method add piece in board        :param sq: square        :param pc: piece        :return:        """        self.squares[sq] = pc        if pc < 16:            pc_adjust = pc - 8            self.red_value += PIECE_VALUE[pc_adjust][sq]        else:            pc_adjust = pc - 16            self.black_value += PIECE_VALUE[pc_adjust][self.square_flip(sq)]            pc_adjust += 7        self.zobristLock ^= self.PreGen_zobristLockTable[pc_adjust][sq]        self.zobristKey ^= self.PreGen_zobristKeyTable[pc_adjust][sq]    def remove_piece(self, sq, pc):        """        this method remove a piece in board        :param sq:  square        :param pc: piece        :return:        """        self.squares[sq] = 0        if pc < 16:            pc_adjust = pc - 8            self.red_value -= PIECE_VALUE[pc_adjust][sq]        else:            pc_adjust = pc - 16            self.black_value -= PIECE_VALUE[pc_adjust][self.square_flip(sq)]            pc_adjust += 7        self.zobristLock ^= self.PreGen_zobristLockTable[pc_adjust][sq]        self.zobristKey ^= self.PreGen_zobristKeyTable[pc_adjust][sq]    def mirror(self):        pos = Position()        for sq in range(0, 256):            pc = self.squares[sq]            if pc > 0:                pos.add_piece(self.mirror_square(sq), pc)        if self.sd_player == 1:            pos.change_side()        return pos.zobristLock    def flip_square_move(self):        pos = Position()        pos.fromFen(Position.change_uper_lower_fen(self.to_fen()[::-1])+' b')        return pos.zobristLock    def flip_mirror_square_move(self):        pos = Position()        pos.fromFen(Position.change_uper_lower_fen(self.to_fen()[::-1])+' b')        return pos.mirror()    @staticmethod    def change_uper_lower_fen(fen):        s = ''        for i in fen:            if i.islower():                s += fen[fen.index(i)].upper()            elif i.isupper():                s += fen[fen.index(i)].lower()            else:                s += fen[fen.index(i)]        return s    @staticmethod    def mirror_square(sq):        return Position.coord_xy(Position.file_flip(Position.file_x(sq)), Position.rank_y(sq))    @staticmethod    def file_flip(x):        """        --->x        |        |        y        flip x to other side        :param x:        :return:        """        return 14 - x    @staticmethod    def rank_y(sq):  # vi tri hang        """        ----->x        |        |        y        index => y        :param sq:        :return:        """        return sq >> 4    @staticmethod    def file_x(sq):  # vi tri cot        """        ----->x        |        |        y        index => x        :param sq:        :return:        """        return sq & 15    def bookMove(self):        if len(BOOK_DAT) == 0:            return 0        mirror = False        flip = False        flip_mirror = False        lock = self.zobristLock >> 1  # Convert into Unsigned        index = SearchUtils.binary_search(BOOK_DAT, lock)        if index < 0:            lock = self.mirror() >> 1  # Convert into Unsigned            index = SearchUtils.binary_search(BOOK_DAT, lock)            if index > 0:                mirror = True        if index < 0:            lock = self.flip_square_move() >> 1  # Convert into Unsigned            index = SearchUtils.binary_search(BOOK_DAT, lock)            if index > 0:                flip = True        if index<0:            lock = self.flip_mirror_square_move() >> 1  # Convert into Unsigned            index = SearchUtils.binary_search(BOOK_DAT, lock)            if index > 0:                flip_mirror = True        if index < 0:            return 0        # first index in block        index -= 1        while index >= 0 and BOOK_DAT[index][0] == lock:            index -= 1        mvs = []        vls = []        value = 0        index += 1        # append all element into mvs, vls        while index < len(BOOK_DAT) and BOOK_DAT[index][0] == lock:            mv = BOOK_DAT[index][1]            if mirror:                mv = self.mirror_move(mv)            elif flip:                mv = self.flip_move(mv)            elif flip_mirror:                mv = self.flip_mirror_move(mv)            # if (this.legalMove(mv)):            mvs.append(mv)            vl = BOOK_DAT[index][2]            vls.append(vl)            value += vl            index += 1        if value == 0:            return 0        # choose random move        value = random.random() * value        for index in range(0, len(mvs)):            value -= vls[index]            if value < 0:                break        return mvs[index]    @staticmethod    def mirror_move(mv):        return Position.move(Position.mirror_square(Position.src(mv)), Position.mirror_square(Position.dst(mv)))    @staticmethod    def flip_rank(y):        return 15 - y    @staticmethod    def flip_square(sq):        return Position.coord_xy(Position.file_flip(Position.file_x(sq)), Position.flip_rank(Position.rank_y(sq)))    @staticmethod    def flip_move(mv):        return Position.move(Position.flip_square(Position.src(mv)), Position.flip_square(Position.dst(mv)))    @staticmethod    def flip_mirror_move(mv):        return Position.move(Position.mirror_square(Position.flip_square(Position.src(mv))), Position.mirror_square(Position.flip_square(Position.dst(mv))))