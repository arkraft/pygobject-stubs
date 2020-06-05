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


class MountOperation(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        MountOperation(**properties)
        new() -> Gio.MountOperation
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

    def do_aborted(self, *args, **kwargs): # real signature unknown
        """ aborted(self) """
        pass

    def do_ask_password(self, *args, **kwargs): # real signature unknown
        """ ask_password(self, message:str, default_user:str, default_domain:str, flags:Gio.AskPasswordFlags) """
        pass

    def do_ask_question(self, *args, **kwargs): # real signature unknown
        """ ask_question(self, message:str, choices:list) """
        pass

    def do_reply(self, *args, **kwargs): # real signature unknown
        """ reply(self, result:Gio.MountOperationResult) """
        pass

    def do_show_processes(self, *args, **kwargs): # real signature unknown
        """ show_processes(self, message:str, processes:list, choices:list) """
        pass

    def do_show_unmount_progress(self, *args, **kwargs): # real signature unknown
        """ show_unmount_progress(self, message:str, time_left:int, bytes_left:int) """
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

    def get_anonymous(self): # real signature unknown; restored from __doc__
        """ get_anonymous(self) -> bool """
        return False

    def get_choice(self): # real signature unknown; restored from __doc__
        """ get_choice(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_domain(self): # real signature unknown; restored from __doc__
        """ get_domain(self) -> str """
        return ""

    def get_is_tcrypt_hidden_volume(self): # real signature unknown; restored from __doc__
        """ get_is_tcrypt_hidden_volume(self) -> bool """
        return False

    def get_is_tcrypt_system_volume(self): # real signature unknown; restored from __doc__
        """ get_is_tcrypt_system_volume(self) -> bool """
        return False

    def get_password(self): # real signature unknown; restored from __doc__
        """ get_password(self) -> str """
        return ""

    def get_password_save(self): # real signature unknown; restored from __doc__
        """ get_password_save(self) -> Gio.PasswordSave """
        pass

    def get_pim(self): # real signature unknown; restored from __doc__
        """ get_pim(self) -> int """
        return 0

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_username(self): # real signature unknown; restored from __doc__
        """ get_username(self) -> str """
        return ""

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

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> Gio.MountOperation """
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

    def reply(self, result): # real signature unknown; restored from __doc__
        """ reply(self, result:Gio.MountOperationResult) """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_anonymous(self, anonymous): # real signature unknown; restored from __doc__
        """ set_anonymous(self, anonymous:bool) """
        pass

    def set_choice(self, choice): # real signature unknown; restored from __doc__
        """ set_choice(self, choice:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_domain(self, domain): # real signature unknown; restored from __doc__
        """ set_domain(self, domain:str) """
        pass

    def set_is_tcrypt_hidden_volume(self, hidden_volume): # real signature unknown; restored from __doc__
        """ set_is_tcrypt_hidden_volume(self, hidden_volume:bool) """
        pass

    def set_is_tcrypt_system_volume(self, system_volume): # real signature unknown; restored from __doc__
        """ set_is_tcrypt_system_volume(self, system_volume:bool) """
        pass

    def set_password(self, password): # real signature unknown; restored from __doc__
        """ set_password(self, password:str) """
        pass

    def set_password_save(self, save): # real signature unknown; restored from __doc__
        """ set_password_save(self, save:Gio.PasswordSave) """
        pass

    def set_pim(self, pim): # real signature unknown; restored from __doc__
        """ set_pim(self, pim:int) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_username(self, username): # real signature unknown; restored from __doc__
        """ set_username(self, username:str) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f28dd310670>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(MountOperation), '__module__': 'gi.repository.Gio', '__gtype__': <GType GMountOperation (94125581932672)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_anonymous': gi.FunctionInfo(get_anonymous), 'get_choice': gi.FunctionInfo(get_choice), 'get_domain': gi.FunctionInfo(get_domain), 'get_is_tcrypt_hidden_volume': gi.FunctionInfo(get_is_tcrypt_hidden_volume), 'get_is_tcrypt_system_volume': gi.FunctionInfo(get_is_tcrypt_system_volume), 'get_password': gi.FunctionInfo(get_password), 'get_password_save': gi.FunctionInfo(get_password_save), 'get_pim': gi.FunctionInfo(get_pim), 'get_username': gi.FunctionInfo(get_username), 'reply': gi.FunctionInfo(reply), 'set_anonymous': gi.FunctionInfo(set_anonymous), 'set_choice': gi.FunctionInfo(set_choice), 'set_domain': gi.FunctionInfo(set_domain), 'set_is_tcrypt_hidden_volume': gi.FunctionInfo(set_is_tcrypt_hidden_volume), 'set_is_tcrypt_system_volume': gi.FunctionInfo(set_is_tcrypt_system_volume), 'set_password': gi.FunctionInfo(set_password), 'set_password_save': gi.FunctionInfo(set_password_save), 'set_pim': gi.FunctionInfo(set_pim), 'set_username': gi.FunctionInfo(set_username), 'do_aborted': gi.VFuncInfo(aborted), 'do_ask_password': gi.VFuncInfo(ask_password), 'do_ask_question': gi.VFuncInfo(ask_question), 'do_reply': gi.VFuncInfo(reply), 'do_show_processes': gi.VFuncInfo(show_processes), 'do_show_unmount_progress': gi.VFuncInfo(show_unmount_progress), 'parent_instance': <property object at 0x7f28ddeb1ea0>, 'priv': <property object at 0x7f28ddeb2040>})"
    __gdoc__ = 'Object GMountOperation\n\nSignals from GMountOperation:\n  ask-password (gchararray, gchararray, gchararray, GAskPasswordFlags)\n  ask-question (gchararray, GStrv)\n  reply (GMountOperationResult)\n  aborted ()\n  show-processes (gchararray, GArray, GStrv)\n  show-unmount-progress (gchararray, gint64, gint64)\n\nProperties from GMountOperation:\n  username -> gchararray: Username\n    The user name\n  password -> gchararray: Password\n    The password\n  anonymous -> gboolean: Anonymous\n    Whether to use an anonymous user\n  domain -> gchararray: Domain\n    The domain of the mount operation\n  password-save -> GPasswordSave: Password save\n    How passwords should be saved\n  choice -> gint: Choice\n    The users choice\n  is-tcrypt-hidden-volume -> gboolean: TCRYPT Hidden Volume\n    Whether to unlock a TCRYPT hidden volume. See https://www.veracrypt.fr/en/Hidden%20Volume.html.\n  is-tcrypt-system-volume -> gboolean: TCRYPT System Volume\n    Whether to unlock a TCRYPT system volume. Only supported for unlocking Windows system volumes. See https://www.veracrypt.fr/en/System%20Encryption.html.\n  pim -> guint: PIM\n    The VeraCrypt PIM value\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GMountOperation (94125581932672)>'
    __info__ = ObjectInfo(MountOperation)


