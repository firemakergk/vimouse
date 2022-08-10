#-*- coding: UTF-8 -*-
from pynput import keyboard
import pynput._util.win32_vks as VK
from pynput._util.win32 import KeyTranslator
from pynput.keyboard._win32 import KeyCode as KeyCodeWin32

class KeyCodeUtil:
    keyTranslator = KeyTranslator()

    vkMap = dict()
    vkMap[VK.MENU] = 'alt'
    vkMap[VK.LMENU] = 'alt_l'
    vkMap[VK.RMENU] = 'alt_r'
    vkMap[VK.RMENU] = 'alt_gr'
    vkMap[VK.BACK] = 'backspace'
    vkMap[VK.CAPITAL] = 'caps_lock'
    vkMap[VK.LWIN] = 'cmd'
    vkMap[VK.LWIN] = 'cmd_l'
    vkMap[VK.RWIN] = 'cmd_r'
    vkMap[VK.CONTROL] = 'ctrl'
    vkMap[VK.LCONTROL] = 'ctrl_l'
    vkMap[VK.RCONTROL] = 'ctrl_r'
    vkMap[VK.DELETE] = 'delete'
    vkMap[VK.DOWN] = 'down'
    vkMap[VK.END] = 'end'
    vkMap[VK.RETURN] = 'enter'
    vkMap[VK.ESCAPE] = 'esc'
    vkMap[VK.F1] = 'f1'
    vkMap[VK.F2] = 'f2'
    vkMap[VK.F3] = 'f3'
    vkMap[VK.F4] = 'f4'
    vkMap[VK.F5] = 'f5'
    vkMap[VK.F6] = 'f6'
    vkMap[VK.F7] = 'f7'
    vkMap[VK.F8] = 'f8'
    vkMap[VK.F9] = 'f9'
    vkMap[VK.F10] = 'f10'
    vkMap[VK.F11] = 'f11'
    vkMap[VK.F12] = 'f12'
    vkMap[VK.F13] = 'f13'
    vkMap[VK.F14] = 'f14'
    vkMap[VK.F15] = 'f15'
    vkMap[VK.F16] = 'f16'
    vkMap[VK.F17] = 'f17'
    vkMap[VK.F18] = 'f18'
    vkMap[VK.F19] = 'f19'
    vkMap[VK.F20] = 'f20'
    vkMap[VK.F21] = 'f21'
    vkMap[VK.F22] = 'f22'
    vkMap[VK.F23] = 'f23'
    vkMap[VK.F24] = 'f24'
    vkMap[VK.HOME] = 'home'
    vkMap[VK.LEFT] = 'left'
    vkMap[VK.NEXT] = 'page_down'
    vkMap[VK.PRIOR] = 'page_up'
    vkMap[VK.RIGHT] = 'right'
    vkMap[VK.LSHIFT] = 'shift'
    vkMap[VK.LSHIFT] = 'shift_l'
    vkMap[VK.RSHIFT] = 'shift_r'
    vkMap[VK.SPACE] = 'space'
    vkMap[VK.TAB] = 'tab'
    vkMap[VK.UP] = 'up'

    vkMap[VK.MEDIA_PLAY_PAUSE] = 'media_play_pause'
    vkMap[VK.VOLUME_MUTE] = 'media_volume_mute'
    vkMap[VK.VOLUME_DOWN] = 'media_volume_down'
    vkMap[VK.VOLUME_UP] = 'media_volume_up'
    vkMap[VK.MEDIA_PREV_TRACK] = 'media_previous'
    vkMap[VK.MEDIA_NEXT_TRACK] = 'media_next'

    vkMap[VK.INSERT] = 'insert'
    vkMap[VK.APPS] = 'menu'
    vkMap[VK.NUMLOCK] = 'num_lock'
    vkMap[VK.PAUSE] = 'pause'
    vkMap[VK.SNAPSHOT] = 'print_screen'
    vkMap[VK.SCROLL] = 'scroll_lock'
    
    
    @classmethod
    def key2Vk(cls, key):
        if isinstance(key, keyboard.Key):
            return key.value.vk
        elif isinstance(key, keyboard._win32.KeyCode):
            return key.vk
        else:
            return None

    @classmethod
    def keys2Vks(cls, keys: set):
        res = set()
        for key in keys:
            res.add(cls.key2Vk(key))
        return res
        
    @classmethod
    def vk2Char(cls, vk):
        res = cls.vkMap.get(vk, None)
        if(res == None):
            res = cls.keyTranslator(vk,None).get('char',None)
        return res