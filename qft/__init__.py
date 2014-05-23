


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
    
    
class Variables:
    __slots__ = '_items'
    

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
        



