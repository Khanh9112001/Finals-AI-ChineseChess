from Database.book import *
NUMSTRING = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
CHESSMAN1 = {'K', 'A', 'E', 'R', 'C', 'H', 'P'}
CHESSMAN2 = {'k', 'a', 'e', 'r', 'c', 'h', 'p'}
PIECE_KING = 0
PIECE_ADVISOR = 1
PIECE_BISHOP = 2
PIECE_KNIGHT = 3
PIECE_ROOK = 4
PIECE_CANNON = 5
PIECE_PAWN = 6

RANK_TOP = 3
RANK_BOTTOM = 12
FILE_LEFT = 3
FILE_RIGHT = 11

ADD_PIECE = False
DEL_PIECE = True

def RANK_Y(sq):  # vi tri hang
    return sq >> 4


def FILE_X(sq):  # vi tri cot
    return sq & 15


def COORD_XY(x, y):
    return x + (y << 4)


def SQUARE_FLIP(sq):
    return 254 - sq


def FILE_FLIP(x):
    return 14 - x


def RANK_FLIP(y):
    return 15 - y


def MIRROR_SQUARE(sq):
    return COORD_XY(FILE_FLIP(FILE_X(sq)), RANK_Y(sq))
def MOVE(sqSrc, sqDst):
  return sqSrc + (sqDst << 8)

def  MIRROR_MOVE(mv):
  return MOVE(MIRROR_SQUARE(SRC(mv)), MIRROR_SQUARE(DST(mv)))

def SRC(mv):
    return mv & 255


def DST(mv):
    return mv >> 8


def CHAR_TO_PIECE(c):
    if c == "K":
        return PIECE_KING
    elif c == "A":
        return PIECE_ADVISOR
    elif c == "B" or c == "E":
        return PIECE_BISHOP
    elif c == "H" or c == "N":
        return PIECE_KNIGHT
    elif c == "R":
        return PIECE_ROOK
    elif c == "C":
        return PIECE_CANNON
    elif c == "P":
        return PIECE_PAWN
    return -1

FEN_PIECE = "        KAEHRCP kaehrcp "
def binarySearch(vlss, vl):
    low = 0
    high = len(vlss) - 1
    while low <= high:
        mid = (low + high) // 2
        if vlss[mid][0] < vl:
            low = mid + 1
        elif vlss[mid][0] > vl:
            high = mid - 1
        else:
            return mid
    return -1
def insort_right(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.
    If x is already in a, insert it to the right of the rightmost x.
    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid][0]:
            hi = mid
        else:
            lo = mid+1
    return lo
    #a.insert(lo, x)
def formatFile(dat):
    s='BOOK_DAT=['+'\n'
    for i in range(0,len(dat)):
        s+='['
        for j in range(0,len(dat[i])):
            s+=str(dat[i][j])
            if j!=len(dat[i])-1:
                s+=','+' '
            else:
                s+=']'
        if i!=len(dat)-1:
            s+=','+'\n'
    return s+'\n'+']'
class RC4:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = []
        self.RC4_key([0])

    def swap(self, i, j):
        t = self.state[i]
        self.state[i] = self.state[j]
        self.state[j] = t

    def RC4_key(self, key):
        for i in range(0, 256):
            self.state.append(i)
        j = 0
        for i in range(0, 256):
            j = (j + self.state[i] + key[i % len(key)]) & 0xff
            self.swap(i, j)

    def nextByte(self):
        self.x = (self.x + 1) & 0xff
        self.y = (self.y + self.state[self.x]) & 0xff
        self.swap(self.x, self.y)
        t = (self.state[self.x] + self.state[self.y]) & 0xff
        return self.state[t]

    def nextLong(self):
        n0 = self.nextByte()
        n1 = self.nextByte()
        n2 = self.nextByte()
        n3 = self.nextByte()
        return n0 + (n1 << 8) + (n2 << 16) + ((n3 << 24) & 0xffffffff)


PreGen_zobristKeyTable = []
PreGen_zobristLockTable = []

