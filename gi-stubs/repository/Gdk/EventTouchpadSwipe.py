# encoding: utf-8
# module gi.repository.Gdk
# from /usr/lib64/girepository-1.0/Gdk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class EventTouchpadSwipe(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        EventTouchpadSwipe()
    """
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

    dx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    n_fingers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    phase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    send_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x_root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y_root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(EventTouchpadSwipe), '__module__': 'gi.repository.Gdk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'EventTouchpadSwipe' objects>, '__weakref__': <attribute '__weakref__' of 'EventTouchpadSwipe' objects>, '__doc__': None, 'type': <property object at 0x7f1e11c65270>, 'window': <property object at 0x7f1e11c65360>, 'send_event': <property object at 0x7f1e11c65450>, 'phase': <property object at 0x7f1e11c65540>, 'n_fingers': <property object at 0x7f1e11c65630>, 'time': <property object at 0x7f1e11c65720>, 'x': <property object at 0x7f1e11c65810>, 'y': <property object at 0x7f1e11c65900>, 'dx': <property object at 0x7f1e11c659f0>, 'dy': <property object at 0x7f1e11c65ae0>, 'x_root': <property object at 0x7f1e11c65bd0>, 'y_root': <property object at 0x7f1e11c65cc0>, 'state': <property object at 0x7f1e11c65db0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(EventTouchpadSwipe)


