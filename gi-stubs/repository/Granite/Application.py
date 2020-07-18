# encoding: utf-8
# module gi.repository.Granite
# from /usr/lib/x86_64-linux-gnu/girepository-1.0/Granite-1.0.typelib
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
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class Application(__gi_repository_Gtk.Application):
    """
    :Constructors:
    
    ::
    
        Application(**properties)
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

    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) """
        pass

    def activate_action(self, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ activate_action(self, action_name:str, parameter:GLib.Variant=None) """
        pass

    def add_accelerator(self, accelerator, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ add_accelerator(self, accelerator:str, action_name:str, parameter:GLib.Variant=None) """
        pass

    def add_action(self, action): # real signature unknown; restored from __doc__
        """ add_action(self, action:Gio.Action) """
        pass

    def add_action_entries(self, entries, user_data=None): # real signature unknown; restored from __doc__
        """ add_action_entries(self, entries:list, user_data=None) """
        pass

    def add_main_option(self, long_name, short_name, flags, arg, description, arg_description=None): # real signature unknown; restored from __doc__
        """ add_main_option(self, long_name:str, short_name:int, flags:GLib.OptionFlags, arg:GLib.OptionArg, description:str, arg_description:str=None) """
        pass

    def add_main_option_entries(self, entries): # real signature unknown; restored from __doc__
        """ add_main_option_entries(self, entries:list) """
        pass

    def add_option_group(self, group): # real signature unknown; restored from __doc__
        """ add_option_group(self, group:GLib.OptionGroup) """
        pass

    def add_window(self, window): # real signature unknown; restored from __doc__
        """ add_window(self, window:Gtk.Window) """
        pass

    def bind_busy_property(self, p_object, property): # real signature unknown; restored from __doc__
        """ bind_busy_property(self, object:GObject.Object, property:str) """
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

    def create_appmenu(self, menu): # real signature unknown; restored from __doc__
        """ create_appmenu(self, menu:Gtk.Menu) -> Granite.WidgetsAppMenu """
        pass

    def disconnect(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) """
        pass

    def do_add_platform_data(self, *args, **kwargs): # real signature unknown
        """ add_platform_data(self, builder:GLib.VariantBuilder) """
        pass

    def do_after_emit(self, *args, **kwargs): # real signature unknown
        """ after_emit(self, platform_data:GLib.Variant) """
        pass

    def do_before_emit(self, *args, **kwargs): # real signature unknown
        """ before_emit(self, platform_data:GLib.Variant) """
        pass

    def do_command_line(self, *args, **kwargs): # real signature unknown
        """ command_line(self, command_line:Gio.ApplicationCommandLine) -> int """
        pass

    def do_dbus_register(self, *args, **kwargs): # real signature unknown
        """ dbus_register(self, connection:Gio.DBusConnection, object_path:str) -> bool """
        pass

    def do_dbus_unregister(self, *args, **kwargs): # real signature unknown
        """ dbus_unregister(self, connection:Gio.DBusConnection, object_path:str) """
        pass

    def do_handle_local_options(self, *args, **kwargs): # real signature unknown
        """ handle_local_options(self, options:GLib.VariantDict) -> int """
        pass

    def do_local_command_line(self, *args, **kwargs): # real signature unknown
        """ local_command_line(self, arguments:list) -> bool, arguments:list, exit_status:int """
        pass

    def do_open(self, *args, **kwargs): # real signature unknown
        """ open(self, files:list, hint:str) """
        pass

    def do_quit_mainloop(self, *args, **kwargs): # real signature unknown
        """ quit_mainloop(self) """
        pass

    def do_run_mainloop(self, *args, **kwargs): # real signature unknown
        """ run_mainloop(self) """
        pass

    def do_set_options(self, *args, **kwargs): # real signature unknown
        """ set_options(self) """
        pass

    def do_show_about(self, *args, **kwargs): # real signature unknown
        """ show_about(self, parent:Gtk.Widget) """
        pass

    def do_shutdown(self, *args, **kwargs): # real signature unknown
        """ shutdown(self) """
        pass

    def do_startup(self, *args, **kwargs): # real signature unknown
        """ startup(self) """
        pass

    def do_window_added(self, *args, **kwargs): # real signature unknown
        """ window_added(self, window:Gtk.Window) """
        pass

    def do_window_removed(self, *args, **kwargs): # real signature unknown
        """ window_removed(self, window:Gtk.Window) """
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

    def get_accels_for_action(self, detailed_action_name): # real signature unknown; restored from __doc__
        """ get_accels_for_action(self, detailed_action_name:str) -> list """
        return []

    def get_actions_for_accel(self, accel): # real signature unknown; restored from __doc__
        """ get_actions_for_accel(self, accel:str) -> list """
        return []

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

    def get_active_window(self): # real signature unknown; restored from __doc__
        """ get_active_window(self) -> Gtk.Window or None """
        pass

    def get_application_id(self): # real signature unknown; restored from __doc__
        """ get_application_id(self) -> str """
        return ""

    def get_app_menu(self): # real signature unknown; restored from __doc__
        """ get_app_menu(self) -> Gio.MenuModel or None """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dbus_connection(self): # real signature unknown; restored from __doc__
        """ get_dbus_connection(self) -> Gio.DBusConnection """
        pass

    def get_dbus_object_path(self): # real signature unknown; restored from __doc__
        """ get_dbus_object_path(self) -> str """
        return ""

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gio.Application """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> Gio.ApplicationFlags """
        pass

    def get_inactivity_timeout(self): # real signature unknown; restored from __doc__
        """ get_inactivity_timeout(self) -> int """
        return 0

    def get_is_busy(self): # real signature unknown; restored from __doc__
        """ get_is_busy(self) -> bool """
        return False

    def get_is_registered(self): # real signature unknown; restored from __doc__
        """ get_is_registered(self) -> bool """
        return False

    def get_is_remote(self): # real signature unknown; restored from __doc__
        """ get_is_remote(self) -> bool """
        return False

    def get_menubar(self): # real signature unknown; restored from __doc__
        """ get_menubar(self) -> Gio.MenuModel """
        pass

    def get_menu_by_id(self, id): # real signature unknown; restored from __doc__
        """ get_menu_by_id(self, id:str) -> Gio.Menu """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_resource_base_path(self): # real signature unknown; restored from __doc__
        """ get_resource_base_path(self) -> str or None """
        return ""

    def get_windows(self): # real signature unknown; restored from __doc__
        """ get_windows(self) -> list """
        return []

    def get_window_by_id(self, id): # real signature unknown; restored from __doc__
        """ get_window_by_id(self, id:int) -> Gtk.Window or None """
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
        # no doc
        pass

    def handler_is_connected(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def handler_unblock(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def handler_unblock_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def has_action(self, action_name): # real signature unknown; restored from __doc__
        """ has_action(self, action_name:str) -> bool """
        return False

    def hold(self): # real signature unknown; restored from __doc__
        """ hold(self) """
        pass

    def id_is_valid(self, application_id): # real signature unknown; restored from __doc__
        """ id_is_valid(application_id:str) -> bool """
        return False

    def inhibit(self, window=None, flags, reason=None): # real signature unknown; restored from __doc__
        """ inhibit(self, window:Gtk.Window=None, flags:Gtk.ApplicationInhibitFlags, reason:str=None) -> int """
        return 0

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

    def is_inhibited(self, flags): # real signature unknown; restored from __doc__
        """ is_inhibited(self, flags:Gtk.ApplicationInhibitFlags) -> bool """
        return False

    def list_actions(self): # real signature unknown; restored from __doc__
        """ list_actions(self) -> list """
        return []

    def list_action_descriptions(self): # real signature unknown; restored from __doc__
        """ list_action_descriptions(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def lookup_action(self, action_name): # real signature unknown; restored from __doc__
        """ lookup_action(self, action_name:str) -> Gio.Action """
        pass

    def mark_busy(self): # real signature unknown; restored from __doc__
        """ mark_busy(self) """
        pass

    def new(self, application_id=None, flags): # real signature unknown; restored from __doc__
        """ new(application_id:str=None, flags:Gio.ApplicationFlags) -> Gtk.Application """
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

    def open(self, files, hint): # real signature unknown; restored from __doc__
        """ open(self, files:list, hint:str) """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def prefers_app_menu(self): # real signature unknown; restored from __doc__
        """ prefers_app_menu(self) -> bool """
        return False

    def query_action(self, action_name): # real signature unknown; restored from __doc__
        """ query_action(self, action_name:str) -> bool, enabled:bool, parameter_type:GLib.VariantType, state_type:GLib.VariantType, state_hint:GLib.Variant, state:GLib.Variant """
        return False

    def quit(self): # real signature unknown; restored from __doc__
        """ quit(self) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def register(self, cancellable=None): # real signature unknown; restored from __doc__
        """ register(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def release(self): # real signature unknown; restored from __doc__
        """ release(self) """
        pass

    def remove_accelerator(self, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ remove_accelerator(self, action_name:str, parameter:GLib.Variant=None) """
        pass

    def remove_action(self, action_name): # real signature unknown; restored from __doc__
        """ remove_action(self, action_name:str) """
        pass

    def remove_window(self, window): # real signature unknown; restored from __doc__
        """ remove_window(self, window:Gtk.Window) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def run(self, args): # real signature unknown; restored from __doc__
        """ run(self, args:list) -> int """
        return 0

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def send_notification(self, id=None, notification): # real signature unknown; restored from __doc__
        """ send_notification(self, id:str=None, notification:Gio.Notification) """
        pass

    def set_accels_for_action(self, detailed_action_name, accels): # real signature unknown; restored from __doc__
        """ set_accels_for_action(self, detailed_action_name:str, accels:list) """
        pass

    def set_action_group(self, action_group=None): # real signature unknown; restored from __doc__
        """ set_action_group(self, action_group:Gio.ActionGroup=None) """
        pass

    def set_application_id(self, application_id=None): # real signature unknown; restored from __doc__
        """ set_application_id(self, application_id:str=None) """
        pass

    def set_app_menu(self, app_menu=None): # real signature unknown; restored from __doc__
        """ set_app_menu(self, app_menu:Gio.MenuModel=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_default(self): # real signature unknown; restored from __doc__
        """ set_default(self) """
        pass

    def set_flags(self, flags): # real signature unknown; restored from __doc__
        """ set_flags(self, flags:Gio.ApplicationFlags) """
        pass

    def set_inactivity_timeout(self, inactivity_timeout): # real signature unknown; restored from __doc__
        """ set_inactivity_timeout(self, inactivity_timeout:int) """
        pass

    def set_menubar(self, menubar=None): # real signature unknown; restored from __doc__
        """ set_menubar(self, menubar:Gio.MenuModel=None) """
        pass

    def set_options(self): # real signature unknown; restored from __doc__
        """ set_options(self) """
        pass

    def set_option_context_description(self, description=None): # real signature unknown; restored from __doc__
        """ set_option_context_description(self, description:str=None) """
        pass

    def set_option_context_parameter_string(self, parameter_string=None): # real signature unknown; restored from __doc__
        """ set_option_context_parameter_string(self, parameter_string:str=None) """
        pass

    def set_option_context_summary(self, summary=None): # real signature unknown; restored from __doc__
        """ set_option_context_summary(self, summary:str=None) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_resource_base_path(self, resource_path=None): # real signature unknown; restored from __doc__
        """ set_resource_base_path(self, resource_path:str=None) """
        pass

    def show_about(self, parent): # real signature unknown; restored from __doc__
        """ show_about(self, parent:Gtk.Widget) """
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
        # no doc
        pass

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def unbind_busy_property(self, p_object, property): # real signature unknown; restored from __doc__
        """ unbind_busy_property(self, object:GObject.Object, property:str) """
        pass

    def uninhibit(self, cookie): # real signature unknown; restored from __doc__
        """ uninhibit(self, cookie:int) """
        pass

    def unmark_busy(self): # real signature unknown; restored from __doc__
        """ unmark_busy(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def watch_closure(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def weak_ref(self, *args, **kwargs): # real signature unknown
        pass

    def withdraw_notification(self, id): # real signature unknown; restored from __doc__
        """ withdraw_notification(self, id:str) """
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

    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        default dir() implementation
        """
        return []

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ default object formatter """
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
        """ helper for pickle """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ helper for pickle """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """
        __sizeof__() -> int
        size of object in memory, in bytes
        """
        return 0

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

    about_artists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_artists_length1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_authors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_authors_length1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_comments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_dlg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_documenters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_documenters_length1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_license = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_license_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    about_translators = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    app_copyright = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    app_icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    app_launcher = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    app_years = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    bug_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_data_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_pkg_data_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_release_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    build_version_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exec_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    granite_application_DEBUG = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    help_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    main_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    program_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    translate_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    options = []
    props = None # (!) real value is '<gi._gi.GProps object at 0x7f832ef35320>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Application), '__module__': 'gi.repository.Granite', '__gtype__': <GType GraniteApplication (31240832)>, '__doc__': None, '__gsignals__': {}, 'run': gi.FunctionInfo(run), 'set_options': gi.FunctionInfo(set_options), 'create_appmenu': gi.FunctionInfo(create_appmenu), 'show_about': gi.FunctionInfo(show_about), 'options': [], 'do_set_options': gi.VFuncInfo(set_options), 'do_show_about': gi.VFuncInfo(show_about), 'parent_instance': <property object at 0x7f832efd8b88>, 'priv': <property object at 0x7f832efd8bd8>, 'build_data_dir': <property object at 0x7f832efd8c28>, 'build_pkg_data_dir': <property object at 0x7f832efd8c78>, 'build_release_name': <property object at 0x7f832efd8cc8>, 'build_version': <property object at 0x7f832efd8d18>, 'build_version_info': <property object at 0x7f832efd8d68>, 'program_name': <property object at 0x7f832efd8db8>, 'exec_name': <property object at 0x7f832efd8e08>, 'app_copyright': <property object at 0x7f832efd8e58>, 'app_years': <property object at 0x7f832efd8ea8>, 'app_icon': <property object at 0x7f832efd8ef8>, 'app_launcher': <property object at 0x7f832efd8f48>, 'main_url': <property object at 0x7f832efd8f98>, 'bug_url': <property object at 0x7f832efdf048>, 'help_url': <property object at 0x7f832efdf098>, 'translate_url': <property object at 0x7f832efdf0e8>, 'about_authors': <property object at 0x7f832efdf138>, 'about_authors_length1': <property object at 0x7f832efdf188>, 'about_documenters': <property object at 0x7f832efdf1d8>, 'about_documenters_length1': <property object at 0x7f832efdf278>, 'about_artists': <property object at 0x7f832efdf2c8>, 'about_artists_length1': <property object at 0x7f832efdf318>, 'about_comments': <property object at 0x7f832efdf368>, 'about_translators': <property object at 0x7f832efdf3b8>, 'about_license': <property object at 0x7f832efdf408>, 'about_license_type': <property object at 0x7f832efdf458>, 'granite_application_DEBUG': <property object at 0x7f832efdf4f8>, 'about_dlg': <property object at 0x7f832efdf548>})"
    __gdoc__ = 'Object GraniteApplication\n\nSignals from GActionGroup:\n  action-added (gchararray)\n  action-removed (gchararray)\n  action-enabled-changed (gchararray, gboolean)\n  action-state-changed (gchararray, GVariant)\n\nSignals from GtkApplication:\n  window-added (GtkWindow)\n  window-removed (GtkWindow)\n\nProperties from GtkApplication:\n  register-session -> gboolean: Register session\n    Register with the session manager\n  app-menu -> GMenuModel: Application menu\n    The GMenuModel for the application menu\n  menubar -> GMenuModel: Menubar\n    The GMenuModel for the menubar\n  active-window -> GtkWindow: Active window\n    The window which most recently had focus\n\nSignals from GActionGroup:\n  action-added (gchararray)\n  action-removed (gchararray)\n  action-enabled-changed (gchararray, gboolean)\n  action-state-changed (gchararray, GVariant)\n\nSignals from GApplication:\n  activate ()\n  startup ()\n  shutdown ()\n  open (gpointer, gint, gchararray)\n  command-line (GApplicationCommandLine) -> gint\n  handle-local-options (GVariantDict) -> gint\n\nProperties from GApplication:\n  application-id -> gchararray: Application identifier\n    The unique identifier for the application\n  flags -> GApplicationFlags: Application flags\n    Flags specifying the behaviour of the application\n  resource-base-path -> gchararray: Resource base path\n    The base resource path for the application\n  is-registered -> gboolean: Is registered\n    If g_application_register() has been called\n  is-remote -> gboolean: Is remote\n    If this application instance is remote\n  inactivity-timeout -> guint: Inactivity timeout\n    Time (ms) to stay alive after becoming idle\n  action-group -> GActionGroup: Action group\n    The group of actions that the application exports\n  is-busy -> gboolean: Is busy\n    If this application is currently marked busy\n\nSignals from GActionGroup:\n  action-added (gchararray)\n  action-removed (gchararray)\n  action-enabled-changed (gchararray, gboolean)\n  action-state-changed (gchararray, GVariant)\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GraniteApplication (31240832)>'
    __info__ = ObjectInfo(Application)


