
# Male Stats
VERILITY =  'Verility'  # only valid if balls

# Male Statuses
RUT =       'Rut'

# Female Stats  
FERTILITY = 'Fertility' # only valid if ovaries

# Female Statuses
PREG =      'Pregnant'
HEAT =      'Heat'

# Other
LACT =      'Lactation' # only if has nipples       

# Basic Stats
HEALTH =    'Health'
LUST =      'Lust'



class Addiction(ValueDict):
    __slots__ = ValueDict.__slots__, '_name')
    def __init__(self, name):
        self._name = name
        self._items = {}
    
    @property
    def name(self):
        return self._name
    
CUM = 'Cum'
MILK = 'Milk'
ALCOHOL = 'Alcohol'
    
class AddictionTypes:
    self._cum =     Addictions(CUM)
    self._milk =    Addiction(MILK)
    self._alcohol = Addictions(ALCOHOL)
        

class BaseChar:
    __slots__ = '_skills', '_main_stats'
    def __init__(self):
        self._party =       None
        self._skills =      ValueDict()
        self._main_stats =  MainStats()
        self._body =        ValueDict()
        self._addictions =  AddictionTypes():
        
    
    @property
    def main_stats(self):
        """Main stats for this character."""
        return self._main_stats
        
    @property
    def body(self):
        return self._body

    @property
    def gender(self):
        return self._body.get_gender()

    def has_skill(self, skill, min_level=1):
        """Return True if this character has given skill of at least min_level"""
        return self._skills.is_ge(skill, min_level)
        
    
class MainStats(ValueDict):
    __slots__ = ValueDict.__slots__
    def __init__(self):
        self._items = {
            STAT_HLTH: 100,
            STAT_ENRG: 100,
            STAT_AGIL: 10,
            STAT_FLEX: 5,
            STAT_STRN: 10,
            STAT_SPED: 5,
            STAT_LIBD: 10,
            STAT_AROU: 0,
            STAT_STAM: 50,
        }
    
    
    
    
    
    
