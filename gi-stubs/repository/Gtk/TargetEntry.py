# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class TargetEntry(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        TargetEntry()
        new(target:str, flags:int, info:int) -> Gtk.TargetEntry
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Gtk.TargetEntry """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def new(self, target, flags, info): # real signature unknown; restored from __doc__
        """ new(target:str, flags:int, info:int) -> Gtk.TargetEntry """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TargetEntry), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkTargetEntry (94846038548048)>, '__dict__': <attribute '__dict__' of 'TargetEntry' objects>, '__weakref__': <attribute '__weakref__' of 'TargetEntry' objects>, '__doc__': None, 'target': <property object at 0x7fe830f830e0>, 'flags': <property object at 0x7fe830f831d0>, 'info': <property object at 0x7fe830f832c0>, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free)})"
    __gtype__ = None # (!) real value is '<GType GtkTargetEntry (94846038548048)>'
    __info__ = StructInfo(TargetEntry)


