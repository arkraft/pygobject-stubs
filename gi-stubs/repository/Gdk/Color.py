# encoding: utf-8
# module gi.repository.Gdk
# from /usr/lib64/girepository-1.0/Gdk-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .Color import Color

class Color(Color):
    """
    :Constructors:
    
    ::
    
        Color()
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gdk.Color """
        pass

    def equal(self, colorb): # real signature unknown; restored from __doc__
        """ equal(self, colorb:Gdk.Color) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def from_floats(red, green, blue): # reliably restored by inspect
        """ Return a new Color object from red/green/blue values from 0.0 to 1.0. """
        pass

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def parse(self, spec): # real signature unknown; restored from __doc__
        """ parse(spec:str) -> bool, color:Gdk.Color """
        return False

    def to_floats(self): # reliably restored by inspect
        """ Return (red_float, green_float, blue_float) triple. """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self, red, green, blue): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    blue_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    green_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pixel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    red_float = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    MAX_VALUE = 65535
    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gdk', 'MAX_VALUE': 65535, '__init__': <function Color.__init__ at 0x7fbaf87ed430>, '__eq__': <function Color.__eq__ at 0x7fbaf87ed3a0>, '__repr__': <function Color.__repr__ at 0x7fbaf87ed550>, 'red_float': <property object at 0x7fbaf87f6f90>, 'green_float': <property object at 0x7fbaf87f8040>, 'blue_float': <property object at 0x7fbaf87f8090>, 'to_floats': <function Color.to_floats at 0x7fbaf87ed940>, 'from_floats': <staticmethod object at 0x7fbaf95978b0>, '__doc__': None, '__hash__': None})"
    __gtype__ = None # (!) real value is '<GType GdkColor (94915768168288)>'
    __hash__ = None
    __info__ = StructInfo(Color)


