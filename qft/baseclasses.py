

# ---------------------------------------------------------------------------- #
#                                                                              #
#     This program is free software: you can redistribute it and/or modify     #
#     it under the terms of the GNU General Public License as published by     #
#     the Free Software Foundation, either version 3 of the License, or        #
#     (at your option) any later version.                                      #
#                                                                              #
#     This program is distributed in the hope that it will be useful,          #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the             #
#     GNU General Public License for more details.                             #
#                                                                              #
#     You should have received a copy of the GNU General Public License        #
#     along with this program. If not, see <http://www.gnu.org/licenses/>.     #
#                                                                              #
# ---------------------------------------------------------------------------- #

from xsbc.storio import Storio

#from ccodes import CCODES_CONFIG
#from codes import *
    
    
class _SB(Storio.Mixin):
    # Shortcut for classes using StorageHandlerMixin 
    #   in the case we don't have any __init__ args
    # __init__ is already defined
    # (if using slots) we can use __slots__ = _SB.__slots__
    #   instead of __slots__ = StorageHandlerMixIn.__slots__
    __slots__ = StorageHandlerMixIn.__slots__
    def __init__(self):
        self._storio_init()

