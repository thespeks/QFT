



# Main Buttons
MB_0 =  0
MB_1 =  1
MB_2 =  2
MB_3 =  3
MB_4 =  4
MB_5 =  5
MB_6 =  6
MB_7 =  7
MB_8 =  8
MB_9 =  9
MB_10 = 10
MB_11 = 11
MB_12 = 12
MB_13 = 13





MAIN_BUTTONS =  ((MB_0, MB_1,  MB_2,  MB_3,  MB_4),
                 (MB_4, MB_5,  MB_6,  MB_7,  MB_8),
                 (MB_9, MB_10, MB_11, MB_12, MB_13))


EMPTY = ""

# from kbdinput import keys

HOTKEYS = {
    #MainButtons
    MB_0:   (, EMPTY),
    MB_1:   (, EMPTY),
    MB_2:   (keys.ARROW_UP, keys.NUM_PAD_8),      # UP
    MB_3:   (, EMPTY),
    MB_4:   (, EMPTY),
    MB_5:   (keys.ARROW_LEFT, keys.NUM_PAD_4),    # Left
    MB_6:   (, EMPTY),
    MB_7:   (keys.ARROW_LEFT, keys.NUM_PAD_6),    # Right
    MB_8:   (, EMPTY),
    MB_9:   (, EMPTY),
    MB_10:  (, EMPTY),
    MB_11:  (keys.ARROW_DOWN, keys.NUM_PAD_11),   # Down
    MB_12:  (, EMPTY),
    MB_13:  (, EMPTY),

}
