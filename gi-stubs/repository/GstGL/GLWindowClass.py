# encoding: utf-8
# module gi.repository.GstGL
# from /usr/lib64/girepository-1.0/GstGL-1.0.typelib
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
import gi.repository.Gst as __gi_repository_Gst
import gi.repository.GstBase as __gi_repository_GstBase
import gobject as __gobject


class GLWindowClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GLWindowClass()
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

    close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    controls_viewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_window_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    queue_resize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    send_message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    send_message_async = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_preferred_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_render_rectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_window_handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    show = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLWindowClass), '__module__': 'gi.repository.GstGL', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GLWindowClass' objects>, '__weakref__': <attribute '__weakref__' of 'GLWindowClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f56a3a3b4a0>, 'get_display': <property object at 0x7f56a3a3b590>, 'set_window_handle': <property object at 0x7f56a3a3b6d0>, 'get_window_handle': <property object at 0x7f56a3a3b7c0>, 'draw': <property object at 0x7f56a3a3b860>, 'run': <property object at 0x7f56a3a3b950>, 'quit': <property object at 0x7f56a3a3ba40>, 'send_message': <property object at 0x7f56a3a3bb30>, 'send_message_async': <property object at 0x7f56a3a3bc70>, 'open': <property object at 0x7f56a3a3bd10>, 'close': <property object at 0x7f56a3a3be00>, 'handle_events': <property object at 0x7f56a3a3bef0>, 'set_preferred_size': <property object at 0x7f56a3a3c090>, 'show': <property object at 0x7f56a3a3c130>, 'set_render_rectangle': <property object at 0x7f56a3a3c270>, 'queue_resize': <property object at 0x7f56a3a3c310>, 'controls_viewport': <property object at 0x7f56a3a3c450>, '_reserved': <property object at 0x7f56a3a3c4f0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GLWindowClass)


