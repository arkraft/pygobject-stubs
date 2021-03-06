# encoding: utf-8
# module gi.repository.NM
# from /usr/lib64/girepository-1.0/NM-1.0.typelib
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


from .Setting import Setting

class SettingIPTunnel(Setting):
    """
    :Constructors:
    
    ::
    
        SettingIPTunnel(**properties)
        new() -> NM.Setting
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compare(self, b, flags): # real signature unknown; restored from __doc__
        """ compare(self, b:NM.Setting, flags:NM.SettingCompareFlags) -> bool """
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

    def diff(self, b, flags, invert_results, results): # real signature unknown; restored from __doc__
        """ diff(self, b:NM.Setting, flags:NM.SettingCompareFlags, invert_results:bool, results:dict) -> bool, results:dict """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_aggregate(self, *args, **kwargs): # real signature unknown
        """ aggregate(self, type_i:int, arg=None) -> bool """
        pass

    def do_get_secret_flags(self, *args, **kwargs): # real signature unknown
        """ get_secret_flags(self, secret_name:str, out_flags:NM.SettingSecretFlags) -> bool """
        pass

    def do_init_from_dbus(self, *args, **kwargs): # real signature unknown
        """ init_from_dbus(self, keys:dict, setting_dict:GLib.Variant, connection_dict:GLib.Variant, parse_flags:int) -> bool """
        pass

    def do_set_secret_flags(self, *args, **kwargs): # real signature unknown
        """ set_secret_flags(self, secret_name:str, flags:NM.SettingSecretFlags) -> bool """
        pass

    def do_update_one_secret(self, *args, **kwargs): # real signature unknown
        """ update_one_secret(self, key:str, value:GLib.Variant) -> int """
        pass

    def do_verify(self, *args, **kwargs): # real signature unknown
        """ verify(self, connection:NM.Connection) -> int """
        pass

    def do_verify_secrets(self, *args, **kwargs): # real signature unknown
        """ verify_secrets(self, connection:NM.Connection=None) -> bool """
        pass

    def duplicate(self): # real signature unknown; restored from __doc__
        """ duplicate(self) -> NM.Setting """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def enumerate_values(self, func, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_values(self, func:NM.SettingValueIterFn, user_data=None) """
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

    def get_dbus_property_type(self, property_name): # real signature unknown; restored from __doc__
        """ get_dbus_property_type(self, property_name:str) -> GLib.VariantType """
        pass

    def get_encapsulation_limit(self): # real signature unknown; restored from __doc__
        """ get_encapsulation_limit(self) -> int """
        return 0

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> NM.IPTunnelFlags """
        pass

    def get_flow_label(self): # real signature unknown; restored from __doc__
        """ get_flow_label(self) -> int """
        return 0

    def get_input_key(self): # real signature unknown; restored from __doc__
        """ get_input_key(self) -> str """
        return ""

    def get_local(self): # real signature unknown; restored from __doc__
        """ get_local(self) -> str """
        return ""

    def get_mode(self): # real signature unknown; restored from __doc__
        """ get_mode(self) -> NM.IPTunnelMode """
        pass

    def get_mtu(self): # real signature unknown; restored from __doc__
        """ get_mtu(self) -> int """
        return 0

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_output_key(self): # real signature unknown; restored from __doc__
        """ get_output_key(self) -> str """
        return ""

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> str """
        return ""

    def get_path_mtu_discovery(self): # real signature unknown; restored from __doc__
        """ get_path_mtu_discovery(self) -> bool """
        return False

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_remote(self): # real signature unknown; restored from __doc__
        """ get_remote(self) -> str """
        return ""

    def get_secret_flags(self, secret_name, out_flags): # real signature unknown; restored from __doc__
        """ get_secret_flags(self, secret_name:str, out_flags:NM.SettingSecretFlags) -> bool """
        return False

    def get_tos(self): # real signature unknown; restored from __doc__
        """ get_tos(self) -> int """
        return 0

    def get_ttl(self): # real signature unknown; restored from __doc__
        """ get_ttl(self) -> int """
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

    def lookup_type(self, name): # real signature unknown; restored from __doc__
        """ lookup_type(name:str) -> GType """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> NM.Setting """
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

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_secret_flags(self, secret_name, flags): # real signature unknown; restored from __doc__
        """ set_secret_flags(self, secret_name:str, flags:NM.SettingSecretFlags) -> bool """
        return False

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

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def verify(self, connection=None): # real signature unknown; restored from __doc__
        """ verify(self, connection:NM.Connection=None) -> bool """
        return False

    def verify_secrets(self, connection=None): # real signature unknown; restored from __doc__
        """ verify_secrets(self, connection:NM.Connection=None) -> bool """
        return False

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fb9b805afd0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SettingIPTunnel), '__module__': 'gi.repository.NM', '__gtype__': <GType NMSettingIPTunnel (94741104484384)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_encapsulation_limit': gi.FunctionInfo(get_encapsulation_limit), 'get_flags': gi.FunctionInfo(get_flags), 'get_flow_label': gi.FunctionInfo(get_flow_label), 'get_input_key': gi.FunctionInfo(get_input_key), 'get_local': gi.FunctionInfo(get_local), 'get_mode': gi.FunctionInfo(get_mode), 'get_mtu': gi.FunctionInfo(get_mtu), 'get_output_key': gi.FunctionInfo(get_output_key), 'get_parent': gi.FunctionInfo(get_parent), 'get_path_mtu_discovery': gi.FunctionInfo(get_path_mtu_discovery), 'get_remote': gi.FunctionInfo(get_remote), 'get_tos': gi.FunctionInfo(get_tos), 'get_ttl': gi.FunctionInfo(get_ttl), 'parent': <property object at 0x7fb9b84f3ea0>})"
    __gdoc__ = 'Object NMSettingIPTunnel\n\nProperties from NMSettingIPTunnel:\n  parent -> gchararray: \n    \n  mode -> guint: \n    \n  local -> gchararray: \n    \n  remote -> gchararray: \n    \n  ttl -> guint: \n    \n  tos -> guint: \n    \n  path-mtu-discovery -> gboolean: \n    \n  input-key -> gchararray: \n    \n  output-key -> gchararray: \n    \n  encapsulation-limit -> guint: \n    \n  flow-label -> guint: \n    \n  mtu -> guint: \n    \n  flags -> guint: \n    \n\nProperties from NMSetting:\n  name -> gchararray: \n    \n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType NMSettingIPTunnel (94741104484384)>'
    __info__ = ObjectInfo(SettingIPTunnel)


