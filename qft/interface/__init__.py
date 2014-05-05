

from buttoncodes import *
hotkeys = HOTKEYS
global hotkeys
__all__ = ()

def reset_hotkeys():
    hotkeys = HOTKEYS


class QFTButton(CodedButtonBase):
    __slots__ = CodedButtonBase.__slots__
    def hotkey_formatted(button):
        if hotkeys[button][0] == EMPTY: return ""
        elif hotkeys[button[1] == EMPTY:
            return "\n\n(hotkey: {0} )"get_hotkey_name(hotkeys[button][0]
        else:
            return "\n\n(hotkeys: {0} or {1} )".format(
                get_hotkey_name(hotkeys[button][0],
                get_hotkey_name(hotkeys[button][1]))
