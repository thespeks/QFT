


class RaceBase:
    _name =       ""
    _eye_colors = ()
    _hair_colors = ()
    _min_max_height = ()
    _skin_colors =  ()
    _fur_colors = ()
    
    @property
    def race_name(self):
        return self.name
    
    def get_eye_colors(self):
        """Return normal eye colors for this race."""
        return self._eye_colors
        
    def get_hair_colors(self):
        """Return normal hair colors for this race."""
        return self._hair_colors
        
        
        
class Faline(RaceBase):
    _name =           RACE_FALINE
    _eye_colors =     (LIGHT_BLUE, YELLOW_ORANGE, OLIVE, CHARCOAL, GREEN, BROWN)
    _hair_colors =    (BLACK, BROWN, DARK_BROWN, LIGHT_BROWN, GRAY, CHARCOAL, LIGHT_GRAY, BLOND, REDISH_BROWN)
    _min_max_height = (36, 66)  # 3 to 5.5 ft
    _fur_colors =     (BROWN, DULL_BROWN, GRAY, CHARCOAL, LIGHT_GRAY)


class Vulpin(RaceBase):
    _name =           RACE_VULPIN
    _eye_colors =     (GREY, ORANGE, YELLOW_ORANGE, OLIVE, YELLOW_GREEN, DARK_GREEN, BROWN) 
    _hair_colors =    (BLACK, BROWN, DARK_BROWN, LIGHT_BROWN, GRAY, CHARCOAL, LIGHT_GRAY, BLOND, REDISH_BROWN)
    _min_max_height = (36, 66)
    _fur_colors =     (REDISH_BROWN, REDISH_ORANGE, BROWN)


class Klolven(RaceBase):
    _name =           RACE_KLOVEN

class Nekoma(RaceBase):
    _name =           RACE_NEKOMA
    _eye_colors =     (LIGHT_BLUE, YELLOW_ORANGE, OLIVE, CHARCOAL, GREEN, BROWN)
    _hair_colors =    (BLACK, BROWN, DARK_BROWN, LIGHT_BROWN, GRAY, CHARCOAL, LIGHT_GRAY, BLOND, REDISH_BROWN)
    _skin_colors =    (PALE, LIGHT, DARK)
    
    # _legfur, _armfur, _tail colors will be the same as hair color


class Faliphae(RaceBase):
    # faline-fae hybrid
    _name =           RACE_FALIPHAE
    _eye_colors =     (LIGHT_BLUE, LIGHT_BLUEGREEN, LIGHT_PURPLE, LIGHT_PINK, LIGHT_GRAY)
    _hair_colors =    _eyecolors
    _min_max_height = (12, 36)
    
    
class Vulphae(RaceBase):
    # vulpin-fae hybrid
    _name =           RACE_VULPHAE
    _eye_colors =     (BRIGHT_BLUE, BRIGHT_PURPLE, BRIGHT_GREEN, BRIGHT_ORANGE, BRIGHT_BLUEGREEN, BRIGHT_OLIVE)
    _hair_colors =    _eye_colors
    _min_max_height = (12, 36)
    
    
