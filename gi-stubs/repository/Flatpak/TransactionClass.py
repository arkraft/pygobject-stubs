# encoding: utf-8
# module gi.repository.Flatpak
# from /usr/lib64/girepository-1.0/Flatpak-1.0.typelib
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


class TransactionClass(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        TransactionClass()
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

    add_new_remote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    basic_auth_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    choose_remote_for_ref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_of_lifed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    end_of_lifed_with_rebase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    new_operation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    operation_done = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    operation_error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ready = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    run = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    webflow_done = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    webflow_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(TransactionClass), '__module__': 'gi.repository.Flatpak', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'TransactionClass' objects>, '__weakref__': <attribute '__weakref__' of 'TransactionClass' objects>, '__doc__': None, 'parent_class': <property object at 0x7f29534f1400>, 'new_operation': <property object at 0x7f29534f14f0>, 'operation_done': <property object at 0x7f29534f15e0>, 'operation_error': <property object at 0x7f29534f16d0>, 'choose_remote_for_ref': <property object at 0x7f29534f1810>, 'end_of_lifed': <property object at 0x7f29534f1900>, 'ready': <property object at 0x7f29534f19f0>, 'add_new_remote': <property object at 0x7f29534f1ae0>, 'run': <property object at 0x7f29534f1bd0>, 'end_of_lifed_with_rebase': <property object at 0x7f29534f1d10>, 'webflow_start': <property object at 0x7f29534f1e00>, 'webflow_done': <property object at 0x7f29534f1ef0>, 'basic_auth_start': <property object at 0x7f29534f3090>, 'padding': <property object at 0x7f29534f3180>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(TransactionClass)


