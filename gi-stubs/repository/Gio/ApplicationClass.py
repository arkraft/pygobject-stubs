# encoding: utf-8
# module gi.repository.Gio
# from /usr/lib64/girepository-1.0/Gio-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


class ApplicationClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ApplicationClass()
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

    activate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    add_platform_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    after_emit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    before_emit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    command_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dbus_register = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dbus_unregister = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_local_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    local_command_line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_lost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    open = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quit_mainloop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run_mainloop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shutdown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    startup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ApplicationClass), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ApplicationClass' objects>, '__weakref__': <attribute '__weakref__' of 'ApplicationClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f4b8807ab80>, 'startup': <property object at 0x7f4b8807ac70>, 'activate': <property object at 0x7f4b8807ad60>, 'open': <property object at 0x7f4b8807ae50>, 'command_line': <property object at 0x7f4b8807af40>, 'local_command_line': <property object at 0x7f4b8808a0e0>, 'before_emit': <property object at 0x7f4b8808a1d0>, 'after_emit': <property object at 0x7f4b8808a2c0>, 'add_platform_data': <property object at 0x7f4b8808a400>, 'quit_mainloop': <property object at 0x7f4b8808a4f0>, 'run_mainloop': <property object at 0x7f4b8808a5e0>, 'shutdown': <property object at 0x7f4b8808a6d0>, 'dbus_register': <property object at 0x7f4b8808a7c0>, 'dbus_unregister': <property object at 0x7f4b8808a8b0>, 'handle_local_options': <property object at 0x7f4b8808a9f0>, 'name_lost': <property object at 0x7f4b8808aae0>, 'padding': <property object at 0x7f4b8808abd0>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ApplicationClass)


