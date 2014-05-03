
# Male Stats
VERILITY =  'Verility'  # only valid if balls

# Male Statuses
RUT =       'Rut'

# Female Stats  
FERTILITY = 'Fertility' # only valid if ovaries

# Female Statuses
PREG =      'Pregnant'
HEAT =      'Heat'

# Basic Stats
HEALTH =    'Health'
LUST =      'Lust'

# Addictions
CUM_ADD =   'Cum Addiction'
MILK_ADD =  'Milk Addiction'





class Char:
    _items = {
        STAT_AGIL: 10,
        STAT_FLEX: 5,
        STAT_STRN: 10,
        STAT_SPED: 5,
        STAT_LIBD: 10,
        STAT_HLTH: 100,
        STAT_ENRG: 100,
        STAT_AROU: 0,
        STAT_STAM: 50,
        }


    @property
    def health(self):
        """The health stat for this character."""
        return self['stat_health']
        
    
    
