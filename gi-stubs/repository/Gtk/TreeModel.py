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


from .TreeModel import TreeModel

class TreeModel(TreeModel):
    # no doc
    def filter_new(self, root=None): # real signature unknown; restored from __doc__
        """ filter_new(self, root:Gtk.TreePath=None) -> Gtk.TreeModel """
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gtk.TreeModelForeachFunc, user_data=None) """
        pass

    def get(self, treeiter, *columns): # reliably restored by inspect
        # no doc
        pass

    def get_column_type(self, index_): # real signature unknown; restored from __doc__
        """ get_column_type(self, index_:int) -> GType """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gtk.TreeModelFlags """
        pass

    def get_iter(self, path): # reliably restored by inspect
        # no doc
        pass

    def get_iter_first(*args, **kwargs): # reliably restored by inspect
        """ get_iter_first(self) -> bool, iter:Gtk.TreeIter """
        pass

    def get_iter_from_string(*args, **kwargs): # reliably restored by inspect
        """ get_iter_from_string(self, path_string:str) -> bool, iter:Gtk.TreeIter """
        pass

    def get_n_columns(self): # real signature unknown; restored from __doc__
        """ get_n_columns(self) -> int """
        return 0

    def get_path(self, iter): # real signature unknown; restored from __doc__
        """ get_path(self, iter:Gtk.TreeIter) -> Gtk.TreePath """
        pass

    def get_string_from_iter(self, iter): # real signature unknown; restored from __doc__
        """ get_string_from_iter(self, iter:Gtk.TreeIter) -> str """
        return ""

    def get_value(self, iter, column): # real signature unknown; restored from __doc__
        """ get_value(self, iter:Gtk.TreeIter, column:int) -> value:GObject.Value """
        pass

    def iter_children(*args, **kwargs): # reliably restored by inspect
        """ iter_children(self, parent:Gtk.TreeIter=None) -> bool, iter:Gtk.TreeIter """
        pass

    def iter_has_child(self, iter): # real signature unknown; restored from __doc__
        """ iter_has_child(self, iter:Gtk.TreeIter) -> bool """
        return False

    def iter_next(self, aiter): # reliably restored by inspect
        # no doc
        pass

    def iter_nth_child(*args, **kwargs): # reliably restored by inspect
        """ iter_nth_child(self, parent:Gtk.TreeIter=None, n:int) -> bool, iter:Gtk.TreeIter """
        pass

    def iter_n_children(self, iter=None): # real signature unknown; restored from __doc__
        """ iter_n_children(self, iter:Gtk.TreeIter=None) -> int """
        return 0

    def iter_parent(*args, **kwargs): # reliably restored by inspect
        """ iter_parent(self, child:Gtk.TreeIter) -> bool, iter:Gtk.TreeIter """
        pass

    def iter_previous(self, aiter): # reliably restored by inspect
        # no doc
        pass

    def ref_node(self, iter): # real signature unknown; restored from __doc__
        """ ref_node(self, iter:Gtk.TreeIter) """
        pass

    def rows_reordered(self, path, iter, new_order): # reliably restored by inspect
        # no doc
        pass

    def row_changed(self, path, iter): # reliably restored by inspect
        # no doc
        pass

    def row_deleted(self, path): # reliably restored by inspect
        # no doc
        pass

    def row_has_child_toggled(self, path, iter): # reliably restored by inspect
        # no doc
        pass

    def row_inserted(self, path, iter): # reliably restored by inspect
        # no doc
        pass

    def set_row(self, treeiter, row): # reliably restored by inspect
        # no doc
        pass

    def sort_new_with_model(self): # reliably restored by inspect
        # no doc
        pass

    def unref_node(self, iter): # real signature unknown; restored from __doc__
        """ unref_node(self, iter:Gtk.TreeIter) """
        pass

    def _coerce_path(self, path): # reliably restored by inspect
        # no doc
        pass

    def _convert_row(self, row): # reliably restored by inspect
        # no doc
        pass

    def _convert_value(self, column, value): # reliably restored by inspect
        """ Convert value to a GObject.Value of the expected type """
        pass

    def _getiter(self, key): # reliably restored by inspect
        # no doc
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __delitem__(self, key): # reliably restored by inspect
        # no doc
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

    def __getitem__(self, key): # reliably restored by inspect
        # no doc
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

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __len__(self): # reliably restored by inspect
        # no doc
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

    def __nonzero__(self): # reliably restored by inspect
        # no doc
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

    def __setitem__(self, key, value): # reliably restored by inspect
        # no doc
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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.overrides.Gtk', '__len__': <function TreeModel.__len__ at 0x7fc63a945b80>, '__bool__': <function TreeModel.__bool__ at 0x7fc63a945c10>, '__nonzero__': <function TreeModel.__bool__ at 0x7fc63a945c10>, '_getiter': <function TreeModel._getiter at 0x7fc63a945ca0>, 'sort_new_with_model': <function TreeModel.sort_new_with_model at 0x7fc63a945d30>, '_coerce_path': <function TreeModel._coerce_path at 0x7fc63a945dc0>, '__getitem__': <function TreeModel.__getitem__ at 0x7fc63a945e50>, '__setitem__': <function TreeModel.__setitem__ at 0x7fc63a945ee0>, '__delitem__': <function TreeModel.__delitem__ at 0x7fc63a945f70>, '__iter__': <function TreeModel.__iter__ at 0x7fc63a960040>, 'get_iter_first': <function strip_boolean_result.<locals>.wrapped at 0x7fc63a9600d0>, 'iter_children': <function strip_boolean_result.<locals>.wrapped at 0x7fc63a960160>, 'iter_nth_child': <function strip_boolean_result.<locals>.wrapped at 0x7fc63a9601f0>, 'iter_parent': <function strip_boolean_result.<locals>.wrapped at 0x7fc63a960310>, 'get_iter_from_string': <function strip_boolean_result.<locals>.wrapped at 0x7fc63a9603a0>, 'get_iter': <function TreeModel.get_iter at 0x7fc63a960430>, 'iter_next': <function TreeModel.iter_next at 0x7fc63a9604c0>, 'iter_previous': <function TreeModel.iter_previous at 0x7fc63a960550>, '_convert_row': <function TreeModel._convert_row at 0x7fc63a9605e0>, 'set_row': <function TreeModel.set_row at 0x7fc63a960670>, '_convert_value': <function TreeModel._convert_value at 0x7fc63a960700>, 'get': <function TreeModel.get at 0x7fc63a960790>, 'row_changed': <function TreeModel.row_changed at 0x7fc63a960820>, 'row_inserted': <function TreeModel.row_inserted at 0x7fc63a9608b0>, 'row_has_child_toggled': <function TreeModel.row_has_child_toggled at 0x7fc63a960940>, 'row_deleted': <function TreeModel.row_deleted at 0x7fc63a9609d0>, 'rows_reordered': <function TreeModel.rows_reordered at 0x7fc63a960a60>, '__doc__': None, '__gsignals__': {}})"
    __gdoc__ = 'Interface GtkTreeModel\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkTreeModel (93897367200688)>'
    __info__ = InterfaceInfo(TreeModel)


