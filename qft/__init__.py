


def run():
    pass














# -- Game -------------------------------------------------------------------- #
from xsbc.storio import StorIO

game =      None
player =    None
data =      StorIO
global game, player, data
__all__ = 'game', 'player', 'data'

#   player = game.player

def _sanitize():
    # clear out/reset game and player variables
    current_game._variables.reset()
    player = None
    
    
class Variables(Storio.Mixin):
    """Class for managing game variables."""
    __slots__ = '_items'
    def __init__(self):
        from codes.ccodes import CCODES_VARIABLES
        self._storio_init(data, CCODES_VARIABLES)
    
    def datetime(self):
        return DateTime(self)


    class DateTime:
        def __init__(self, parent):
            self._parent = parent
            
        def __call__(self): return self._parent[TIME]
        
        def __add__(self, x):
            if not len(x) >= 4: x = x + tuple([0] * 4-len(x)) 
            m, h = divmod(self,minutes+x[0], 60)
            h, d = divmod(self.hours+x[1], 23)
            d, w = divmod(self.days+x[2], 6)
            return w, d, h, m
        __radd__ = __add__
        
        def update(self, minutes=0, hours=0, days=0, weeks=0):
            self._parent[TIME] = self + (minutes, hours, days, weeks)
        
        @property
        def minutes(self):
            return self._parent[TIME][0]
            
        @property
        def hours(self):
            return self._parent[TIME][1]
            
        @property
        def days(self):
            return self._parent[TIME][2]
    
        @property
        def weeks(self):
            return self._parent[TIME][3]
            

class Game(Storio.Mixin):
    __slots__ = '_variables'
    def __init__(self): 
        self._variables =   Variables()
        
        from codes.ccodes import CCODES_GAME
        self._storio_init(data, CCODES_GAME)
        
    @property
    def variables(self):
        """Access the variables for this game."""
        return self._variables
    
    def get_variable(self, v, fallback=None):
        """Return variable v if in variables else return fallback."""
        try:    return self._variables[v]
        except: return fallback
            
    def save_game(self):
        if self.is_savable():
            self[COMMENT] = ""  # TODO
            import datetime
            self[SAVE_TIME] = datetime.datetime.now()
            data.json_dump(fp)
        
    # Events ---- #
    def _init_game(self):
        """Called when initalizing a game."""
        player = Player()
    
    def on_quit_game(self):
        """Called when returning back to the mainmenu."""
        _sanitize
    
    def on_exit_game(self):
        """Called when exiting to the desktop."""
        pass



class Player:
    __slots__ = .__slots__
    def __init__(self):
    self._in_battle = False
    self._pc =      None
    self._party =   Party()
    
    
    @property
    def in_battle(self):
        """True if the player party is currently in battle."""
        return self._in_battle
        

# -- QFT Base Classes -------------------------------------------------------- #
class QFTObj:
    __slots__ = ()
    def __init__(self):
        pass
        
    def get_type(self):
        """The type of object this is."""
        return self.__class__.__name__.lower()

