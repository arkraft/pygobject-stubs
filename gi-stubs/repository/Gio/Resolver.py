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


class Resolver(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Resolver(**properties)
    """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_lookup_by_address(self, *args, **kwargs): # real signature unknown
        """ lookup_by_address(self, address:Gio.InetAddress, cancellable:Gio.Cancellable=None) -> str """
        pass

    def do_lookup_by_address_async(self, *args, **kwargs): # real signature unknown
        """ lookup_by_address_async(self, address:Gio.InetAddress, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_by_address_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_by_address_finish(self, result:Gio.AsyncResult) -> str """
        pass

    def do_lookup_by_name(self, *args, **kwargs): # real signature unknown
        """ lookup_by_name(self, hostname:str, cancellable:Gio.Cancellable=None) -> list """
        pass

    def do_lookup_by_name_async(self, *args, **kwargs): # real signature unknown
        """ lookup_by_name_async(self, hostname:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_by_name_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_by_name_finish(self, result:Gio.AsyncResult) -> list """
        pass

    def do_lookup_by_name_with_flags(self, *args, **kwargs): # real signature unknown
        """ lookup_by_name_with_flags(self, hostname:str, flags:Gio.ResolverNameLookupFlags, cancellable:Gio.Cancellable=None) -> list """
        pass

    def do_lookup_by_name_with_flags_async(self, *args, **kwargs): # real signature unknown
        """ lookup_by_name_with_flags_async(self, hostname:str, flags:Gio.ResolverNameLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_by_name_with_flags_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_by_name_with_flags_finish(self, result:Gio.AsyncResult) -> list """
        pass

    def do_lookup_records(self, *args, **kwargs): # real signature unknown
        """ lookup_records(self, rrname:str, record_type:Gio.ResolverRecordType, cancellable:Gio.Cancellable=None) -> list """
        pass

    def do_lookup_records_async(self, *args, **kwargs): # real signature unknown
        """ lookup_records_async(self, rrname:str, record_type:Gio.ResolverRecordType, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_records_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_records_finish(self, result:Gio.AsyncResult) -> list """
        pass

    def do_lookup_service_async(self, *args, **kwargs): # real signature unknown
        """ lookup_service_async(self, rrname:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_lookup_service_finish(self, *args, **kwargs): # real signature unknown
        """ lookup_service_finish(self, result:Gio.AsyncResult) -> list """
        pass

    def do_reload(self, *args, **kwargs): # real signature unknown
        """ reload(self) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
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

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gio.Resolver """
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

    def lookup_by_address(self, address, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_by_address(self, address:Gio.InetAddress, cancellable:Gio.Cancellable=None) -> str """
        return ""

    def lookup_by_address_async(self, address, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_by_address_async(self, address:Gio.InetAddress, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_by_address_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_by_address_finish(self, result:Gio.AsyncResult) -> str """
        return ""

    def lookup_by_name(self, hostname, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_by_name(self, hostname:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def lookup_by_name_async(self, hostname, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_by_name_async(self, hostname:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_by_name_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_by_name_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def lookup_by_name_with_flags(self, hostname, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_by_name_with_flags(self, hostname:str, flags:Gio.ResolverNameLookupFlags, cancellable:Gio.Cancellable=None) -> list """
        return []

    def lookup_by_name_with_flags_async(self, hostname, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_by_name_with_flags_async(self, hostname:str, flags:Gio.ResolverNameLookupFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_by_name_with_flags_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_by_name_with_flags_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def lookup_records(self, rrname, record_type, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_records(self, rrname:str, record_type:Gio.ResolverRecordType, cancellable:Gio.Cancellable=None) -> list """
        return []

    def lookup_records_async(self, rrname, record_type, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_records_async(self, rrname:str, record_type:Gio.ResolverRecordType, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_records_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_records_finish(self, result:Gio.AsyncResult) -> list """
        return []

    def lookup_service(self, service, protocol, domain, cancellable=None): # real signature unknown; restored from __doc__
        """ lookup_service(self, service:str, protocol:str, domain:str, cancellable:Gio.Cancellable=None) -> list """
        return []

    def lookup_service_async(self, service, protocol, domain, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ lookup_service_async(self, service:str, protocol:str, domain:str, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def lookup_service_finish(self, result): # real signature unknown; restored from __doc__
        """ lookup_service_finish(self, result:Gio.AsyncResult) -> list """
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

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default(self): # real signature unknown; restored from __doc__
        """ set_default(self) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f4b873349d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Resolver), '__module__': 'gi.repository.Gio', '__gtype__': <GType GResolver (94269257277792)>, '__doc__': None, '__gsignals__': {}, 'get_default': gi.FunctionInfo(get_default), 'lookup_by_address': gi.FunctionInfo(lookup_by_address), 'lookup_by_address_async': gi.FunctionInfo(lookup_by_address_async), 'lookup_by_address_finish': gi.FunctionInfo(lookup_by_address_finish), 'lookup_by_name': gi.FunctionInfo(lookup_by_name), 'lookup_by_name_async': gi.FunctionInfo(lookup_by_name_async), 'lookup_by_name_finish': gi.FunctionInfo(lookup_by_name_finish), 'lookup_by_name_with_flags': gi.FunctionInfo(lookup_by_name_with_flags), 'lookup_by_name_with_flags_async': gi.FunctionInfo(lookup_by_name_with_flags_async), 'lookup_by_name_with_flags_finish': gi.FunctionInfo(lookup_by_name_with_flags_finish), 'lookup_records': gi.FunctionInfo(lookup_records), 'lookup_records_async': gi.FunctionInfo(lookup_records_async), 'lookup_records_finish': gi.FunctionInfo(lookup_records_finish), 'lookup_service': gi.FunctionInfo(lookup_service), 'lookup_service_async': gi.FunctionInfo(lookup_service_async), 'lookup_service_finish': gi.FunctionInfo(lookup_service_finish), 'set_default': gi.FunctionInfo(set_default), 'do_lookup_by_address': gi.VFuncInfo(lookup_by_address), 'do_lookup_by_address_async': gi.VFuncInfo(lookup_by_address_async), 'do_lookup_by_address_finish': gi.VFuncInfo(lookup_by_address_finish), 'do_lookup_by_name': gi.VFuncInfo(lookup_by_name), 'do_lookup_by_name_async': gi.VFuncInfo(lookup_by_name_async), 'do_lookup_by_name_finish': gi.VFuncInfo(lookup_by_name_finish), 'do_lookup_by_name_with_flags': gi.VFuncInfo(lookup_by_name_with_flags), 'do_lookup_by_name_with_flags_async': gi.VFuncInfo(lookup_by_name_with_flags_async), 'do_lookup_by_name_with_flags_finish': gi.VFuncInfo(lookup_by_name_with_flags_finish), 'do_lookup_records': gi.VFuncInfo(lookup_records), 'do_lookup_records_async': gi.VFuncInfo(lookup_records_async), 'do_lookup_records_finish': gi.VFuncInfo(lookup_records_finish), 'do_lookup_service_async': gi.VFuncInfo(lookup_service_async), 'do_lookup_service_finish': gi.VFuncInfo(lookup_service_finish), 'do_reload': gi.VFuncInfo(reload), 'parent_instance': <property object at 0x7f4b87fa98b0>, 'priv': <property object at 0x7f4b87fa9ae0>})"
    __gdoc__ = 'Object GResolver\n\nSignals from GResolver:\n  reload ()\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GResolver (94269257277792)>'
    __info__ = ObjectInfo(Resolver)


