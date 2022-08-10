#-*- coding: UTF-8 -*-
from enum import Enum

class Action(Enum):
    MOVE_DOWN = 'MOVE_DOWN'
    MOVE_UP = 'MOVE_UP'
    MOVE_LEFT = 'MOVE_LEFT'
    MOVE_RIGHT = 'MOVE_RIGHT'
    MOVE_DOWN_STOP = 'MOVE_DOWN_STOP'
    MOVE_UP_STOP = 'MOVE_UP_STOP'
    MOVE_LEFT_STOP = 'MOVE_LEFT_STOP'
    MOVE_RIGHT_STOP = 'MOVE_RIGHT_STOP'
    SCROLL_UP = 'SCROLL_UP'
    SCROLL_UP_STOP = 'SCROLL_UP_STOP'
    SCROLL_DOWN = 'SCROLL_DOWN'
    SCROLL_DOWN_STOP = 'SCROLL_DOWN_STOP'
    PRESS_LEFT = 'PRESS_LEFT'
    RELEASE_LEFT = 'RELEASE_LEFT'
    PPRESS_RIGHT = 'PPRESS_RIGHT'
    RELEASE_RIGHT = 'RELEASE_RIGHT'
    SCROLL_PRESS = 'SCROLL_PRESS'
    SCROLL_RELEASE = 'SCROLL_RELEASE'
    COPY = 'COPY'
    CUT = 'CUT'
    PASTE = 'PASTE'
    EDIT = 'EDIT'
    UNDO = 'UNDO'
    SPEED_BUFF_1 = 'SPEED_BUFF_1'
    SPEED_BUFF_1_STOP = 'SPEED_BUFF_1_STOP'
    SPEED_BUFF_2 = 'SPEED_BUFF_2'
    SPEED_BUFF_2_STOP = 'SPEED_BUFF_2_STOP'
    SPEED_BUFF_3 = 'SPEED_BUFF_3'
    SPEED_BUFF_3_STOP = 'SPEED_BUFF_3_STOP'
    SPEED_BUFF_4 = 'SPEED_BUFF_4'
    SPEED_BUFF_4_STOP = 'SPEED_BUFF_4_STOP'
    SPEED_BUFF_5 = 'SPEED_BUFF_5'
    SPEED_BUFF_5_STOP = 'SPEED_BUFF_5_STOP'

class MoveAction(Enum):
    MOVE_DOWN = 'MOVE_DOWN'
    MOVE_UP = 'MOVE_UP'
    MOVE_LEFT = 'MOVE_LEFT'
    MOVE_RIGHT = 'MOVE_RIGHT'
    SCROLL_UP = 'SCROLL_UP'
    SCROLL_DOWN = 'SCROLL_DOWN'
    SPEED_BUFF_1 = 'SPEED_BUFF_1'
    SPEED_BUFF_1_STOP = 'SPEED_BUFF_1_STOP'
    SPEED_BUFF_2 = 'SPEED_BUFF_2'
    SPEED_BUFF_2_STOP = 'SPEED_BUFF_2_STOP'
    SPEED_BUFF_3 = 'SPEED_BUFF_3'
    SPEED_BUFF_3_STOP = 'SPEED_BUFF_3_STOP'
    SPEED_BUFF_4 = 'SPEED_BUFF_4'
    SPEED_BUFF_4_STOP = 'SPEED_BUFF_4_STOP'
    SPEED_BUFF_5 = 'SPEED_BUFF_5'
    SPEED_BUFF_5_STOP = 'SPEED_BUFF_5_STOP'

class ClickAction(Enum):
    PRESS_LEFT = 'PRESS_LEFT'
    RELEASE_LEFT = 'RELEASE_LEFT'
    PPRESS_RIGHT = 'PPRESS_RIGHT'
    RELEASE_RIGHT = 'RELEASE_RIGHT'
    SCROLL_PRESS = 'SCROLL_PRESS'
    SCROLL_RELEASE = 'SCROLL_RELEASE'
    COPY = 'COPY'
    PASTE = 'PASTE'

