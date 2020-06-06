# encoding: utf-8
# module gi.repository.Gegl
# from /usr/lib64/girepository-1.0/Gegl-0.4.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class ParamString(__gi_repository_GObject.ParamSpecString):
    """
    :Constructors:
    
    ::
    
        ParamString(**properties)
    """
    def do_finalize(self, *args, **kwargs): # real signature unknown
        """ finalize(self) """
        pass

    def do_values_cmp(self, *args, **kwargs): # real signature unknown
        """ values_cmp(self, value1:GObject.Value, value2:GObject.Value) -> int """
        pass

    def do_value_set_default(self, *args, **kwargs): # real signature unknown
        """ value_set_default(self, value:GObject.Value) """
        pass

    def do_value_validate(self, *args, **kwargs): # real signature unknown
        """ value_validate(self, value:GObject.Value) -> bool """
        pass

    def get_blurb(self): # real signature unknown; restored from __doc__
        """ get_blurb(self) -> str """
        return ""

    def get_default_value(self): # real signature unknown; restored from __doc__
        """ get_default_value(self) -> GObject.Value """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_name_quark(self): # real signature unknown; restored from __doc__
        """ get_name_quark(self) -> int """
        return 0

    def get_nick(self): # real signature unknown; restored from __doc__
        """ get_nick(self) -> str """
        return ""

    def get_qdata(self, quark): # real signature unknown; restored from __doc__
        """ get_qdata(self, quark:int) """
        pass

    def get_redirect_target(self): # real signature unknown; restored from __doc__
        """ get_redirect_target(self) -> GObject.ParamSpec """
        pass

    def set_qdata(self, quark, data=None): # real signature unknown; restored from __doc__
        """ set_qdata(self, quark:int, data=None) """
        pass

    def sink(self): # real signature unknown; restored from __doc__
        """ sink(self) """
        pass

    def steal_qdata(self, quark): # real signature unknown; restored from __doc__
        """ steal_qdata(self, quark:int) """
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    cset_first = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cset_nth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ensure_non_null = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    null_fold_if_empty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owner_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    param_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    substitutor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _blurb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ParamString), '__module__': 'gi.repository.Gegl', '__gtype__': <GType GeglParamString (94113950034992)>, '__doc__': None, '__gsignals__': {}})"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GeglParamString (94113950034992)>'
    __info__ = ObjectInfo(ParamString)


