
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


        
def write_char_data(f, char):
    from qft.utils import write_attr_subdicts
    cpfx = '.'join('char', char.name)   # char prefix (char.thischarsname)
    for i in x._get_writables():    write_attr_subdicts(f, cpfx, i)
    
    
    
from baseclassses import AddictionTypes

class BaseChar:
    def __init__(self):
        self._name =        ""
        self._party =       None
        self._skills =      Skills()
        self._main_stats =  MainStats()
        self._body =        Body()
        self._addictions =  AddictionTypes():
    
    def _get_writables(self):
        return iter(self._body, self._skills, self._main_stats, self._addictions)
    
    @property
    def main_stats(self):
        """Main stats for this character."""
        return self._main_stats
        
    @property
    def body(self):
        return self._body

    @property
    def name(self):
        """The name of this character."""
        return self._name
        
    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._body.get_gender()

    def has_skill(self, skill, min_level=1):
        """Return True if this character has given skill of at least min_level"""
        return self._skills.is_ge(skill, min_level)
        
    
class MainStats(NamedValueDict):
    __slots__ = Named.ValueDict.__slots__
    def __init__(self, name):
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
    
    
    
    
    
    
    
    
