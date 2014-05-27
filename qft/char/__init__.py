


from .codes.ccodes import CCODES_CHARS
from .codes.ccodes import CCODES_CHAR
from .codes import *

from xsbc.storio import Storio

__all__ = 'active_chars', 'get_pc'

active_chars = {}

def get_char(charid):
    global active_chars
    from qft import data
    try:    return active_chars[CCODES_char, charid]
    except: return Char(charid)

def get_pc()
    return get_char(0)


class Char(Storio.SIMixin):
    __slots__ = SSIHandlerMixin.__slots__ + ('_charid', '_loc')
    def __init__(self, charid=None):
        # Storio init stuff
        from qft import data
        self._storio_init(data, CCODES_CHAR)

        if charid == None:  
            _reg_char(self, charid)

        # make a subdict if non-existant
        if self.st_hi(): data[(CCODES_CHAR, self._charid)] = {}
        
        self._loc = Location(self, code=LOC)
        
        # add to active_chars
        active_chars[CCODES_CHAR, self._charid] = self
    
    def st_dx(self):
        return (self._CCODE, self._charid)
    
    def _get_row(self): return self.st_gsi(ROW)
    def _set_row(self r):
        if r != self[ROW] and r in range(-1, 1):
            self[ROW] = r
    row = property(_get_row, _set_row, doc="The row for this character.")

    @property
    def location(self):
        """Location data for this character."""
        return self._loc
    
    @property
    def is_pc(self):
        """True if this character is the player character. (charid 0)"""
        return self._charid == 0
    
    @property
    def row_name(self):
        """The name of the row this character is in."""
        return ('Front', 'Middle', 'Back')[self.row]
    
    @property
    def charid(self):
        """The character id"""
        return self._charid
        
    # modifiable attributes
    def _get_name(self):        return self[NAME]
    def _set_name(self, x):  self[NAME] = x
    name = property(_get_name, _set_name, 
            doc="The name of this character.")
        
    def _get_height(self):      return self[HEIGHT]
    def _set_height(self, height):  self[HEIGHT] = x
    height = property(_get_height, _set_height, 
            doc="The height of this character.")
    
    @property    
    def statuses(self):
        """Get statuses for this character."""
        return self[STAUSES]
        
    # attribute getters - these are not stored, instead generated on call
    def get_gender(self):
        """The gender of this character."""
        if self._has_bp(COCK):
            if self._has_bp(POON):      return GEND_H           # herm
            elif self[BODY][BOOB, SIZE, 0] > 1: return GEND_DG  # dickgirl
            else:                       return GEND_M           # male
        elif self._has_bp(POON):
            if self[BODY][BOOB, SIZE, 0] < 1: return GEND_CB    # cuntboi
            else:                       return GEND_F           # female
        else:                           return GEND_N           # neuter
        
    def get_pronoun(self, assigned=False):
        if assigned:    # by self or player
            try: return self[GENDER, PRONOUN, assigned]
            except:     # get by gender
                if self.get_gender() == GEND_M or GEND_CB: return 1 # masucline
                else: return 0 # Feminine
                
        
    def get_weight(self):
        """The weight of this character."""
        return    
    
            
    def in_party(self, p=None):
        """True if this char is in 'p'"""
        if p is None:   return self.charid in data[CCODE_PARTY][ALL_IDS]
        else:           
    
    def has_skill(self, skill, min_level=1):
        """Return True if this character has given skill of at least min_level"""
        return _is_level(SKILLS, skill, min_level) # TODO implement XP
    
    def stat_level(self, stat, substat=LEVEL):
        try: return self[stat][substat]
        except: return 0
    
    def stat_level_plus_mult(self, stat):
        return self.get_stat_level(stat) * self.get_stat_level(stat, MULT]
    
        
    def _is_level(self, code, key, min_level):
        try: return self[code][key] > min_level
        except: return False
        
    def _has_bp(self, bp, sp=0, st=0):
        try: return (bp, sp, st) in self[BODY]
        except return False
        
        
from xsbc.storio import SubData

from qft.location import _Loc

class Location(_Loc, SubData):
    __slots__ = SubData.__slots__
    def __init__(self, parent, code):
        self._parent =  parent
        self._code =    code
    
    def __getitem__(self, i):       return self._parent[self._code][i]
    def __setitem__(self, i, v):    self._parent[self._code][i] = v
    
    def _get_reg(self):       return self.__getitem__(0)
    def _set_reg(self, x):    self.__setitem__(0, x)
    region = property(_get_reg, _set_reg, doc="The region.")
    reg = region
    
    def _get_sector(self):       return self.__getitem__(1)
    def _set_sector(self, x):    self.__setitem__(1, x)
    sector = property(_get_sector, _set_sector, doc="The current sector.")
    
    def _get_pos(self):       return self.__getitem__(2)
    def _set_pos(self, x):    self.__setitem__(2, x)
    position = property(_get_pos, _set_pos, doc="The x,y position.")
    pos = position
    
    def _get_px(self):       return self._char[self._code][2][0]
    def _set_px(self, x):    self._char[self._code][2][0] = x
    x = property(_get_px, _set_px, doc="The x position.")
    
    def _get_py(self):       return self._char[self._code][2][1]
    def _set_py(self, y):    self._char[self._code][2][1] = y
    y = property(_get_py, _set_py, doc="The y position.")
    
        
# -- Some basic utils -------------------------------------------------------- #
def get_char_codes(force=False):
    if force:
        if data[(CCODE_CHARS, ALL_IDS)] == []: return 0:
    else: return data[(CCODE_CHARS, ALL_IDS)]

# register character
def _reg_char(char, hint=None):
    # register this character to a unique charid
    if hint is not None:
        if int(hint) not in get_char_codes():   char._charid = int(hint)
        data[CCODE_CHARS, ALL_IDS].append(char._charid)
        return _chk_reg(char, int(hint))
    else:
        char._charid+1 = tuple(sorted(get_char_codes(force=True)))[-1]
        data[CCODE_CHARS, ALL_IDS].append(char._charid)
        return _chk_reg(char, char._charid)
        
def _chk_reg(char, hint):
    # make sure that we have a unique charid and if not retry
    if get_char_codes().count(hint) == 1:  return
    else:
        # try again
        import time
        time.sleep(0.1)
        return _reg_char(char, hint+1)

