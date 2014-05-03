
class Part:
    pass


class Eyes(Part):
    __slots__ = '_items'
    def __init__(self):
        self._items = {
            EYE_COL_L:  BLUE,
            EYE_COL_R:  BLUE,
            }
            
    
class Butt(Part):
    __slots__ = '_items'
    def __init__(self):
        self._items = {
            BUTT_SIZE:  2,
            BUTT_TONE:  50,
            }

class Boobs(Part):
    __slots__ = '_items'
    def __init__(self):
        self._items = {
            BOOB_SIZE:  2
            }


class Body:
    def __init__(self):
        self._items = {
        BITS_COL:     BROWN,
        EYE_COL_L:    BLUE,
        EYE_COL_R:    BLUE,
        
        # Nipz
        NIP_LEN:      1,
        NIP_COL:      BITS_COL,
            
        # Rump
        BUTT_SIZE:    2,    
        BUTT_TONE:    50,
        
        # Anus
        ANUS_SIZE:    2,
        ANUS_TIGHT:   2,
        ANUS_COL:     BITS_COL,
                
        
        HEIGHT:       72,
        WEIGHT:       133,
        }
        
    
        
        
        
        
        
        
        
