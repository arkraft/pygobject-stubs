# encoding: utf-8
# module gi.repository.EDataServer
# from /usr/lib64/girepository-1.0/EDataServer-1.2.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Soup as __gi_repository_Soup
import gobject as __gobject


class SourceRegistry(__gi_overrides_GObject.Object, __gi_repository_Gio.AsyncInitable, __gi_repository_Gio.Initable):
    """
    :Constructors:
    
    ::
    
        SourceRegistry(**properties)
        new_finish(result:Gio.AsyncResult) -> EDataServer.SourceRegistry
        new_sync(cancellable:Gio.Cancellable=None) -> EDataServer.SourceRegistry
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def check_enabled(self, source): # real signature unknown; restored from __doc__
        """ check_enabled(self, source:EDataServer.Source) -> bool """
        return False

    def commit_source(self, source, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ commit_source(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def commit_source_finish(self, result): # real signature unknown; restored from __doc__
        """ commit_source_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def commit_source_sync(self, source, cancellable=None): # real signature unknown; restored from __doc__
        """ commit_source_sync(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    def create_sources(self, list_of_sources, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_sources(self, list_of_sources:list, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_sources_finish(self, result): # real signature unknown; restored from __doc__
        """ create_sources_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def create_sources_sync(self, list_of_sources, cancellable=None): # real signature unknown; restored from __doc__
        """ create_sources_sync(self, list_of_sources:list, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def debug_dump(self, extension_name=None): # real signature unknown; restored from __doc__
        """ debug_dump(self, extension_name:str=None) """
        pass

    def debug_enabled(self): # real signature unknown; restored from __doc__
        """ debug_enabled() -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_credentials_required(self, *args, **kwargs): # real signature unknown
        """ credentials_required(self, source:EDataServer.Source, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error) """
        pass

    def do_source_added(self, *args, **kwargs): # real signature unknown
        """ source_added(self, source:EDataServer.Source) """
        pass

    def do_source_changed(self, *args, **kwargs): # real signature unknown
        """ source_changed(self, source:EDataServer.Source) """
        pass

    def do_source_disabled(self, *args, **kwargs): # real signature unknown
        """ source_disabled(self, source:EDataServer.Source) """
        pass

    def do_source_enabled(self, *args, **kwargs): # real signature unknown
        """ source_enabled(self, source:EDataServer.Source) """
        pass

    def do_source_removed(self, *args, **kwargs): # real signature unknown
        """ source_removed(self, source:EDataServer.Source) """
        pass

    def dup_unique_display_name(self, source, extension_name=None): # real signature unknown; restored from __doc__
        """ dup_unique_display_name(self, source:EDataServer.Source, extension_name:str=None) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def find_extension(self, source, extension_name): # real signature unknown; restored from __doc__
        """ find_extension(self, source:EDataServer.Source, extension_name:str) -> EDataServer.Source """
        pass

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

    def free_display_tree(self, display_tree): # real signature unknown; restored from __doc__
        """ free_display_tree(display_tree:GLib.Node) """
        pass

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_oauth2_services(self): # real signature unknown; restored from __doc__
        """ get_oauth2_services(self) -> EDataServer.OAuth2Services """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def init(self, cancellable=None): # real signature unknown; restored from __doc__
        """ init(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def init_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ init_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def init_finish(self, res): # real signature unknown; restored from __doc__
        """ init_finish(self, res:Gio.AsyncResult) -> bool """
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

    def list_enabled(self, extension_name=None): # real signature unknown; restored from __doc__
        """ list_enabled(self, extension_name:str=None) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def list_sources(self, extension_name=None): # real signature unknown; restored from __doc__
        """ list_sources(self, extension_name:str=None) -> list """
        return []

    def new(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ new(cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def newv_async(self, object_type, n_parameters, parameters, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ newv_async(object_type:GType, n_parameters:int, parameters:GObject.Parameter, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def new_finish(self, result): # real signature unknown; restored from __doc__
        """ new_finish(result:Gio.AsyncResult) -> EDataServer.SourceRegistry """
        pass

    def new_sync(self, cancellable=None): # real signature unknown; restored from __doc__
        """ new_sync(cancellable:Gio.Cancellable=None) -> EDataServer.SourceRegistry """
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

    def refresh_backend(self, source_uid, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ refresh_backend(self, source_uid:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def refresh_backend_finish(self, result): # real signature unknown; restored from __doc__
        """ refresh_backend_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def refresh_backend_sync(self, source_uid, cancellable=None): # real signature unknown; restored from __doc__
        """ refresh_backend_sync(self, source_uid:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def ref_builtin_address_book(self): # real signature unknown; restored from __doc__
        """ ref_builtin_address_book(self) -> EDataServer.Source """
        pass

    def ref_builtin_calendar(self): # real signature unknown; restored from __doc__
        """ ref_builtin_calendar(self) -> EDataServer.Source """
        pass

    def ref_builtin_mail_account(self): # real signature unknown; restored from __doc__
        """ ref_builtin_mail_account(self) -> EDataServer.Source """
        pass

    def ref_builtin_memo_list(self): # real signature unknown; restored from __doc__
        """ ref_builtin_memo_list(self) -> EDataServer.Source """
        pass

    def ref_builtin_proxy(self): # real signature unknown; restored from __doc__
        """ ref_builtin_proxy(self) -> EDataServer.Source """
        pass

    def ref_builtin_task_list(self): # real signature unknown; restored from __doc__
        """ ref_builtin_task_list(self) -> EDataServer.Source """
        pass

    def ref_default_address_book(self): # real signature unknown; restored from __doc__
        """ ref_default_address_book(self) -> EDataServer.Source """
        pass

    def ref_default_calendar(self): # real signature unknown; restored from __doc__
        """ ref_default_calendar(self) -> EDataServer.Source """
        pass

    def ref_default_for_extension_name(self, extension_name): # real signature unknown; restored from __doc__
        """ ref_default_for_extension_name(self, extension_name:str) -> EDataServer.Source """
        pass

    def ref_default_mail_account(self): # real signature unknown; restored from __doc__
        """ ref_default_mail_account(self) -> EDataServer.Source """
        pass

    def ref_default_mail_identity(self): # real signature unknown; restored from __doc__
        """ ref_default_mail_identity(self) -> EDataServer.Source """
        pass

    def ref_default_memo_list(self): # real signature unknown; restored from __doc__
        """ ref_default_memo_list(self) -> EDataServer.Source """
        pass

    def ref_default_task_list(self): # real signature unknown; restored from __doc__
        """ ref_default_task_list(self) -> EDataServer.Source """
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_source(self, uid): # real signature unknown; restored from __doc__
        """ ref_source(self, uid:str) -> EDataServer.Source """
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default_address_book(self, default_source=None): # real signature unknown; restored from __doc__
        """ set_default_address_book(self, default_source:EDataServer.Source=None) """
        pass

    def set_default_calendar(self, default_source=None): # real signature unknown; restored from __doc__
        """ set_default_calendar(self, default_source:EDataServer.Source=None) """
        pass

    def set_default_for_extension_name(self, extension_name, default_source=None): # real signature unknown; restored from __doc__
        """ set_default_for_extension_name(self, extension_name:str, default_source:EDataServer.Source=None) """
        pass

    def set_default_mail_account(self, default_source=None): # real signature unknown; restored from __doc__
        """ set_default_mail_account(self, default_source:EDataServer.Source=None) """
        pass

    def set_default_mail_identity(self, default_source=None): # real signature unknown; restored from __doc__
        """ set_default_mail_identity(self, default_source:EDataServer.Source=None) """
        pass

    def set_default_memo_list(self, default_source=None): # real signature unknown; restored from __doc__
        """ set_default_memo_list(self, default_source:EDataServer.Source=None) """
        pass

    def set_default_task_list(self, default_source=None): # real signature unknown; restored from __doc__
        """ set_default_task_list(self, default_source:EDataServer.Source=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
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

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

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

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f626e6d4370>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SourceRegistry), '__module__': 'gi.repository.EDataServer', '__gtype__': <GType ESourceRegistry (94877537278128)>, '__doc__': None, '__gsignals__': {}, 'new_finish': gi.FunctionInfo(new_finish), 'new_sync': gi.FunctionInfo(new_sync), 'debug_enabled': gi.FunctionInfo(debug_enabled), 'free_display_tree': gi.FunctionInfo(free_display_tree), 'new': gi.FunctionInfo(new), 'check_enabled': gi.FunctionInfo(check_enabled), 'commit_source': gi.FunctionInfo(commit_source), 'commit_source_finish': gi.FunctionInfo(commit_source_finish), 'commit_source_sync': gi.FunctionInfo(commit_source_sync), 'create_sources': gi.FunctionInfo(create_sources), 'create_sources_finish': gi.FunctionInfo(create_sources_finish), 'create_sources_sync': gi.FunctionInfo(create_sources_sync), 'debug_dump': gi.FunctionInfo(debug_dump), 'dup_unique_display_name': gi.FunctionInfo(dup_unique_display_name), 'find_extension': gi.FunctionInfo(find_extension), 'get_oauth2_services': gi.FunctionInfo(get_oauth2_services), 'list_enabled': gi.FunctionInfo(list_enabled), 'list_sources': gi.FunctionInfo(list_sources), 'ref_builtin_address_book': gi.FunctionInfo(ref_builtin_address_book), 'ref_builtin_calendar': gi.FunctionInfo(ref_builtin_calendar), 'ref_builtin_mail_account': gi.FunctionInfo(ref_builtin_mail_account), 'ref_builtin_memo_list': gi.FunctionInfo(ref_builtin_memo_list), 'ref_builtin_proxy': gi.FunctionInfo(ref_builtin_proxy), 'ref_builtin_task_list': gi.FunctionInfo(ref_builtin_task_list), 'ref_default_address_book': gi.FunctionInfo(ref_default_address_book), 'ref_default_calendar': gi.FunctionInfo(ref_default_calendar), 'ref_default_for_extension_name': gi.FunctionInfo(ref_default_for_extension_name), 'ref_default_mail_account': gi.FunctionInfo(ref_default_mail_account), 'ref_default_mail_identity': gi.FunctionInfo(ref_default_mail_identity), 'ref_default_memo_list': gi.FunctionInfo(ref_default_memo_list), 'ref_default_task_list': gi.FunctionInfo(ref_default_task_list), 'ref_source': gi.FunctionInfo(ref_source), 'refresh_backend': gi.FunctionInfo(refresh_backend), 'refresh_backend_finish': gi.FunctionInfo(refresh_backend_finish), 'refresh_backend_sync': gi.FunctionInfo(refresh_backend_sync), 'set_default_address_book': gi.FunctionInfo(set_default_address_book), 'set_default_calendar': gi.FunctionInfo(set_default_calendar), 'set_default_for_extension_name': gi.FunctionInfo(set_default_for_extension_name), 'set_default_mail_account': gi.FunctionInfo(set_default_mail_account), 'set_default_mail_identity': gi.FunctionInfo(set_default_mail_identity), 'set_default_memo_list': gi.FunctionInfo(set_default_memo_list), 'set_default_task_list': gi.FunctionInfo(set_default_task_list), 'do_credentials_required': gi.VFuncInfo(credentials_required), 'do_source_added': gi.VFuncInfo(source_added), 'do_source_changed': gi.VFuncInfo(source_changed), 'do_source_disabled': gi.VFuncInfo(source_disabled), 'do_source_enabled': gi.VFuncInfo(source_enabled), 'do_source_removed': gi.VFuncInfo(source_removed), 'parent': <property object at 0x7f626e8c4770>, 'priv': <property object at 0x7f626e8c4860>})"
    __gdoc__ = 'Object ESourceRegistry\n\nSignals from ESourceRegistry:\n  credentials-required (ESource, ESourceCredentialsReason, gchararray, GTlsCertificateFlags, GError)\n  source-added (ESource)\n  source-changed (ESource)\n  source-removed (ESource)\n  source-enabled (ESource)\n  source-disabled (ESource)\n\nProperties from ESourceRegistry:\n  default-address-book -> ESource: Default Address Book\n    The default address book ESource\n  default-calendar -> ESource: Default Calendar\n    The default calendar ESource\n  default-mail-account -> ESource: Default Mail Account\n    The default mail account ESource\n  default-mail-identity -> ESource: Default Mail Identity\n    The default mail identity ESource\n  default-memo-list -> ESource: Default Memo List\n    The default memo list ESource\n  default-task-list -> ESource: Default Task List\n    The default task list ESource\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ESourceRegistry (94877537278128)>'
    __info__ = ObjectInfo(SourceRegistry)


