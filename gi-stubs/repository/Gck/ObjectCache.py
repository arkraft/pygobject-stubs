# encoding: utf-8
# module gi.repository.Gck
# from /usr/lib64/girepository-1.0/Gck-1.typelib
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
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ObjectCache(__gobject.GInterface):
    # no doc
    def fill(self, attrs): # real signature unknown; restored from __doc__
        """ fill(self, attrs:Gck.Attributes) """
        pass

    def set_attributes(self, attrs=None): # real signature unknown; restored from __doc__
        """ set_attributes(self, attrs:Gck.Attributes=None) """
        pass

    def update(self, attr_types, cancellable=None): # real signature unknown; restored from __doc__
        """ update(self, attr_types:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def update_async(self, attr_types, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ update_async(self, attr_types:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def update_finish(self, result): # real signature unknown; restored from __doc__
        """ update_finish(self, result:Gio.AsyncResult) -> bool """
        return False

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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(ObjectCache), '__module__': 'gi.repository.Gck', '__gtype__': <GType GckObjectCache (94702128094048)>, '__dict__': <attribute '__dict__' of 'ObjectCache' objects>, '__weakref__': <attribute '__weakref__' of 'ObjectCache' objects>, '__doc__': None, '__gsignals__': {}, 'fill': gi.FunctionInfo(fill), 'set_attributes': gi.FunctionInfo(set_attributes), 'update': gi.FunctionInfo(update), 'update_async': gi.FunctionInfo(update_async), 'update_finish': gi.FunctionInfo(update_finish)})"
    __gdoc__ = 'Interface GckObjectCache\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GckObjectCache (94702128094048)>'
    __info__ = InterfaceInfo(ObjectCache)