class ActionKey(Enum):
    MOVE_DOWN = {'j'}
    MOVE_UP = {'k'}
    MOVE_LEFT = {'h'}
    MOVE_RIGHT = {'l'}
    PRESS_LEFT = {'i', 'e','v_O'}
    RELEASE_LEFT = {'i_R','e_R','v_C'}
    PPRESS_RIGHT = {'o','w'}
    RELEASE_RIGHT = {'o_R','w_R'}
    SCROLL_UP = {'r'}
    SCROLL_DOWN = {'f'}
    SCROLL_PRESS = {'d'}
    SCROLL_RELEASE = {'d_R'}
    COPY = {'y'}
    PASTE = {'p'}

moveEventMap = dict()
moveEventMap['_P_j'] = 'MOVE_DOWN'
moveEventMap['_R_j'] = 'MOVE_DOWN_STOP'
moveEventMap['_P_k'] = 'MOVE_UP'
moveEventMap['_R_k'] = 'MOVE_UP_STOP'
moveEventMap['_P_h'] = 'MOVE_LEFT'
moveEventMap['_R_h'] = 'MOVE_LEFT_STOP'
moveEventMap['_P_l'] = 'MOVE_RIGHT'
moveEventMap['_R_l'] = 'MOVE_RIGHT_STOP'
moveEventMap['_P_r'] = 'SCROLL_UP'
moveEventMap['_R_r'] = 'SCROLL_UP_STOP'
moveEventMap['_P_f'] = 'SCROLL_DOWN'
moveEventMap['_R_f'] = 'SCROLL_DOWN_STOP'
moveEventMap['_P_1'] = 'SPEED_BUFF_1'
moveEventMap['_R_1'] = 'SPEED_BUFF_1_STOP'
moveEventMap['_P_2'] = 'SPEED_BUFF_2'
moveEventMap['_R_2'] = 'SPEED_BUFF_2_STOP'
moveEventMap['_P_3'] = 'SPEED_BUFF_3'
moveEventMap['_R_3'] = 'SPEED_BUFF_3_STOP'
moveEventMap['_P_4'] = 'SPEED_BUFF_4'
moveEventMap['_R_4'] = 'SPEED_BUFF_4_STOP'
moveEventMap['_P_5'] = 'SPEED_BUFF_5'
moveEventMap['_R_5'] = 'SPEED_BUFF_5_STOP'
moveEventMap['_P_space'] = 'SPEED_BUFF_3'
moveEventMap['_R_space'] = 'SPEED_BUFF_3_STOP'
moveEventMap['_P_shift_l'] = 'SPEED_BUFF_2'
moveEventMap['_R_shift_l'] = 'SPEED_BUFF_2_STOP'

clickEventMap = dict()
clickEventMap['_P_i'] = 'PRESS_LEFT'
clickEventMap['_P_e'] = 'PRESS_LEFT'
clickEventMap['_O_v'] = 'PRESS_LEFT'
clickEventMap['_R_i'] = 'RELEASE_LEFT'
clickEventMap['_R_e'] = 'RELEASE_LEFT'
clickEventMap['_C_v'] = 'RELEASE_LEFT'
clickEventMap['_P_o'] = 'PPRESS_RIGHT'
clickEventMap['_P_w'] = 'PPRESS_RIGHT'
clickEventMap['_R_o'] = 'RELEASE_RIGHT'
clickEventMap['_R_w'] = 'RELEASE_RIGHT'
clickEventMap['_P_d'] = 'SCROLL_PRESS'
clickEventMap['_R_d'] = 'SCROLL_RELEASE'
clickEventMap['_P_a'] = 'EDIT'
clickEventMap['_P_y'] = 'COPY'
clickEventMap['_P_c'] = 'CUT'
clickEventMap['_P_p'] = 'PASTE'
clickEventMap['_P_u'] = 'UNDO'

speedBuffMap = dict()
speedBuffMap['SPEED_BUFF_1'] = 0.3
speedBuffMap['SPEED_BUFF_2'] = 0.6
speedBuffMap['SPEED_BUFF_3'] = 4
speedBuffMap['SPEED_BUFF_4'] = 8
speedBuffMap['SPEED_BUFF_5'] = 12
