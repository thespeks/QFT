from qft import QFTObj
    
    
class _Loc:
    __slots__ = ()
    
    def __call__(self):         return self.reg, self.sector, self.x, self.y
    def __iter__(self):         return iter(self.__call__())
    def __contains__(self, i):  return i in self.__call__()
    def __len__(self):          return 4
    def __reversed__(self):     return reversed(self.__call__())
    
    def __str__(self):          
        return "{} {} {},{}".format(self.reg, self.sector, self.x, self.y)
    __repr__ = __str__
    
    # add/sub for getting adjacent cells
    def __add__(self, n):   return self.x + n[0], self.y + n[1]
    __radd__ = __add__
    
    def __sub__(self, n):   return self.x - n[0], self.y - n[1]
    def __rsub__(self, n):  return n[0] - self.x, n[1] - self.y
    
    # char._loc to cell._loc comparison
    def __eq__(self, x):
        try:    return tuple(self) == tuple(x)
        except: return False
    
    def __ne__(self, x):
        try:    return tuple(self) != tuple(x)
        except: return False
    
    
class Region:
    """Region base class."""
    __slots__ = '_name', '_maps'
    def __init__(self, name, maps):
        self._name = name
        self._maps = maps
        
    @property
    def name(self):
        """The name of this region."""
        return self._name    
        
    
class Sector(QFTObj):
    """Region 'sector' base class."""
    __slots__ = '_region', '_cells', '_subtype'
    def __init__(self, cells, region, subtype):
        self._region = region
        self._cells = cells
        self._subtype = subtype
        
    @property
    def region(self):
        """The region this sector is in."""
        return self._region
        
    @property
    def subtype(self):
        """The subtype of this sector."""
        return self._subtype
        
        
class Cell:
    """Sector 'cell' base class."""
    __slots__ = '_sector', '_loc'
    def __init__(self, sector):
        self._sector = sector
        
    _loc = CellLocation(self, code)
    
    @property
    def location(self):
        """The location of this cell."""
        return self._loc

    @property
    def sector(self):
        """The sector this cell is in."""
        return self._sector
        
    @property
    def position(self):
        """The x,y position of this cell in the sector."""
        return self._loc.pos
    pos = position

        
    class CellLocation(_Loc):
        """
        Cell location class. 
            Used to comapre cell location data with other object location data.
        """
        __slots__ = '_parent'
        def __init__(self, parent, pos):
            self._parent =  parent
            self._pos =     pos

        def __getitem__(self, i):   return tuple(iter(self))[i]

        @property
        def region(self):
            # cell.location.region
            return self._parent.sector.region

        @property
        def sector(self):
            """The sector this cell is in."""
            return self._parent._sector

        @property
        def position(self):
            """The x,y position of this cell."""
            return self._pos
        pos = position

        @property
        def x(self):
            """The x position of this cell."""
            return self._pos[0]
        
        @property
        def y(self):
            """The y position of this cell."""
            return self._pos[1]
            
            
