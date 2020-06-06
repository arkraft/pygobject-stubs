# encoding: utf-8
# module gi.repository.Modulemd
# from /usr/lib64/girepository-1.0/Modulemd-1.0.typelib
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


from .Component import Component

class ComponentRpm(Component):
    """
    :Constructors:
    
    ::
    
        ComponentRpm(**properties)
        new(key:str) -> Modulemd.ComponentRpm
    """
    def add_buildafter(self, key): # real signature unknown; restored from __doc__
        """ add_buildafter(self, key:str) """
        pass

    def add_multilib_arch(self, arch): # real signature unknown; restored from __doc__
        """ add_multilib_arch(self, arch:str) """
        pass

    def add_restricted_arch(self, arch): # real signature unknown; restored from __doc__
        """ add_restricted_arch(self, arch:str) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_arches(self): # real signature unknown; restored from __doc__
        """ clear_arches(self) """
        pass

    def clear_buildafter(self): # real signature unknown; restored from __doc__
        """ clear_buildafter(self) """
        pass

    def clear_multilib_arches(self): # real signature unknown; restored from __doc__
        """ clear_multilib_arches(self) """
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

    def copy(self, key=None): # real signature unknown; restored from __doc__
        """ copy(self, key:str=None) -> Modulemd.Component """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_copy(self, *args, **kwargs): # real signature unknown
        """ copy(self, key:str=None) -> Modulemd.Component """
        pass

    def do_equals(self, *args, **kwargs): # real signature unknown
        """ equals(self, self_2:Modulemd.Component) -> bool """
        pass

    def do_get_name(self, *args, **kwargs): # real signature unknown
        """ get_name(self) -> str """
        pass

    def do_set_name(self, *args, **kwargs): # real signature unknown
        """ set_name(self, name:str=None) """
        pass

    def do_validate(self, *args, **kwargs): # real signature unknown
        """ validate(self) -> bool """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def equals(self, self_2): # real signature unknown; restored from __doc__
        """ equals(self, self_2:Modulemd.Component) -> bool """
        return False

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

    def get_arches(self): # real signature unknown; restored from __doc__
        """ get_arches(self) -> list """
        return []

    def get_buildafter(self): # real signature unknown; restored from __doc__
        """ get_buildafter(self) -> list """
        return []

    def get_buildonly(self): # real signature unknown; restored from __doc__
        """ get_buildonly(self) -> bool """
        return False

    def get_buildorder(self): # real signature unknown; restored from __doc__
        """ get_buildorder(self) -> int """
        return 0

    def get_buildroot(self): # real signature unknown; restored from __doc__
        """ get_buildroot(self) -> bool """
        return False

    def get_cache(self): # real signature unknown; restored from __doc__
        """ get_cache(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_key(self): # real signature unknown; restored from __doc__
        """ get_key(self) -> str """
        return ""

    def get_multilib_arches(self): # real signature unknown; restored from __doc__
        """ get_multilib_arches(self) -> list """
        return []

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_rationale(self): # real signature unknown; restored from __doc__
        """ get_rationale(self) -> str """
        return ""

    def get_ref(self): # real signature unknown; restored from __doc__
        """ get_ref(self) -> str """
        return ""

    def get_repository(self): # real signature unknown; restored from __doc__
        """ get_repository(self) -> str """
        return ""

    def get_srpm_buildroot(self): # real signature unknown; restored from __doc__
        """ get_srpm_buildroot(self) -> bool """
        return False

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

    def new(self, key): # real signature unknown; restored from __doc__
        """ new(key:str) -> Modulemd.ComponentRpm """
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

    def reset_arches(self): # real signature unknown; restored from __doc__
        """ reset_arches(self) """
        pass

    def reset_multilib_arches(self): # real signature unknown; restored from __doc__
        """ reset_multilib_arches(self) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_buildonly(self, buildonly): # real signature unknown; restored from __doc__
        """ set_buildonly(self, buildonly:bool) """
        pass

    def set_buildorder(self, buildorder): # real signature unknown; restored from __doc__
        """ set_buildorder(self, buildorder:int) """
        pass

    def set_buildroot(self, buildroot): # real signature unknown; restored from __doc__
        """ set_buildroot(self, buildroot:bool) """
        pass

    def set_cache(self, cache=None): # real signature unknown; restored from __doc__
        """ set_cache(self, cache:str=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_name(self, name=None): # real signature unknown; restored from __doc__
        """ set_name(self, name:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_rationale(self, rationale=None): # real signature unknown; restored from __doc__
        """ set_rationale(self, rationale:str=None) """
        pass

    def set_ref(self, ref=None): # real signature unknown; restored from __doc__
        """ set_ref(self, ref:str=None) """
        pass

    def set_repository(self, repository=None): # real signature unknown; restored from __doc__
        """ set_repository(self, repository:str=None) """
        pass

    def set_srpm_buildroot(self, srpm_buildroot): # real signature unknown; restored from __doc__
        """ set_srpm_buildroot(self, srpm_buildroot:bool) """
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

    def validate(self): # real signature unknown; restored from __doc__
        """ validate(self) -> bool """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f723f1d53d0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(ComponentRpm), '__module__': 'gi.repository.Modulemd', '__gtype__': <GType ModulemdComponentRpm (94446540133888)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_multilib_arch': gi.FunctionInfo(add_multilib_arch), 'add_restricted_arch': gi.FunctionInfo(add_restricted_arch), 'clear_arches': gi.FunctionInfo(clear_arches), 'clear_multilib_arches': gi.FunctionInfo(clear_multilib_arches), 'get_arches': gi.FunctionInfo(get_arches), 'get_buildroot': gi.FunctionInfo(get_buildroot), 'get_cache': gi.FunctionInfo(get_cache), 'get_multilib_arches': gi.FunctionInfo(get_multilib_arches), 'get_ref': gi.FunctionInfo(get_ref), 'get_repository': gi.FunctionInfo(get_repository), 'get_srpm_buildroot': gi.FunctionInfo(get_srpm_buildroot), 'reset_arches': gi.FunctionInfo(reset_arches), 'reset_multilib_arches': gi.FunctionInfo(reset_multilib_arches), 'set_buildroot': gi.FunctionInfo(set_buildroot), 'set_cache': gi.FunctionInfo(set_cache), 'set_ref': gi.FunctionInfo(set_ref), 'set_repository': gi.FunctionInfo(set_repository), 'set_srpm_buildroot': gi.FunctionInfo(set_srpm_buildroot)})"
    __gdoc__ = "Object ModulemdComponentRpm\n\nProperties from ModulemdComponentRpm:\n  ref -> gchararray: Ref\n    The commit ID in the SCM repository.\n  repository -> gchararray: Repository\n    The URI of the SCM repository.\n  cache -> gchararray: Cache\n    The lookaside cache URL.\n  buildroot -> gboolean: Buildroot\n    Whether the packages listed in this module's buildroot profile will be installed into the buildroot of any component built in subsequent buildorder/buildafter batches.\n  srpm-buildroot -> gboolean: SrpmBuildroot\n    Whether the packages listed in this module's srpm-buildroot profile will be installed into the buildroot when performing the buildSRPMfromSCM step in subsequent buildorder/buildafter batches.\n\nProperties from ModulemdComponent:\n  buildonly -> gboolean: Buildonly\n    Whether the artifacts produced by this component are intended only for building this module.\n  buildorder -> gint64: Buildorder\n    The order this component should be built relative to others.\n  name -> gchararray: Name\n    The name of the component. This is the real name of the component and may differ from the key used to associate this component with the ModuleStream.\n  rationale -> gchararray: Rationale\n    A description of the reason this component is part of the module stream.\n\nSignals from GObject:\n  notify (GParam)\n\n"
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType ModulemdComponentRpm (94446540133888)>'
    __info__ = ObjectInfo(ComponentRpm)

