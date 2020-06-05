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


class BindingSet(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        BindingSet()
    """
    def activate(self, keyval, modifiers, p_object): # real signature unknown; restored from __doc__
        """ activate(self, keyval:int, modifiers:Gdk.ModifierType, object:GObject.Object) -> bool """
        return False

    def add_path(self, path_type, path_pattern, priority): # real signature unknown; restored from __doc__
        """ add_path(self, path_type:Gtk.PathType, path_pattern:str, priority:Gtk.PathPriorityType) """
        pass

    def find(self, set_name): # real signature unknown; restored from __doc__
        """ find(set_name:str) -> Gtk.BindingSet or None """
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

    class_branch_pspecs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    widget_class_pspecs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    widget_path_pspecs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(BindingSet), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'BindingSet' objects>, '__weakref__': <attribute '__weakref__' of 'BindingSet' objects>, '__doc__': None, 'set_name': <property object at 0x7fe8310a1590>, 'priority': <property object at 0x7fe8310a1680>, 'widget_path_pspecs': <property object at 0x7fe8310a17c0>, 'widget_class_pspecs': <property object at 0x7fe8310a1900>, 'class_branch_pspecs': <property object at 0x7fe8310a1a40>, 'entries': <property object at 0x7fe8310a1b30>, 'current': <property object at 0x7fe8310a1c20>, 'parsed': <property object at 0x7fe8310a1d10>, 'activate': gi.FunctionInfo(activate), 'add_path': gi.FunctionInfo(add_path), 'find': gi.FunctionInfo(find)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(BindingSet)


