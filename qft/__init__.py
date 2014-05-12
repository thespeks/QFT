


def run():
    pass














# -- Game -------------------------------------------------------------------- #
game =      None
player =    None
global game, player
__all__ = 'game', 'player'

#   player = game.player

def _sanitize():
    # clear out/reset game and player variables
    current_game._variables.reset()
    player = None


def _write_data(data, filepath)
    import json
    json.dump(json.dumps(data), filepath)
    
def _load_data(self, filepath):
    import json
    return json.loads(json.load(filepath))
    
    
class Variables:
    __slots__ = '_items'
    

class Game:
    __slots__ = '_variables'
    def __init__(self, 
        self._variables =   Variables()
        
    @property
    def variables(self):
        """Access the variables for this game."""
        return self._variables
    
    def get_variable(self, v, fallback=None):
        """Return variable v if in variables else return fallback."""
        try:    return self._variables[v]
        except: return fallback
        
    def get_writable(self):
        """Return a new dict containing only the writable items."""
        import datetime
        self._variables[LAST_SAVE_TIME] = datetime.datetime.today()
        d = {
            'variables': self._variables
            'player': player._items()
            ## File comments ------------------- ##
            '_Comment': {
                'savetime': self._variables[LAST_SAVE_TIME]      
                }
            ## End file comments --------------- ##
            }
            
    def load_(self, filepath):
        x = _load_data(filepath)
        self._variables =   x['variables']
        self._player =      x['player']
        
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


# -- Player ------------------------------------------------------------------ #

from xsbc import OrderedDict

class Party(OrderedDict):
    __slots__ = OrderedDict.__slots__


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
        



