import copy
import tkinter as tk
import json
import ast
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageOps

from Model.EBoardModel import EBoardModel
from Const.GuiConst import *
from View.Arrange import Arrange
from View.BoardView import BoardView
from Model.BoardModel import BoardModel
from Utils.FenUtils import FenUtils
from Model.GameInfo import GameInfo
from Sound.Sound import Sound

import os

RESOURCE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Asset'))
PIECE_TYPE = ['Chinese Piece','English Piece','Figure Piece']
PIECE_LIST = [['Red King','Red Advisor','Red Elephant','Red Horse','Red Rook','Red Cannon','Red Pawn',
              'Black King','Black Advisor','Black Elephant','Black Horse','Black Rook','Black Cannon','Black Pawn'],
              ['Black King','Black Advisor','Black Elephant','Black Horse','Black Rook','Black Cannon','Black Pawn',
               'Red King','Red Advisor','Red Elephant','Red Horse','Red Rook','Red Cannon','Red Pawn']]
SIDE = ['Person','Computer']
LEVEL_TYPE = ['Easy','Medium','Difficult']
DEPTH = [3,DEFAULT_PLY_DEPTH ,5]
class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.geometry("600x420+400+250")
        self.title("Setting")
        # create tab control
        self.TAB_CONTROL = ttk.Notebook(self)
        self.TAB_CONTROL.pack(expand=1, fill="both")
        # Tab1
        self.TAB1 = ttk.Frame(self.TAB_CONTROL, height=2)
        self.TAB_CONTROL.add(self.TAB1, text='Change Interface')
        # Tab2
        self.TAB2 = ttk.Frame(self.TAB_CONTROL)
        self.TAB_CONTROL.add(self.TAB2, text='Change Experience')
        # Tab3
        self.TAB3 = ttk.Frame(self.TAB_CONTROL)
        self.TAB_CONTROL.add(self.TAB3, text='Save board')
        # Tab4
        self.TAB4 = ttk.Frame(self.TAB_CONTROL)
        self.TAB_CONTROL.add(self.TAB4, text='Statistic')


        #Tab5
        self.TAB5 = ttk.Frame(self.TAB_CONTROL)
        self.TAB_CONTROL.add(self.TAB5, text='Arrange Board')

        # Tab6
        self.TAB6 = ttk.Frame(self.TAB_CONTROL)
        self.TAB_CONTROL.add(self.TAB6, text='About')

        # self.resizable(width=True, height=True)
        self.var = ''
        self.type_piece = ''
        self.side = ''
        self.level = ''
        self.img_piece = './Asset/pieces/bk.png'
        self.img_background = "./Asset/pieces/background.png"

        # self.img_opacity_default()

        # Tab1
        self.option_choose_pieces_tab1()
        self.option_type_pieces_tab1()
        self.option_side_tab2()
        self.option_level_tab2()
        self.btn_choose_img_tab1()
        self.btn_change_background_tab1()
        self.btn_ok_tab1()

        #Tab2
        self.btn_ok_tab2()
        self.btn_open_test_tab5()
        self.label_piece_tab1()
        self.open_background_default_tab6()
        self.open_piece_default_tab1()
        self.label_tab2()
        # tab2
        self.button_change_sound_tab2()
        # tab5
        self.img_about_tab6()
        self.label_about_tab6()


        # tab3
        self.save_board_tab3()
        self.statistic_tab4()
        self.mainloop()

    def option_choose_pieces_tab1(self):
        self.var = StringVar(self)
        self.var.set("Choose Piece")  # initial value
        option = OptionMenu(self.TAB1, self.var, *PIECE_LIST[0])
        option.config(height=1, width=12, bg='#33BBFF')
        option.place(x=100, y=60)

    def option_type_pieces_tab1(self):
        self.type_piece = StringVar(self)
        self.type_piece.set(BoardModel.get_instance().typepiece)  # initial value
        option = OptionMenu(self.TAB1, self.type_piece, *PIECE_TYPE)
        option.config(height=1, width=13, bg='#33BBFF')
        option.place(x=380, y=100)

    def open_piece_default_tab1(self):
        if self.img_piece != '':
            try:
                img = Image.open(self.img_piece)
                img = img.resize((200, 200), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                panel = Label(self.TAB1, image=img)
                panel.image = img
                panel.place(x=60, y=150)
            except :
                print('not open imges')


    def open_img_piece_tab1(self):
        filename = filedialog.askopenfilename(title='Choose Image')
        if filename != '':
            self.img_piece = filename
        self.open_piece_default_tab1()

    def option_side_tab2(self):
        self.side = StringVar(self)
        self.side.set(BoardModel.get_instance().whofist)  # initial value
        option = OptionMenu(self.TAB2, self.side, *SIDE)
        option.config(height=1, width=12, bg='#33BBFF')
        option.place(x=150, y=100)

    def option_level_tab2(self):
        self.level = StringVar(self)
        self.level.set(LEVEL_TYPE[DEPTH.index(BoardModel.get_instance().plydepth)])  # initial value
        option = OptionMenu(self.TAB2, self.level, *LEVEL_TYPE)
        option.config(height=1, width=12, bg='#33BBFF')
        option.place(x=150, y=150)

    def open_background_default_tab6(self):
        if self.img_background != '':
            try:
                img = Image.open(self.img_background)
                img = img.resize((200, 200), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                panel = Label(self.TAB1, image=img)
                panel.image = img
                panel.place(x=340, y=150)
            except:
                print('not open')

    def open_img_background(self):
        filename = filedialog.askopenfilename(title='Choose Image')
        self.img_background = filename
        self.open_background_default_tab6()

    def img_about_tab6(self):
        img_about = './Asset/About/bachkhoa.png'
        img = Image.open(img_about)
        img = img.resize((600, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self.TAB6, image=img)
        panel.image = img
        panel.place(x=0, y=0)

    def img_opacity_default(self):
        img_opacity = './Asset/About/bachkhoa2.png'
        img = Image.open(img_opacity)
        img = img.resize((600, 400), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel1 = Label(self.TAB1, image=img)
        panel2 = Label(self.TAB2, image=img)
        panel3 = Label(self.TAB3, image=img)
        panel1.image = img
        panel1.place(x=0, y=0)

    def open_sound_tab2(self):
        direction = StringVar()
        direction.set("")
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=
        (("jpeg files", "*.jpg"), ("all files", "*.*")))
        label1 = Label(self.TAB2, textvariable=direction, font=(None, 10)).place(x=15, y=10)
        try:
            pygame.mixer.music.load(open(filename, "rb"))
            pygame.mixer.music.play()
            direction.set('')
            label = Label(self.TAB2, text=filename, font=(None, 10)).place(x=20, y=10)
        except:
            direction.set('')


    def open_test_tab5(self):
        Arrange.board_arrangement()
        self.destroy()

    def close_test_tab5(self):
        Arrange.board_init()
        self.destroy()

    def change_tab1(self):
        BoardModel.get_instance().typepiece = self.type_piece.get()
        if BoardModel.get_instance().top_color == COLOR[0]:
            BoardModel.get_instance().images = IMAGES_PERSON_FIRST[PIECE_TYPE.index(self.type_piece.get())]
        else:
            BoardModel.get_instance().images = IMAGES_AI_FIRST[PIECE_TYPE.index(self.type_piece.get())]
        BoardView.get_instance().draw_pieces()
        #Change face of piece
        if self.img_piece != '':
            try:
                card = Image.open(self.img_piece).convert("RGBA")
                img = Image.open("./Asset/ChangePiece/bg.png").convert("RGBA")
                size = img.size
                card = card.resize(size, Image.ANTIALIAS)
                mask = Image.new('L', size, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse([(175, 175), (820, 820)] , fill=255)
                mask = mask.resize(size, Image.ANTIALIAS)
                card.putalpha(mask)
                output = ImageOps.fit(card, mask.size, centering=(0, 0))
                output.putalpha(mask)
                img.paste(output,(0, 0, size[0], size[1]), output)
                # output.paste(img, (0, 0, size[0], size[1]), img)
                img.save('./Asset/ChangePiece/change.png')
                img_change = pygame.transform.smoothscale(pygame.image.load('./Asset/ChangePiece/change.png'), PIECE_SIZE)
                if self.var.get() != 'Choose Piece':
                    if GameInfo.get_instance().LowerSideMoveFirst:
                        BoardModel.get_instance().images[PIECE_LIST[0].index(self.var.get())] = img_change
                    else:
                        BoardModel.get_instance().images[PIECE_LIST[1].index(self.var.get())] = img_change
                    BoardView.get_instance().draw_pieces()
            except:
                print("Can not open file")
        #Change background
        if self.img_background != '':
            try:
                BoardView.get_instance().BOARD_BACKGROUND = pygame.transform.smoothscale(
                    pygame.image.load(self.img_background), (WINDOW_HEIGHT, WINDOW_HEIGHT))
            except:
                print("Can not open image")
        self.destroy()

    def change_side_tab2(self):
        if self.side.get() != BoardModel.get_instance().whofist:
            if self.side.get() == 'Computer':
                BoardModel.get_instance().state = copy.deepcopy(INIT_STATE)
                BoardModel.get_instance().images = IMAGES_AI_FIRST[PIECE_TYPE.index(
                    BoardModel.get_instance().typepiece)]
                BoardView.get_instance().draw_pieces()
                BoardModel.get_instance().previousStep.empty()
                GameInfo.get_instance().LowerSideMoveFirst = False
                BoardModel.get_instance().top_color = COLOR[1]
                GameInfo.get_instance().reset_attributes_to_new_game()
                BoardModel.get_instance().whofist = self.side.get()
            elif self.side.get() == 'Person':
                BoardModel.get_instance().state = copy.deepcopy(INIT_STATE)
                BoardModel.get_instance().images = IMAGES_PERSON_FIRST[PIECE_TYPE.index(
                    BoardModel.get_instance().typepiece)]
                BoardView.get_instance().draw_pieces()
                BoardModel.get_instance().previousStep.empty()
                GameInfo.get_instance().LowerSideMoveFirst = True
                BoardModel.get_instance().top_color = COLOR[0]
                GameInfo.get_instance().reset_attributes_to_new_game()
                BoardModel.get_instance().whofist = self.side.get()

        BoardModel.get_instance().plydepth = DEPTH[LEVEL_TYPE.index(self.level.get())]
        self.destroy()

    def btn_choose_img_tab1(self):
        btn = Button(self.TAB1, text='Choose Image', command=self.open_img_piece_tab1, height=1, width=15, bg='#33BBFF')
        btn.place(x=100, y=100)

    def btn_ok_tab1(self):
        btn = Button(self.TAB1, text="OK", command=self.change_tab1, height=1, width=10, bg='#33BBFF')
        btn.place(x=265, y=360)

    def btn_ok_tab2(self):
        btn = Button(self.TAB2, text="OK", command=self.change_side_tab2, height=1, width=15, bg='#33BBFF')
        btn.place(x=150, y=200)

    def btn_change_background_tab1(self):
        btn = Button(self.TAB1, text="Choose Backgound", command=self.open_img_background, height=1, width=16,
                     bg='#33BBFF')
        btn.place(x=380, y=60)

    def button_change_sound_tab2(self):
        btn = Button(self.TAB2, text='Choose Sound', command=self.open_sound_tab2, height=1, width=15, bg='#33BBFF')
        btn.place(x=150, y=50)

    def btn_open_test_tab5(self):
        btn = Button(self.TAB5, text='Open', command=self.open_test_tab5, height=1, width=15, bg='#33BBFF')
        btn.place(x=100, y=100)
        btn2 = Button(self.TAB5, text='Close', command=self.close_test_tab5, height=1, width=15, bg='#33BBFF')
        btn2.place(x=100, y=150)

    def label_piece_tab1(self):
        Label(self.TAB1, text="Change Pieces", font=(None, 15)).place(x=90, y=10)
        Label(self.TAB1, text="Change Background", font=(None, 15)).place(x=370, y=10)

    def label_tab2(self):
        Label(self.TAB2, text="Music", font=(None, 15)).place(x=50, y=50)
        Label(self.TAB2, text="Who first?", font=(None, 15)).place(x=50, y=100)
        Label(self.TAB2, text="Level", font=(None, 15)).place(x=50, y=150)
    def label_about_tab6(self):
        Label(self.TAB6, text='ThanhLongDo \n'
                              'HuynhVu \n'
                              'Department of computer science, \n'
                              'Faculty of computer science and engineering,\n'
                              'Bach Khoa university, HoChiMinh City, VietNam.\n'
              , font=(None, 10)).place(x=10, y=10)

    def save_board_tab3(self):
        btn = Button(self.TAB3, text="Save board", command=self.saveFen_tab3, height=1, width=15, bg='#33BBFF')
        btn.place(x=100, y=100)

        btn = Button(self.TAB3, text="Load board", command=self.loadFen_tab3, height=1, width=15, bg='#33BBFF')
        btn.place(x=100, y=150)

    def saveFen_tab3(self):
        try:
            fen = FenUtils.matrix2fen(BoardModel.get_instance().state)
            if GameInfo.get_instance().isUpperTurn:
                sidefist = 'top'
            else:
                sidefist = 'bellow'
            img = str(BoardModel.get_instance().images)
            type_piece = BoardModel.get_instance().typepiece
            if GameInfo.get_instance().mode == MODE[0]:
                mode = '0'
            else:
                mode = '1'
            color = BoardModel.get_instance().top_color
            data = {}
            data['saveboard'] = []
            data['saveboard'].append({
                'fen': fen ,
                'side': sidefist,
                'typepiece': type_piece,
                'mode': mode,
                'top_color': color,
                'number_step_red': BoardModel.get_instance().number_step_red,
                'number_step_black': BoardModel.get_instance().number_step_black
            })
            with open('View\data.txt', 'w') as outfile:
                json.dump(data, outfile)
        except:
            print("can not save file")
        Label(self.TAB3, text="Board is saved !", font=(None, 15)).place(x=100, y=20)


    def loadFen_tab3(self):
        try:
            with open('View\data.txt') as json_file:
                data = json.load(json_file)
                for p in data['saveboard']:
                    BoardModel.get_instance().state = FenUtils.fen2matrix(p['fen'])
                    BoardModel.get_instance().top_color = p['top_color']
                    BoardModel.get_instance().typepiece = p['typepiece']
                    if p['top_color'] == 'red':
                        BoardModel.get_instance().images = IMAGES_PERSON_FIRST[PIECE_TYPE.index(p['typepiece'])]
                    else:
                        BoardModel.get_instance().images = IMAGES_AI_FIRST[PIECE_TYPE.index(p['typepiece'])]
                    if p['side'] == 'top':
                        BoardModel.get_instance().isUpperTurn = True
                    else:
                        BoardModel.get_instance().isUpperTurn = False

                    if p['mode'] == '0':
                        GameInfo.get_instance().mode = MODE[0]
                        for s in EBoardModel.get_instance().button_group:
                            if s.type == 'mode':
                                s.index = 0
                                s.image = MODE_BUTTON[0]
                    else:
                        GameInfo.get_instance().mode = MODE[1]
                        for s in EBoardModel.get_instance().button_group:
                            if s.type == 'mode':
                                s.index = 1
                                s.image = MODE_BUTTON[1]
                    BoardModel.get_instance().number_step_red = p['number_step_red']
                    BoardModel.get_instance().number_step_black = p['number_step_black']
                    BoardView.get_instance().draw_pieces()
                    BoardModel.get_instance().previousStep.empty()
        except:
            Label(self.TAB3, text="Board is not saved !", font=(None, 15)).place(x=100, y=20)
        self.destroy()

    def sound_move_piece(self):
        Sound.get_instance().is_turn_on_move = True

    def statistic_tab4(self):
        text_red = 'Number of moves Red : '+ str(BoardModel.get_instance().number_step_red)
        text_black = 'Number of moves Black : ' + str(BoardModel.get_instance().number_step_black)
        Label(self.TAB4, text=text_red, font=(None, 15)).place(x=90, y=10)
        Label(self.TAB4, text=text_black , font=(None, 15)).place(x=90, y=50)

    def sound_track(self):
        pass

    def quit(self):
        self.destroy()
