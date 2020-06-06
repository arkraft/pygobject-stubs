# encoding: utf-8
# module gi.repository.Poppler
# from /usr/lib64/girepository-1.0/Poppler-0.18.typelib
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
import gobject as __gobject


class Action(__gi.Boxed):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Poppler.Action """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    any = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    goto_dest = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    goto_remote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    javascript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    launch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    movie = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    named = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ocg_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    rendition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': gi.UnionInfo(Action), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerAction (94391898643696)>, '__dict__': <attribute '__dict__' of 'Action' objects>, '__weakref__': <attribute '__weakref__' of 'Action' objects>, '__doc__': None, 'type': <property object at 0x7f57e685b040>, 'any': <property object at 0x7f57e685b090>, 'goto_dest': <property object at 0x7f57e685b0e0>, 'goto_remote': <property object at 0x7f57e685b130>, 'launch': <property object at 0x7f57e685b220>, 'uri': <property object at 0x7f57e685b310>, 'named': <property object at 0x7f57e685b400>, 'movie': <property object at 0x7f57e685b4f0>, 'rendition': <property object at 0x7f57e685b5e0>, 'ocg_state': <property object at 0x7f57e685b6d0>, 'javascript': <property object at 0x7f57e685b7c0>, 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free)})"
    __gtype__ = None # (!) real value is '<GType PopplerAction (94391898643696)>'
    __info__ = gi.UnionInfo(Action)


