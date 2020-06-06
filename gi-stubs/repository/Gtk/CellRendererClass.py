# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-2.0.typelib
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


class CellRendererClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        CellRendererClass()
    """
    def set_accessible_type(self, type): # real signature unknown; restored from __doc__
        """ set_accessible_type(self, type:GType) """
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

    activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    editing_canceled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    editing_started = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_aligned_area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_height_for_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_preferred_width_for_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_request_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    render = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    start_editing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _gtk_reserved4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(CellRendererClass), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'CellRendererClass' objects>, '__weakref__': <attribute '__weakref__' of 'CellRendererClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7fc63a7d7720>, 'get_request_mode': <property object at 0x7fc63a7d7860>, 'get_preferred_width': <property object at 0x7fc63a7d7950>, 'get_preferred_height_for_width': <property object at 0x7fc63a7d7a40>, 'get_preferred_height': <property object at 0x7fc63a7d7b30>, 'get_preferred_width_for_height': <property object at 0x7fc63a7d7c20>, 'get_aligned_area': <property object at 0x7fc63a7d7d10>, 'get_size': <property object at 0x7fc63a7d7db0>, 'render': <property object at 0x7fc63a7d7ea0>, 'activate': <property object at 0x7fc63a7d7f90>, 'start_editing': <property object at 0x7fc63a7d90e0>, 'editing_canceled': <property object at 0x7fc63a7d9220>, 'editing_started': <property object at 0x7fc63a7d9310>, 'priv': <property object at 0x7fc63a7d9400>, '_gtk_reserved2': <property object at 0x7fc63a7d94f0>, '_gtk_reserved3': <property object at 0x7fc63a7d95e0>, '_gtk_reserved4': <property object at 0x7fc63a7d96d0>, 'set_accessible_type': gi.FunctionInfo(set_accessible_type)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(CellRendererClass)


