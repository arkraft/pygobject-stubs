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


from .TreeSortable import TreeSortable

class TreeSortable(TreeSortable):
    # no doc
    def get_sort_column_id(*args, **kwargs): # reliably restored by inspect
        """ get_sort_column_id(self) -> bool, sort_column_id:int, order:Gtk.SortType """
        pass

    def has_default_sort_func(self): # real signature unknown; restored from __doc__
        """ has_default_sort_func(self) -> bool """
        return False

    def set_default_sort_func(self, sort_func, user_data=None): # reliably restored by inspect
        # no doc
        pass

    def set_sort_column_id(self, sort_column_id, order): # real signature unknown; restored from __doc__
        """ set_sort_column_id(self, sort_column_id:int, order:Gtk.SortType) """
        pass

    def set_sort_func(self, sort_column_id, sort_func, user_data=None): # reliably restored by inspect
        # no doc
        pass

    def sort_column_changed(self): # real signature unknown; restored from __doc__
        """ sort_column_changed(self) """
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', 'get_sort_column_id': <function strip_boolean_result.<locals>.wrapped at 0x7fc63a960af0>, 'set_sort_func': <function TreeSortable.set_sort_func at 0x7fc63a960b80>, 'set_default_sort_func': <function TreeSortable.set_default_sort_func at 0x7fc63a960c10>, '__doc__': None, '__gsignals__': {}})"
    __gdoc__ = 'Interface GtkTreeSortable\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkTreeSortable (93897367207680)>'
    __info__ = InterfaceInfo(TreeSortable)


