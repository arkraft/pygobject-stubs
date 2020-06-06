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


class ParamSpecInt(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ParamSpecInt()
    """
    def set_steps(self, small_step, big_step): # real signature unknown; restored from __doc__
        """ set_steps(self, small_step:int, big_step:int) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ui_gamma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ui_maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ui_minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ui_step_big = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ui_step_small = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ParamSpecInt), '__module__': 'gi.repository.Gegl', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ParamSpecInt' objects>, '__weakref__': <attribute '__weakref__' of 'ParamSpecInt' objects>, '__doc__': None, 'parent_instance': <property object at 0x7f72398b2450>, 'ui_minimum': <property object at 0x7f72398b2540>, 'ui_maximum': <property object at 0x7f72398b2630>, 'ui_gamma': <property object at 0x7f72398b2720>, 'ui_step_small': <property object at 0x7f72398b2810>, 'ui_step_big': <property object at 0x7f72398b2900>, 'set_steps': gi.FunctionInfo(set_steps)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ParamSpecInt)


