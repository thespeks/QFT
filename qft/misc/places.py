


BAR =               'Bar'
STRIP_CLUB =        'Strip Bar'
BROTHEL =           'Brothel'
MASSAGE_PARLOR =    'Massage Parlor'  # massage skill

# Shop Types
SHOP =              'Shop'
REPAIR_SHOP =       'Repair Shop'   
PAWN_SHOP =         'Pawn Shop'     
LOCK_SMITH =        'Lock Smith'    # locksmith skill
WEAPON_SMITH =      'Weapon Smith'

# Entertainment
THEATRE =           'Theatre'

# 
LIBRARY =           'Library'   
GARDEN =            'Garden'    
PARK =              'Park'      

HOSPITAL =          'Hospital'  # get healed here
PHARMACY =          'Pharmacy'  # get medicines here


CLUB =              'Club'
SPA =               'Spa'
GYM =               'Gym'



    
class Place:
    _type = ""
    
    
class Bar(Place):
    _subtype = BAR
    
class StripClub(Place):
    _subtype = STRIP_CLUB
    
class Brothel(Place):
    _subtype = BROTHEL
    
class MassageParlor(Place):
    _subtype = MASSAGE_PARLOR
    
class Hospital(Place):
    _subtype = HOSPITAL
    
class Theatre(Place):
    _subtype = THEATRE
    


class Garden(Place):
    _subtype = GARDEN
    
class Park(Place):
    _subtype = PARK
    
    
# Clubs
class Club(Place):
    _type =     CLUB  
  
  
class Spa(Club):
    _subtype = SPA
    
class Gym(Club):
    _subtype = GYM
    
    
    
class Library(Place):
    _subtype = LIBRARY
    

# Shops
class Shop(Place):
    _type = SHOP
    
class PawnShop(Shop):
    _subtype = PAWN_SHOP

class Pharmacy(Shop):
    _subtype = PHAMRACY
    
class Repair(Shop):
    _subtype = REPAIR_SHOP
    
class LockSmith(Shop):
    _subtype = LOCK_SMITH
    
class WeaponSmith(Shop):
    _subtype = WEAPON_SMITH
    
    

