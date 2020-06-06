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


class LayersIter(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(document:Poppler.Document) -> Poppler.LayersIter
    """
    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> Poppler.LayersIter """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_child(self): # real signature unknown; restored from __doc__
        """ get_child(self) -> Poppler.LayersIter """
        pass

    def get_layer(self): # real signature unknown; restored from __doc__
        """ get_layer(self) -> Poppler.Layer """
        pass

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
        return ""

    def new(self, document): # real signature unknown; restored from __doc__
        """ new(document:Poppler.Document) -> Poppler.LayersIter """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> bool """
        return False

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

    def __init__(*args, **kwargs): # reliably restored by inspect
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
        """ new(document:Poppler.Document) -> Poppler.LayersIter """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(LayersIter), '__module__': 'gi.repository.Poppler', '__gtype__': <GType PopplerLayersIter (94391899100848)>, '__dict__': <attribute '__dict__' of 'LayersIter' objects>, '__weakref__': <attribute '__weakref__' of 'LayersIter' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'copy': gi.FunctionInfo(copy), 'free': gi.FunctionInfo(free), 'get_child': gi.FunctionInfo(get_child), 'get_layer': gi.FunctionInfo(get_layer), 'get_title': gi.FunctionInfo(get_title), 'next': gi.FunctionInfo(next), '__new__': <staticmethod object at 0x7f57e5e6a250>, '__init__': <function nothing at 0x7f57e6a9aee0>})"
    __gtype__ = None # (!) real value is '<GType PopplerLayersIter (94391899100848)>'
    __info__ = StructInfo(LayersIter)


