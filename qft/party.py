class Party:
    """Party base class."""
    def __init__(self):
        self._slots = []
        
    def get_chars(self):
        """Return an iterator of characters in order."""
        return iter(self._dg(i) for i in range(CHAR_SLOT0, CHAR_SLOT4))
# ---------------------------------------------------------------------------- #

from baseclasses import _SB

from codes.ccodes import CCODES_PARTY
from codes import *

pcparty = PlayerParty
__all__ = 'pcparty'

class PlayerParty(_SB):
    """PC Party class."""
    __slots__ = _SB.__slots__
    def __init__(self):
        self._ccode = CCODES_PARTY

    def get_chars(self):
        """Return an iterator of characters in order."""
        return iter(self._st_gi(i) for i in range(CHAR_SLOT0, CHAR_SLOT4))
    
    def swap_slot(self, a, b):
        """Swap two character slots."""
        if (a != b and 0 <= (a and b) <= 4:
            tmp = self._st_gi(a)
            self._st_si(a, self._st_gi(b))
            self._st_si(b, tmp)
