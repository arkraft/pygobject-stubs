# encoding: utf-8
# module gi.repository.GcrUi
# from /usr/lib64/girepository-1.0/GcrUi-3.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gcr as __gi_repository_Gcr
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class CollectionModel(__gi_overrides_GObject.Object, __gi_overrides_Gtk.TreeModel, __gi_overrides_Gtk.TreeSortable):
    """
    :Constructors:
    
    ::
    
        CollectionModel(**properties)
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_selected(self, iter, selected): # real signature unknown; restored from __doc__
        """ change_selected(self, iter:Gtk.TreeIter, selected:bool) """
        pass

    def column_for_selected(self): # real signature unknown; restored from __doc__
        """ column_for_selected(self) -> int """
        return 0

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_after(self, *args, **kwargs): # real signature unknown
        pass

    def connect_data(self, detailed_signal, handler, *data, **kwargs): # reliably restored by inspect
        """
        Connect a callback to the given signal with optional user data.
        
                :param str detailed_signal:
                    A detailed signal to connect to.
                :param callable handler:
                    Callback handler to connect to the signal.
                :param *data:
                    Variable data which is passed through to the signal handler.
                :param GObject.ConnectFlags connect_flags:
                    Flags used for connection options.
                :returns:
                    A signal id which can be used with disconnect.
        """
        pass

    def connect_object(self, *args, **kwargs): # real signature unknown
        pass

    def connect_object_after(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def filter_new(self, root=None): # real signature unknown; restored from __doc__
        """ filter_new(self, root:Gtk.TreePath=None) -> Gtk.TreeModel """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, func:Gtk.TreeModelForeachFunc, user_data=None) """
        pass

    def freeze_notify(self): # reliably restored by inspect
        """
        Freezes the object's property-changed notification queue.
        
                :returns:
                    A context manager which optionally can be used to
                    automatically thaw notifications.
        
                This will freeze the object so that "notify" signals are blocked until
                the thaw_notify() method is called.
        
                .. code-block:: python
        
                    with obj.freeze_notify():
                        pass
        """
        pass

    def get(self, treeiter, *columns): # reliably restored by inspect
        # no doc
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_collection(self): # real signature unknown; restored from __doc__
        """ get_collection(self) -> Gcr.Collection """
        pass

    def get_column_type(self, index_): # real signature unknown; restored from __doc__
        """ get_column_type(self, index_:int) -> GType """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_selected_objects(self): # real signature unknown; restored from __doc__
        """ get_selected_objects(self) -> list """
        return []

    def get_sort_column_id(*args, **kwargs): # reliably restored by inspect
        """ get_sort_column_id(self) -> bool, sort_column_id:int, order:Gtk.SortType """
        pass

    def get_string_from_iter(self, iter): # real signature unknown; restored from __doc__
        """ get_string_from_iter(self, iter:Gtk.TreeIter) -> str """
        return ""

    def get_value(self, iter, column): # real signature unknown; restored from __doc__
        """ get_value(self, iter:Gtk.TreeIter, column:int) -> value:GObject.Value """
        pass

    def handler_block(obj, handler_id): # reliably restored by inspect
        """
        Blocks the signal handler from being invoked until
            handler_unblock() is called.
        
            :param GObject.Object obj:
                Object instance to block handlers for.
            :param int handler_id:
                Id of signal to block.
            :returns:
                A context manager which optionally can be used to
                automatically unblock the handler:
        
            .. code-block:: python
        
                with GObject.signal_handler_block(obj, id):
                    pass
        """
        pass

    def handler_block_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def handler_disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_is_connected(instance:GObject.Object, handler_id:int) -> bool """
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_unblock(instance:GObject.Object, handler_id:int) """
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def has_default_sort_func(self): # real signature unknown; restored from __doc__
        """ has_default_sort_func(self) -> bool """
        return False

    def install_properties(self, pspecs): # real signature unknown; restored from __doc__
        """ install_properties(self, pspecs:list) """
        pass

    def install_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_property(self, property_id:int, pspec:GObject.ParamSpec) """
        pass

    def interface_find_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_install_property(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def interface_list_properties(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_selected(self, iter): # real signature unknown; restored from __doc__
        """ is_selected(self, iter:Gtk.TreeIter) -> bool """
        return False

    def iter_children(*args, **kwargs): # reliably restored by inspect
        """ iter_children(self, parent:Gtk.TreeIter=None) -> bool, iter:Gtk.TreeIter """
        pass

    def iter_for_object(self, p_object, iter): # real signature unknown; restored from __doc__
        """ iter_for_object(self, object:GObject.Object, iter:Gtk.TreeIter) -> bool """
        return False

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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def object_for_iter(self, iter): # real signature unknown; restored from __doc__
        """ object_for_iter(self, iter:Gtk.TreeIter) -> GObject.Object """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_node(self, iter): # real signature unknown; restored from __doc__
        """ ref_node(self, iter:Gtk.TreeIter) """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_collection(self, collection=None): # real signature unknown; restored from __doc__
        """ set_collection(self, collection:Gcr.Collection=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_sort_func(self, sort_func, user_data=None): # reliably restored by inspect
        # no doc
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_row(self, treeiter, row): # reliably restored by inspect
        # no doc
        pass

    def set_selected_objects(self, selected): # real signature unknown; restored from __doc__
        """ set_selected_objects(self, selected:list) """
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

    def sort_new_with_model(self): # reliably restored by inspect
        # no doc
        pass

    def steal_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def steal_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def stop_emission(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def stop_emission_by_name(*args, **kwargs): # reliably restored by inspect
        """ signal_stop_emission_by_name(instance:GObject.Object, detailed_signal:str) """
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def toggle_selected(self, iter): # real signature unknown; restored from __doc__
        """ toggle_selected(self, iter:Gtk.TreeIter) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unref_node(self, iter): # real signature unknown; restored from __doc__
        """ unref_node(self, iter:Gtk.TreeIter) """
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
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

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
        pass

    def _getiter(self, key): # reliably restored by inspect
        # no doc
        pass

    def _ref(self, *args, **kwargs): # real signature unknown
        """ ref(self) -> GObject.Object """
        pass

    def _ref_sink(self, *args, **kwargs): # real signature unknown
        """ ref_sink(self) -> GObject.Object """
        pass

    def _unref(self, *args, **kwargs): # real signature unknown
        """ unref(self) """
        pass

    def _unsupported_data_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def _unsupported_method(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def __bool__(self): # reliably restored by inspect
        # no doc
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fa3299082b0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CollectionModel), '__module__': 'gi.repository.GcrUi', '__gtype__': <GType GcrCollectionModel (94715180884288)>, '__doc__': None, '__gsignals__': {}, 'change_selected': gi.FunctionInfo(change_selected), 'column_for_selected': gi.FunctionInfo(column_for_selected), 'get_collection': gi.FunctionInfo(get_collection), 'get_selected_objects': gi.FunctionInfo(get_selected_objects), 'is_selected': gi.FunctionInfo(is_selected), 'iter_for_object': gi.FunctionInfo(iter_for_object), 'object_for_iter': gi.FunctionInfo(object_for_iter), 'set_collection': gi.FunctionInfo(set_collection), 'set_selected_objects': gi.FunctionInfo(set_selected_objects), 'toggle_selected': gi.FunctionInfo(toggle_selected), 'parent': <property object at 0x7fa3298ed770>, 'pv': <property object at 0x7fa3298ed860>})"
    __gdoc__ = 'Object GcrCollectionModel\n\nProperties from GcrCollectionModel:\n  collection -> GcrCollection: Object Collection\n    Collection to get objects from\n  columns -> gpointer: Columns\n    Columns for the model\n  mode -> GcrCollectionModelMode: Mode\n    Tree or list mode\n\nSignals from GtkTreeModel:\n  row-changed (GtkTreePath, GtkTreeIter)\n  row-inserted (GtkTreePath, GtkTreeIter)\n  row-has-child-toggled (GtkTreePath, GtkTreeIter)\n  row-deleted (GtkTreePath)\n  rows-reordered (GtkTreePath, GtkTreeIter, gpointer)\n\nSignals from GtkTreeSortable:\n  sort-column-changed ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GcrCollectionModel (94715180884288)>'
    __info__ = ObjectInfo(CollectionModel)


