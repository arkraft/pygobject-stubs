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


from .ActionGroup import ActionGroup

class SimpleActionGroup(__gi_overrides_GObject.Object, ActionGroup, __gi_overrides_Gio.ActionMap):
    """
    :Constructors:
    
    ::
    
        SimpleActionGroup(**properties)
        new() -> Gio.SimpleActionGroup
    """
    def action_added(self, action_name): # real signature unknown; restored from __doc__
        """ action_added(self, action_name:str) """
        pass

    def action_enabled_changed(self, action_name, enabled): # real signature unknown; restored from __doc__
        """ action_enabled_changed(self, action_name:str, enabled:bool) """
        pass

    def action_removed(self, action_name): # real signature unknown; restored from __doc__
        """ action_removed(self, action_name:str) """
        pass

    def action_state_changed(self, action_name, state): # real signature unknown; restored from __doc__
        """ action_state_changed(self, action_name:str, state:GLib.Variant) """
        pass

    def activate_action(self, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ activate_action(self, action_name:str, parameter:GLib.Variant=None) """
        pass

    def add_action(self, action): # real signature unknown; restored from __doc__
        """ add_action(self, action:Gio.Action) """
        pass

    def add_action_entries(self, entries, user_data=None): # reliably restored by inspect
        """
        The add_action_entries() method is a convenience function for creating
                multiple Gio.SimpleAction instances and adding them to a Gio.ActionMap.
                Each action is constructed as per one entry.
        
                :param list entries:
                    List of entry tuples for add_action() method. The entry tuple can
                    vary in size with the following information:
        
                        * The name of the action. Must be specified.
                        * The callback to connect to the "activate" signal of the
                          action. Since GLib 2.40, this can be None for stateful
                          actions, in which case the default handler is used. For
                          boolean-stated actions with no parameter, this is a toggle.
                          For other state types (and parameter type equal to the state
                          type) this will be a function that just calls change_state
                          (which you should provide).
                        * The type of the parameter that must be passed to the activate
                          function for this action, given as a single GLib.Variant type
                          string (or None for no parameter)
                        * The initial state for this action, given in GLib.Variant text
                          format. The state is parsed with no extra type information, so
                          type tags must be added to the string if they are necessary.
                          Stateless actions should give None here.
                        * The callback to connect to the "change-state" signal of the
                          action. All stateful actions should provide a handler here;
                          stateless actions should not.
        
                :param user_data:
                    The user data for signal connections, or None
        """
        pass

    def add_entries(self, entries, user_data=None): # real signature unknown; restored from __doc__
        """ add_entries(self, entries:list, user_data=None) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def change_action_state(self, action_name, value): # real signature unknown; restored from __doc__
        """ change_action_state(self, action_name:str, value:GLib.Variant) """
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

    def get_action_enabled(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_enabled(self, action_name:str) -> bool """
        return False

    def get_action_parameter_type(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_parameter_type(self, action_name:str) -> GLib.VariantType or None """
        pass

    def get_action_state(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state(self, action_name:str) -> GLib.Variant or None """
        pass

    def get_action_state_hint(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state_hint(self, action_name:str) -> GLib.Variant or None """
        pass

    def get_action_state_type(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state_type(self, action_name:str) -> GLib.VariantType or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
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

    def has_action(self, action_name): # real signature unknown; restored from __doc__
        """ has_action(self, action_name:str) -> bool """
        return False

    def insert(self, action): # real signature unknown; restored from __doc__
        """ insert(self, action:Gio.Action) """
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

    def list_actions(self): # real signature unknown; restored from __doc__
        """ list_actions(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lookup(self, action_name): # real signature unknown; restored from __doc__
        """ lookup(self, action_name:str) -> Gio.Action """
        pass

    def lookup_action(self, action_name): # real signature unknown; restored from __doc__
        """ lookup_action(self, action_name:str) -> Gio.Action """
        pass

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gio.SimpleActionGroup """
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

    def query_action(self, action_name): # real signature unknown; restored from __doc__
        """ query_action(self, action_name:str) -> bool, enabled:bool, parameter_type:GLib.VariantType, state_type:GLib.VariantType, state_hint:GLib.Variant, state:GLib.Variant """
        return False

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove(self, action_name): # real signature unknown; restored from __doc__
        """ remove(self, action_name:str) """
        pass

    def remove_action(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action(self, action_name:str) """
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

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f4b870fb280>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(SimpleActionGroup), '__module__': 'gi.repository.Gio', '__gtype__': <GType GSimpleActionGroup (94269257326368)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'add_entries': gi.FunctionInfo(add_entries), 'insert': gi.FunctionInfo(insert), 'lookup': gi.FunctionInfo(lookup), 'remove': gi.FunctionInfo(remove), 'parent_instance': <property object at 0x7f4b87fb56d0>, 'priv': <property object at 0x7f4b87fb57c0>})"
    __gdoc__ = 'Object GSimpleActionGroup\n\nSignals from GActionGroup:\n  action-added (gchararray)\n  action-removed (gchararray)\n  action-enabled-changed (gchararray, gboolean)\n  action-state-changed (gchararray, GVariant)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GSimpleActionGroup (94269257326368)>'
    __info__ = ObjectInfo(SimpleActionGroup)


