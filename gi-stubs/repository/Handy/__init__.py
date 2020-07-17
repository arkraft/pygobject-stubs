# encoding: utf-8
# module gi.repository.Handy
# from /usr/lib/x86_64-linux-gnu/girepository-1.0/Handy-1.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
import gi as __gi
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


# Variables with simple values

_namespace = 'Handy'

_version = '1'

__weakref__ = None

# functions

def ease_out_cubic(t): # real signature unknown; restored from __doc__
    """ ease_out_cubic(t:float) -> float """
    return 0.0

def enum_value_row_name(value, user_data=None): # real signature unknown; restored from __doc__
    """ enum_value_row_name(value:Handy.EnumValueObject, user_data=None) -> str """
    return ""

def get_enable_animations(widget): # real signature unknown; restored from __doc__
    """ get_enable_animations(widget:Gtk.Widget) -> bool """
    return False

def init(): # real signature unknown; restored from __doc__
    """ init() """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ default object formatter """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ helper for pickle """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ helper for pickle """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(): # real signature unknown; restored from __doc__
    """
    __sizeof__() -> int
    size of object in memory, in bytes
    """
    return 0

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .PreferencesRow import PreferencesRow
from .ActionRow import ActionRow
from .ActionRowClass import ActionRowClass
from .ApplicationWindow import ApplicationWindow
from .ApplicationWindowClass import ApplicationWindowClass
from .Avatar import Avatar
from .AvatarClass import AvatarClass
from .Swipeable import Swipeable
from .Carousel import Carousel
from .CarouselClass import CarouselClass
from .CarouselIndicatorStyle import CarouselIndicatorStyle
from .CenteringPolicy import CenteringPolicy
from .Clamp import Clamp
from .ClampClass import ClampClass
from .ComboRow import ComboRow
from .ComboRowClass import ComboRowClass
from .Deck import Deck
from .DeckClass import DeckClass
from .DeckTransitionType import DeckTransitionType
from .EnumValueObject import EnumValueObject
from .EnumValueObjectClass import EnumValueObjectClass
from .ExpanderRow import ExpanderRow
from .ExpanderRowClass import ExpanderRowClass
from .HeaderBar import HeaderBar
from .HeaderBarClass import HeaderBarClass
from .HeaderGroup import HeaderGroup
from .HeaderGroupClass import HeaderGroupClass
from .Keypad import Keypad
from .KeypadClass import KeypadClass
from .Leaflet import Leaflet
from .LeafletClass import LeafletClass
from .LeafletTransitionType import LeafletTransitionType
from .NavigationDirection import NavigationDirection
from .PreferencesGroup import PreferencesGroup
from .PreferencesGroupClass import PreferencesGroupClass
from .PreferencesPage import PreferencesPage
from .PreferencesPageClass import PreferencesPageClass
from .PreferencesRowClass import PreferencesRowClass
from .Window import Window
from .PreferencesWindow import PreferencesWindow
from .PreferencesWindowClass import PreferencesWindowClass
from .SearchBar import SearchBar
from .SearchBarClass import SearchBarClass
from .Squeezer import Squeezer
from .SqueezerClass import SqueezerClass
from .SqueezerTransitionType import SqueezerTransitionType
from .SwipeableInterface import SwipeableInterface
from .SwipeGroup import SwipeGroup
from .SwipeGroupClass import SwipeGroupClass
from .SwipeTracker import SwipeTracker
from .SwipeTrackerClass import SwipeTrackerClass
from .TitleBar import TitleBar
from .TitleBarClass import TitleBarClass
from .ValueObject import ValueObject
from .ValueObjectClass import ValueObjectClass
from .ViewSwitcher import ViewSwitcher
from .ViewSwitcherBar import ViewSwitcherBar
from .ViewSwitcherBarClass import ViewSwitcherBarClass
from .ViewSwitcherClass import ViewSwitcherClass
from .ViewSwitcherPolicy import ViewSwitcherPolicy
from .ViewSwitcherTitle import ViewSwitcherTitle
from .ViewSwitcherTitleClass import ViewSwitcherTitleClass
from .WindowClass import WindowClass
from .WindowHandle import WindowHandle
from .WindowHandleClass import WindowHandleClass
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f2ca1dcd4e0>'

__path__ = [
    '/usr/lib/x86_64-linux-gnu/girepository-1.0/Handy-1.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Handy', loader=<gi.importer.DynamicImporter object at 0x7f2ca1dcd4e0>)"

