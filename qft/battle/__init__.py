
from game import player

class Battle:
    __slots__ = '_state', '_pp', '_pp_turns', '_ep', '_ep_turns'
    """Class for managing and handling battles."""
    def __init__(self, player_party, other_party):
        # setup battle stuff here
        self._state = -1 
        
        # player party
        self._pp = player_party
        self._pp_turns = [Turn(self, i for i in self._pp.chars]  

        
        # opposing party
        self._ep = other_party
        self._ep_turns = [Turn(self, i for i in self._ep.chars]

    def start(self):
        """Start the battle."""
        # do some pre start stuff
        player._in_battle = True    
        
        # set the started state
        self._state = 0   # (must call after pre start stuff) 
        # TODO call some start text here
        
        
    def has_ended(self):
        """True if this battle has ended."""
        return self._state > 0
        
    # evts
    def on_turn_end(self, index, n):
        if cant_fight(self._ep.chars):    # player wins
            self._state = 1  
            self.handler('Player Win')
        elif cant_fight(self._pp.chars):  # opponent wins
            self._state = 2  
            self.handler('Player Lose')
        else:   # no winner yet keep going
            pass
            # TODO
            #if n == 0   # player
            
            #else:       # opponent
                
            
    def handler(self, n):
        """
        Battle event handler. Events will call this automatically
            as needed.
        """
        return
        

class Turn:
    __slots__ = '_battle', '_char', '_action'
    """Special class for handling and storing turn actions."""
    def __init__(self, battle, char):
        self._battle =  battle
        self._char =    char
        self._action =  None
        
    def _can_do_action(self, action):
        if action == "Last":
            if (self._action == None or self.action.reqs_move) and not
                self._can_move(): return False
            return True
        elif action.reqs_move:
            if self._can_move(): return True
            return False
    
        
    def turn_choices(self):
        return
        
    def is_player_party(self):
        """True if this character is in the player's party."""
        return self in self._battle._p_turns
    
    def turn_start(self):
        available = []
        if self.is_player_party():
            if self._can_do_action("Last")   available.append("Last")
            pass
        else:
            if available:
                self._action = random.choice(available)
        
    def turn_end(self):
        self._battle.on_turn_end()
        
        
