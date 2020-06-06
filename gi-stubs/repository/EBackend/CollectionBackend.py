# encoding: utf-8
# module gi.repository.EBackend
# from /usr/lib64/girepository-1.0/EBackend-1.2.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


from .Backend import Backend

class CollectionBackend(Backend):
    """
    :Constructors:
    
    ::
    
        CollectionBackend(**properties)
    """
    def authenticate_children(self, credentials): # real signature unknown; restored from __doc__
        """ authenticate_children(self, credentials:EDataServer.NamedParameters) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def claim_all_resources(self): # real signature unknown; restored from __doc__
        """ claim_all_resources(self) -> list """
        return []

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

    def create_resource(self, source, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_resource(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_resource_finish(self, result): # real signature unknown; restored from __doc__
        """ create_resource_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def create_resource_sync(self, source, cancellable=None): # real signature unknown; restored from __doc__
        """ create_resource_sync(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def credentials_required_finish(self, result): # real signature unknown; restored from __doc__
        """ credentials_required_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def credentials_required_sync(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None): # real signature unknown; restored from __doc__
        """ credentials_required_sync(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_resource(self, source, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_resource(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_resource_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_resource_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def delete_resource_sync(self, source, cancellable=None): # real signature unknown; restored from __doc__
        """ delete_resource_sync(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_authenticate_sync(self, *args, **kwargs): # real signature unknown
        """ authenticate_sync(self, credentials:EDataServer.NamedParameters, out_certificate_pem:str, out_certificate_errors:Gio.TlsCertificateFlags, cancellable:Gio.Cancellable=None) -> EDataServer.SourceAuthenticationResult """
        pass

    def do_child_added(self, *args, **kwargs): # real signature unknown
        """ child_added(self, child_source:EDataServer.Source) """
        pass

    def do_child_removed(self, *args, **kwargs): # real signature unknown
        """ child_removed(self, child_source:EDataServer.Source) """
        pass

    def do_create_resource(self, *args, **kwargs): # real signature unknown
        """ create_resource(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_create_resource_finish(self, *args, **kwargs): # real signature unknown
        """ create_resource_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_create_resource_sync(self, *args, **kwargs): # real signature unknown
        """ create_resource_sync(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_delete_resource(self, *args, **kwargs): # real signature unknown
        """ delete_resource(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_delete_resource_finish(self, *args, **kwargs): # real signature unknown
        """ delete_resource_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_delete_resource_sync(self, *args, **kwargs): # real signature unknown
        """ delete_resource_sync(self, source:EDataServer.Source, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_dup_resource_id(self, *args, **kwargs): # real signature unknown
        """ dup_resource_id(self, child_source:EDataServer.Source) -> str """
        pass

    def do_get_destination_address(self, *args, **kwargs): # real signature unknown
        """ get_destination_address(self) -> bool, host:str, port:int """
        pass

    def do_populate(self, *args, **kwargs): # real signature unknown
        """ populate(self) """
        pass

    def do_prepare_shutdown(self, *args, **kwargs): # real signature unknown
        """ prepare_shutdown(self) """
        pass

    def dup_resource_id(self, child_source): # real signature unknown; restored from __doc__
        """ dup_resource_id(self, child_source:EDataServer.Source) -> str """
        return ""

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_online_state_updated(self, cancellable=None): # real signature unknown; restored from __doc__
        """ ensure_online_state_updated(self, cancellable:Gio.Cancellable=None) """
        pass

    def ensure_source_status_connected(self): # real signature unknown; restored from __doc__
        """ ensure_source_status_connected(self) """
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

    def getv(self, names, values): # real signature unknown; restored from __doc__
        """ getv(self, names:list, values:list) """
        pass

    def get_cache_dir(self): # real signature unknown; restored from __doc__
        """ get_cache_dir(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_destination_address(self): # real signature unknown; restored from __doc__
        """ get_destination_address(self) -> bool, host:str, port:int """
        return False

    def get_online(self): # real signature unknown; restored from __doc__
        """ get_online(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_source(self): # real signature unknown; restored from __doc__
        """ get_source(self) -> EDataServer.Source """
        pass

    def get_user_prompter(self): # real signature unknown; restored from __doc__
        """ get_user_prompter(self) """
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

    def is_destination_reachable(self, cancellable=None): # real signature unknown; restored from __doc__
        """ is_destination_reachable(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_new_source(self, source): # real signature unknown; restored from __doc__
        """ is_new_source(self, source:EDataServer.Source) -> bool """
        return False

    def list_calendar_sources(self): # real signature unknown; restored from __doc__
        """ list_calendar_sources(self) -> list """
        return []

    def list_contacts_sources(self): # real signature unknown; restored from __doc__
        """ list_contacts_sources(self) -> list """
        return []

    def list_mail_sources(self): # real signature unknown; restored from __doc__
        """ list_mail_sources(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_child(self, resource_id): # real signature unknown; restored from __doc__
        """ new_child(self, resource_id:str) -> EDataServer.Source """
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

    def prepare_shutdown(self): # real signature unknown; restored from __doc__
        """ prepare_shutdown(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_connectable(self): # real signature unknown; restored from __doc__
        """ ref_connectable(self) -> Gio.SocketConnectable or None """
        pass

    def ref_main_context(self): # real signature unknown; restored from __doc__
        """ ref_main_context(self) -> GLib.MainContext """
        pass

    def ref_proxy_resolver(self): # real signature unknown; restored from __doc__
        """ ref_proxy_resolver(self) -> Gio.ProxyResolver or None """
        pass

    def ref_server(self): # real signature unknown; restored from __doc__
        """ ref_server(self) -> EBackend.SourceRegistryServer """
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

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def schedule_authenticate(self, credentials=None): # real signature unknown; restored from __doc__
        """ schedule_authenticate(self, credentials:EDataServer.NamedParameters=None) """
        pass

    def schedule_credentials_required(self, reason, certificate_pem, certificate_errors, op_error=None, cancellable=None, who_calls=None): # real signature unknown; restored from __doc__
        """ schedule_credentials_required(self, reason:EDataServer.SourceCredentialsReason, certificate_pem:str, certificate_errors:Gio.TlsCertificateFlags, op_error:error=None, cancellable:Gio.Cancellable=None, who_calls:str=None) """
        pass

    def schedule_populate(self): # real signature unknown; restored from __doc__
        """ schedule_populate(self) """
        pass

    def set_connectable(self, connectable): # real signature unknown; restored from __doc__
        """ set_connectable(self, connectable:Gio.SocketConnectable) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_online(self, online): # real signature unknown; restored from __doc__
        """ set_online(self, online:bool) """
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

    def trust_prompt(self, parameters, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ trust_prompt(self, parameters:EDataServer.NamedParameters, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def trust_prompt_finish(self, result): # real signature unknown; restored from __doc__
        """ trust_prompt_finish(self, result:Gio.AsyncResult) -> EDataServer.TrustPromptResponse """
        pass

    def trust_prompt_sync(self, parameters, cancellable=None): # real signature unknown; restored from __doc__
        """ trust_prompt_sync(self, parameters:EDataServer.NamedParameters, cancellable:Gio.Cancellable=None) -> EDataServer.TrustPromptResponse """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f9dbf8c3640>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CollectionBackend), '__module__': 'gi.repository.EBackend', '__gtype__': <GType ECollectionBackend (94170535235776)>, '__doc__': None, '__gsignals__': {}, 'authenticate_children': gi.FunctionInfo(authenticate_children), 'claim_all_resources': gi.FunctionInfo(claim_all_resources), 'create_resource': gi.FunctionInfo(create_resource), 'create_resource_finish': gi.FunctionInfo(create_resource_finish), 'create_resource_sync': gi.FunctionInfo(create_resource_sync), 'delete_resource': gi.FunctionInfo(delete_resource), 'delete_resource_finish': gi.FunctionInfo(delete_resource_finish), 'delete_resource_sync': gi.FunctionInfo(delete_resource_sync), 'dup_resource_id': gi.FunctionInfo(dup_resource_id), 'get_cache_dir': gi.FunctionInfo(get_cache_dir), 'is_new_source': gi.FunctionInfo(is_new_source), 'list_calendar_sources': gi.FunctionInfo(list_calendar_sources), 'list_contacts_sources': gi.FunctionInfo(list_contacts_sources), 'list_mail_sources': gi.FunctionInfo(list_mail_sources), 'new_child': gi.FunctionInfo(new_child), 'ref_proxy_resolver': gi.FunctionInfo(ref_proxy_resolver), 'ref_server': gi.FunctionInfo(ref_server), 'schedule_populate': gi.FunctionInfo(schedule_populate), 'do_child_added': gi.VFuncInfo(child_added), 'do_child_removed': gi.VFuncInfo(child_removed), 'do_create_resource': gi.VFuncInfo(create_resource), 'do_create_resource_finish': gi.VFuncInfo(create_resource_finish), 'do_create_resource_sync': gi.VFuncInfo(create_resource_sync), 'do_delete_resource': gi.VFuncInfo(delete_resource), 'do_delete_resource_finish': gi.VFuncInfo(delete_resource_finish), 'do_delete_resource_sync': gi.VFuncInfo(delete_resource_sync), 'do_dup_resource_id': gi.VFuncInfo(dup_resource_id), 'do_populate': gi.VFuncInfo(populate), 'parent': <property object at 0x7f9dc2d82f40>, 'priv': <property object at 0x7f9dc2d88040>})"
    __gdoc__ = 'Object ECollectionBackend\n\nSignals from ECollectionBackend:\n  child-added (EServerSideSource)\n  child-removed (EServerSideSource)\n\nProperties from ECollectionBackend:\n  proxy-resolver -> GProxyResolver: Proxy Resolver\n    The proxy resolver for this backend\n  server -> ESourceRegistryServer: Server\n    The server to which the backend belongs\n\nProperties from EBackend:\n  connectable -> GSocketConnectable: Connectable\n    Socket endpoint of a network service\n  main-context -> GMainContext: Main Context\n    The main loop context on which to attach event sources\n  online -> gboolean: Online\n    Whether the backend is online\n  source -> ESource: Source\n    The data source being acted upon\n  user-prompter -> EUserPrompter: User Prompter\n    User prompter instance\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ECollectionBackend (94170535235776)>'
    __info__ = ObjectInfo(CollectionBackend)

