



    
CUM =       'Cum'
MILK =      'Milk'
ALCOHOL =   'Alcohol'
ADDICTION = 'Addiction'
BODY =      'Body'
SKILLS =    'Skills'


from trpg.baseclasses import NamedBase
from trpg.baseclasses import ValueDict
class AddictionTypes(NamedBase):
    __slots__ = '_name', '_cum', '_milk', '_alcohol'
    def __init__(self):
        self._name =    ADDICTION
        self._cum =     Addiction(CUM)
        self._milk =    Addiction(MILK)
        self._alcohol = Addiction(ALCOHOL)
    
    def __get__(self):  return self._cum, self._milk, self._alcohol
    
    
    class Addiction(ValueDict):
        __slots__ = (ValueDict.__slots__, '_name')
        def __init__(self, name):
            self._name = name
            self._items = {}
        
        @property
        def name(self):
            return self._name
            
            
class Body(DictBase):
    __slots__ = '_name', '_items'
    def __init__(self):
        self._name = BODY
        self._items = {
        
        }
        
    def get_gender(self):
        if COCK in self._items:
            if POON in self._items: return GENDERS_H
            elif self._items[BREASTS][SIZE][0] >= 4: return GENDERS_I
            else: return GENDERS_M
        elif POON in self._items:
            if BALLS in self._items: return GENDERS_I
            return GENDERS_F
        else: return GENDERS_N
        
GENDERS_H = 'Hermaphrodite' # has cock and poon
GENDERS_F = 'Female'
GENDERS_M = 'Male'
GENDERS_I = 'Intersex'  # cock+tits or poon+balls-cock
GENDERS_N = 'Neuter'    # no poon or cock
        
        
        
        
