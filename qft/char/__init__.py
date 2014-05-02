
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
        HEALTH:     100,
        }


    @property
    def health(self):
        """The health stat for this character."""
        return self['stat_health']
        
    @property
    def lust(self):
        """The lust stat for this character."""
        return self.['stat_lust']
        
    
    
