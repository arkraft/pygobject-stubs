# encoding: utf-8
# module gi.repository.AppStreamGlib
# from /usr/lib64/girepository-1.0/AppStreamGlib-1.0.typelib
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
import gobject as __gobject


class Store(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Store(**properties)
        new() -> AppStreamGlib.Store
    """
    def add_app(self, app): # real signature unknown; restored from __doc__
        """ add_app(self, app:AppStreamGlib.App) """
        pass

    def add_apps(self, apps): # real signature unknown; restored from __doc__
        """ add_apps(self, apps:list) """
        pass

    def add_filter(self, kind): # real signature unknown; restored from __doc__
        """ add_filter(self, kind:AppStreamGlib.AppKind) """
        pass

    def add_metadata_index(self, key): # real signature unknown; restored from __doc__
        """ add_metadata_index(self, key:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

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

    def convert_icons(self, kind): # real signature unknown; restored from __doc__
        """ convert_icons(self, kind:AppStreamGlib.IconKind) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_app_added(self, *args, **kwargs): # real signature unknown
        """ app_added(self, app:AppStreamGlib.App) """
        pass

    def do_app_changed(self, *args, **kwargs): # real signature unknown
        """ app_changed(self, app:AppStreamGlib.App) """
        pass

    def do_app_removed(self, *args, **kwargs): # real signature unknown
        """ app_removed(self, app:AppStreamGlib.App) """
        pass

    def do_changed(self, *args, **kwargs): # real signature unknown
        """ changed(self) """
        pass

    def dup_apps(self): # real signature unknown; restored from __doc__
        """ dup_apps(self) -> list """
        return []

    def dup_apps_by_id_merge(self, id): # real signature unknown; restored from __doc__
        """ dup_apps_by_id_merge(self, id:str) -> list """
        return []

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def error_quark(self): # real signature unknown; restored from __doc__
        """ error_quark() -> int """
        return 0

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def from_bytes(self, bytes, cancellable=None): # real signature unknown; restored from __doc__
        """ from_bytes(self, bytes:GLib.Bytes, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def from_file(self, file, icon_root=None, cancellable=None): # real signature unknown; restored from __doc__
        """ from_file(self, file:Gio.File, icon_root:str=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def from_xml(self, data, icon_root=None): # real signature unknown; restored from __doc__
        """ from_xml(self, data:str, icon_root:str=None) -> bool """
        return False

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_add_flags(self): # real signature unknown; restored from __doc__
        """ get_add_flags(self) -> int """
        return 0

    def get_api_version(self): # real signature unknown; restored from __doc__
        """ get_api_version(self) -> float """
        return 0.0

    def get_apps(self): # real signature unknown; restored from __doc__
        """ get_apps(self) -> list """
        return []

    def get_apps_by_id(self, id): # real signature unknown; restored from __doc__
        """ get_apps_by_id(self, id:str) -> list """
        return []

    def get_apps_by_id_merge(self, id): # real signature unknown; restored from __doc__
        """ get_apps_by_id_merge(self, id:str) -> list """
        return []

    def get_apps_by_metadata(self, key, value): # real signature unknown; restored from __doc__
        """ get_apps_by_metadata(self, key:str, value:str) -> list """
        return []

    def get_apps_by_provide(self, kind, value): # real signature unknown; restored from __doc__
        """ get_apps_by_provide(self, kind:AppStreamGlib.ProvideKind, value:str) -> list """
        return []

    def get_app_by_id(self, id): # real signature unknown; restored from __doc__
        """ get_app_by_id(self, id:str) -> AppStreamGlib.App """
        pass

    def get_app_by_id_ignore_prefix(self, id): # real signature unknown; restored from __doc__
        """ get_app_by_id_ignore_prefix(self, id:str) -> AppStreamGlib.App """
        pass

    def get_app_by_id_with_fallbacks(self, id): # real signature unknown; restored from __doc__
        """ get_app_by_id_with_fallbacks(self, id:str) -> AppStreamGlib.App """
        pass

    def get_app_by_launchable(self, kind, value): # real signature unknown; restored from __doc__
        """ get_app_by_launchable(self, kind:AppStreamGlib.LaunchableKind, value:str) -> AppStreamGlib.App """
        pass

    def get_app_by_pkgname(self, pkgname): # real signature unknown; restored from __doc__
        """ get_app_by_pkgname(self, pkgname:str) -> AppStreamGlib.App """
        pass

    def get_app_by_pkgnames(self, pkgnames): # real signature unknown; restored from __doc__
        """ get_app_by_pkgnames(self, pkgnames:str) -> AppStreamGlib.App """
        pass

    def get_app_by_provide(self, kind, value): # real signature unknown; restored from __doc__
        """ get_app_by_provide(self, kind:AppStreamGlib.ProvideKind, value:str) -> AppStreamGlib.App """
        pass

    def get_app_by_unique_id(self, unique_id, search_flags): # real signature unknown; restored from __doc__
        """ get_app_by_unique_id(self, unique_id:str, search_flags:int) -> AppStreamGlib.App """
        pass

    def get_builder_id(self): # real signature unknown; restored from __doc__
        """ get_builder_id(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_destdir(self): # real signature unknown; restored from __doc__
        """ get_destdir(self) -> str """
        return ""

    def get_origin(self): # real signature unknown; restored from __doc__
        """ get_origin(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_search_match(self): # real signature unknown; restored from __doc__
        """ get_search_match(self) -> int """
        return 0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_watch_flags(self): # real signature unknown; restored from __doc__
        """ get_watch_flags(self) -> int """
        return 0

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

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ load(self, flags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def load_async(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_async(self, flags:AppStreamGlib.StoreLoadFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_finish(self, result): # real signature unknown; restored from __doc__
        """ load_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def load_path(self, path, cancellable=None): # real signature unknown; restored from __doc__
        """ load_path(self, path:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def load_path_async(self, path, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_path_async(self, path:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_path_finish(self, result): # real signature unknown; restored from __doc__
        """ load_path_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def load_search_cache(self): # real signature unknown; restored from __doc__
        """ load_search_cache(self) """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> AppStreamGlib.Store """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_all(self): # real signature unknown; restored from __doc__
        """ remove_all(self) """
        pass

    def remove_app(self, app): # real signature unknown; restored from __doc__
        """ remove_app(self, app:AppStreamGlib.App) """
        pass

    def remove_apps_with_veto(self): # real signature unknown; restored from __doc__
        """ remove_apps_with_veto(self) """
        pass

    def remove_app_by_id(self, id): # real signature unknown; restored from __doc__
        """ remove_app_by_id(self, id:str) """
        pass

    def remove_filter(self, kind): # real signature unknown; restored from __doc__
        """ remove_filter(self, kind:AppStreamGlib.AppKind) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_add_flags(self, add_flags): # real signature unknown; restored from __doc__
        """ set_add_flags(self, add_flags:int) """
        pass

    def set_api_version(self, api_version): # real signature unknown; restored from __doc__
        """ set_api_version(self, api_version:float) """
        pass

    def set_builder_id(self, builder_id): # real signature unknown; restored from __doc__
        """ set_builder_id(self, builder_id:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_destdir(self, destdir): # real signature unknown; restored from __doc__
        """ set_destdir(self, destdir:str) """
        pass

    def set_origin(self, origin): # real signature unknown; restored from __doc__
        """ set_origin(self, origin:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_match(self, search_match): # real signature unknown; restored from __doc__
        """ set_search_match(self, search_match:int) """
        pass

    def set_watch_flags(self, watch_flags): # real signature unknown; restored from __doc__
        """ set_watch_flags(self, watch_flags:int) """
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

    def to_file(self, file, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ to_file(self, file:Gio.File, flags:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def to_xml(self, flags): # real signature unknown; restored from __doc__
        """ to_xml(self, flags:int) -> GLib.String """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def validate(self, flags): # real signature unknown; restored from __doc__
        """ validate(self, flags:int) -> list """
        return []

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def _force_floating(self, *args, **kwargs): # real signature unknown
        """ force_floating(self) """
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

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, **properties): # real signature unknown; restored from __doc__
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f27414720d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Store), '__module__': 'gi.repository.AppStreamGlib', '__gtype__': <GType AsStore (93964255196112)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'error_quark': gi.FunctionInfo(error_quark), 'add_app': gi.FunctionInfo(add_app), 'add_apps': gi.FunctionInfo(add_apps), 'add_filter': gi.FunctionInfo(add_filter), 'add_metadata_index': gi.FunctionInfo(add_metadata_index), 'convert_icons': gi.FunctionInfo(convert_icons), 'dup_apps': gi.FunctionInfo(dup_apps), 'dup_apps_by_id_merge': gi.FunctionInfo(dup_apps_by_id_merge), 'from_bytes': gi.FunctionInfo(from_bytes), 'from_file': gi.FunctionInfo(from_file), 'from_xml': gi.FunctionInfo(from_xml), 'get_add_flags': gi.FunctionInfo(get_add_flags), 'get_api_version': gi.FunctionInfo(get_api_version), 'get_app_by_id': gi.FunctionInfo(get_app_by_id), 'get_app_by_id_ignore_prefix': gi.FunctionInfo(get_app_by_id_ignore_prefix), 'get_app_by_id_with_fallbacks': gi.FunctionInfo(get_app_by_id_with_fallbacks), 'get_app_by_launchable': gi.FunctionInfo(get_app_by_launchable), 'get_app_by_pkgname': gi.FunctionInfo(get_app_by_pkgname), 'get_app_by_pkgnames': gi.FunctionInfo(get_app_by_pkgnames), 'get_app_by_provide': gi.FunctionInfo(get_app_by_provide), 'get_app_by_unique_id': gi.FunctionInfo(get_app_by_unique_id), 'get_apps': gi.FunctionInfo(get_apps), 'get_apps_by_id': gi.FunctionInfo(get_apps_by_id), 'get_apps_by_id_merge': gi.FunctionInfo(get_apps_by_id_merge), 'get_apps_by_metadata': gi.FunctionInfo(get_apps_by_metadata), 'get_apps_by_provide': gi.FunctionInfo(get_apps_by_provide), 'get_builder_id': gi.FunctionInfo(get_builder_id), 'get_destdir': gi.FunctionInfo(get_destdir), 'get_origin': gi.FunctionInfo(get_origin), 'get_search_match': gi.FunctionInfo(get_search_match), 'get_size': gi.FunctionInfo(get_size), 'get_watch_flags': gi.FunctionInfo(get_watch_flags), 'load': gi.FunctionInfo(load), 'load_async': gi.FunctionInfo(load_async), 'load_finish': gi.FunctionInfo(load_finish), 'load_path': gi.FunctionInfo(load_path), 'load_path_async': gi.FunctionInfo(load_path_async), 'load_path_finish': gi.FunctionInfo(load_path_finish), 'load_search_cache': gi.FunctionInfo(load_search_cache), 'remove_all': gi.FunctionInfo(remove_all), 'remove_app': gi.FunctionInfo(remove_app), 'remove_app_by_id': gi.FunctionInfo(remove_app_by_id), 'remove_apps_with_veto': gi.FunctionInfo(remove_apps_with_veto), 'remove_filter': gi.FunctionInfo(remove_filter), 'set_add_flags': gi.FunctionInfo(set_add_flags), 'set_api_version': gi.FunctionInfo(set_api_version), 'set_builder_id': gi.FunctionInfo(set_builder_id), 'set_destdir': gi.FunctionInfo(set_destdir), 'set_origin': gi.FunctionInfo(set_origin), 'set_search_match': gi.FunctionInfo(set_search_match), 'set_watch_flags': gi.FunctionInfo(set_watch_flags), 'to_file': gi.FunctionInfo(to_file), 'to_xml': gi.FunctionInfo(to_xml), 'validate': gi.FunctionInfo(validate), 'do_app_added': gi.VFuncInfo(app_added), 'do_app_changed': gi.VFuncInfo(app_changed), 'do_app_removed': gi.VFuncInfo(app_removed), 'do_changed': gi.VFuncInfo(changed), 'parent_instance': <property object at 0x7f2741686450>})"
    __gdoc__ = 'Object AsStore\n\nSignals from AsStore:\n  changed ()\n  app-added (AsApp)\n  app-removed (AsApp)\n  app-changed (AsApp)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AsStore (93964255196112)>'
    __info__ = ObjectInfo(Store)