rc4 = RC4()
PreGen_zobristKeyPlayer = rc4.nextLong()

rc4.nextLong()
PreGen_zobristLockPlayer = rc4.nextLong()

for i in range(0, 14):
    keys = []
    locks = []
    for j in range(0, 256):
        keys.append(rc4.nextLong())
        rc4.nextLong()
        locks.append(rc4.nextLong())

    PreGen_zobristKeyTable.append(keys)
    PreGen_zobristLockTable.append(locks)

class Hashtable:
    def __init__(self):
        self.zobristLock = 0
        self.sdPlayer = 0
        self.squares = []
        for sq in range(0, 256):
            self.squares.append(0)

    def fromFen(self, fen):
        y = RANK_TOP
        x = FILE_LEFT
        index = 0
        c = fen[index]
        while c != ' ':
            if c == '/':
                x = FILE_LEFT
                y += 1
                if y > RANK_BOTTOM:
                    break
            elif c in NUMSTRING:
                for i in range(0, int(c)):
                    if x >= FILE_RIGHT:
                        break
                    x += 1
            elif c in CHESSMAN1:  # chu hoa
                if x <= FILE_RIGHT:
                    pt = CHAR_TO_PIECE(c)
                    if pt >= 0:
                        self.addPiece(COORD_XY(x, y), pt + 8, False)
                    x += 1
            elif c in CHESSMAN2:  # chu thuong
                if x <= FILE_RIGHT:
                    pt = CHAR_TO_PIECE(c.upper())
                    if pt >= 0:
                        self.addPiece(COORD_XY(x, y), pt + 16, False)
                    x += 1
            index += 1
            c = fen[index]
        index += 1
        if index == len(fen):
            return
        if fen[index] == 'b' and self.sdPlayer == 0:
            self.changeSide()
        elif fen[index] == 'w' and self.sdPlayer == 1:
            self.changeSide()

    def changeSide(self):
        self.sdPlayer = 1 - self.sdPlayer
        self.zobristLock ^= PreGen_zobristLockPlayer

    def addPiece(self, sq, pc, bDel):
        if bDel:
            self.squares[sq] = 0
        else:
            self.squares[sq] = pc
        if pc < 16:
            pcAdjust = pc - 8
        else:
            pcAdjust = pc - 16
            pcAdjust += 7
        self.zobristLock ^= PreGen_zobristLockTable[pcAdjust][sq]
    def toFen(self):
        fen = ''
        for y in range(RANK_TOP, RANK_BOTTOM + 1):
            k = 0
            for x in range(FILE_LEFT, FILE_RIGHT + 1):
                pc = self.squares[COORD_XY(x, y)]
                if pc > 0:
                    if k > 0:
                        fen += str(k)
                        k = 0
                    fen += FEN_PIECE[pc]
                else:
                    k += 1
            if k > 0:
                fen += str(k)
            fen += '/'
        return fen[0:len(fen) - 1]
    def mirror(self):
        pos = Hashtable()
        for sq in range(0, 256):
            pc = self.squares[sq]
            if pc > 0:
                pos.addPiece(MIRROR_SQUARE(sq), pc, False)
        if self.sdPlayer == 1:
            pos.changeSide()
        return pos.zobristLock
    def Insert_Dat(self, move):
        if len(BOOK_DAT) == 0:
            return 0

        mirror = False
        lock1 = self.zobristLock >> 1  # Convert into Unsigned
        index = binarySearch(BOOK_DAT, lock1)
        if index < 0:
            mirror = True
            lock2 = self.mirror() >> 1  # Convert into Unsigned
            index = binarySearch(BOOK_DAT, lock2)
        if index < 0:
            lo=insort_right(BOOK_DAT,lock1)
            value=1
            BOOK_DAT.insert(lo,[lock1,move,value])
            with open('Database/book.py', 'w') as f:
                f.write(formatFile(BOOK_DAT))
            print(lo,BOOK_DAT)
            return 1
        print('Existed in Database')
        return 0
