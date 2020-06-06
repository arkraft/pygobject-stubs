# encoding: utf-8
# module gi.repository.Atk
# from /usr/lib64/girepository-1.0/Atk-1.0.typelib
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


class HyperlinkClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        HyperlinkClass()
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

    get_end_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_n_anchors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_start_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_selected_link = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    link_activated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    link_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pad1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(HyperlinkClass), '__module__': 'gi.repository.Atk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'HyperlinkClass' objects>, '__weakref__': <attribute '__weakref__' of 'HyperlinkClass' objects>, '__doc__': None, 'parent': <property object at 0x7f44c6dac7c0>, 'get_uri': <property object at 0x7f44c6dac8b0>, 'get_object': <property object at 0x7f44c6dac9a0>, 'get_end_index': <property object at 0x7f44c6daca90>, 'get_start_index': <property object at 0x7f44c6dacb80>, 'is_valid': <property object at 0x7f44c6dacc70>, 'get_n_anchors': <property object at 0x7f44c6dacd60>, 'link_state': <property object at 0x7f44c6dace50>, 'is_selected_link': <property object at 0x7f44c6dacf90>, 'link_activated': <property object at 0x7f44c6dad090>, 'pad1': <property object at 0x7f44c6dad180>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(HyperlinkClass)


