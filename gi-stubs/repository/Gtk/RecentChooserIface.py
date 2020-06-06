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


class RecentChooserIface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RecentChooserIface()
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

    add_filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    base_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_current_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_recent_manager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    item_activated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    list_filters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    remove_filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    selection_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    select_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    select_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_current_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    set_sort_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unselect_all = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unselect_uri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RecentChooserIface), '__module__': 'gi.repository.Gtk', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RecentChooserIface' objects>, '__weakref__': <attribute '__weakref__' of 'RecentChooserIface' objects>, '__doc__': None, 'base_iface': <property object at 0x7fc63a6cc860>, 'set_current_uri': <property object at 0x7fc63a6cc950>, 'get_current_uri': <property object at 0x7fc63a6cca40>, 'select_uri': <property object at 0x7fc63a6ccb30>, 'unselect_uri': <property object at 0x7fc63a6ccc20>, 'select_all': <property object at 0x7fc63a6ccd10>, 'unselect_all': <property object at 0x7fc63a6cce00>, 'get_items': <property object at 0x7fc63a6ccef0>, 'get_recent_manager': <property object at 0x7fc63a6cd090>, 'add_filter': <property object at 0x7fc63a6cd180>, 'remove_filter': <property object at 0x7fc63a6cd270>, 'list_filters': <property object at 0x7fc63a6cd360>, 'set_sort_func': <property object at 0x7fc63a6cd450>, 'item_activated': <property object at 0x7fc63a6cd540>, 'selection_changed': <property object at 0x7fc63a6cd680>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RecentChooserIface)


