# encoding: utf-8
# module gi.repository.UDisks
# from /usr/lib64/girepository-1.0/UDisks-2.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class PartitionIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        PartitionIface()
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

    get_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_is_contained = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_is_container = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_type_ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_delete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_resize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    handle_set_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(PartitionIface), '__module__': 'gi.repository.UDisks', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'PartitionIface' objects>, '__weakref__': <attribute '__weakref__' of 'PartitionIface' objects>, '__doc__': None, 'parent_iface': <property object at 0x7f13a806dd10>, 'handle_delete': <property object at 0x7f13a806de00>, 'handle_resize': <property object at 0x7f13a806def0>, 'handle_set_flags': <property object at 0x7f13a806f090>, 'handle_set_name': <property object at 0x7f13a806f180>, 'handle_set_type': <property object at 0x7f13a806f270>, 'get_flags': <property object at 0x7f13a806f360>, 'get_is_contained': <property object at 0x7f13a806f4a0>, 'get_is_container': <property object at 0x7f13a806f5e0>, 'get_name': <property object at 0x7f13a806f6d0>, 'get_number': <property object at 0x7f13a806f7c0>, 'get_offset': <property object at 0x7f13a806f8b0>, 'get_size': <property object at 0x7f13a806f9a0>, 'get_table': <property object at 0x7f13a806fa90>, 'get_type_': <property object at 0x7f13a806fb80>, 'get_uuid': <property object at 0x7f13a806fc20>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(PartitionIface)


