# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-3.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Atk as __gi_repository_Atk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gobject as __gobject


from .RecentChooser import RecentChooser

class RecentAction(__gi_overrides_Gtk.Action, RecentChooser):
    """
    :Constructors:
    
    ::
    
        RecentAction(**properties)
        new(name:str, label:str=None, tooltip:str=None, stock_id:str=None) -> Gtk.Action
        new_for_manager(name:str, label:str=None, tooltip:str=None, stock_id:str=None, manager:Gtk.RecentManager=None) -> Gtk.Action
    """
    def activate(self): # real signature unknown; restored from __doc__
        """ activate(self) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def add_filter(self, filter): # real signature unknown; restored from __doc__
        """ add_filter(self, filter:Gtk.RecentFilter) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def block_activate(self): # real signature unknown; restored from __doc__
        """ block_activate(self) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def compat_control(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def connect(self, *args, **kwargs): # real signature unknown
        pass

    def connect_accelerator(self): # real signature unknown; restored from __doc__
        """ connect_accelerator(self) """
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

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def create_icon(self, icon_size): # real signature unknown; restored from __doc__
        """ create_icon(self, icon_size:int) -> Gtk.Widget """
        pass

    def create_menu(self): # real signature unknown; restored from __doc__
        """ create_menu(self) -> Gtk.Widget """
        pass

    def create_menu_item(self): # real signature unknown; restored from __doc__
        """ create_menu_item(self) -> Gtk.Widget """
        pass

    def create_tool_item(self): # real signature unknown; restored from __doc__
        """ create_tool_item(self) -> Gtk.Widget """
        pass

    def custom_finished(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_finished(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_end(self, builder, child=None, tagname, data=None): # real signature unknown; restored from __doc__
        """ custom_tag_end(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str, data=None) """
        pass

    def custom_tag_start(self, builder, child=None, tagname): # real signature unknown; restored from __doc__
        """ custom_tag_start(self, builder:Gtk.Builder, child:GObject.Object=None, tagname:str) -> bool, parser:GLib.MarkupParser, data """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_accelerator(self): # real signature unknown; restored from __doc__
        """ disconnect_accelerator(self) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self) """
        pass

    def do_connect_proxy(self, *args, **kwargs): # real signature unknown
        """ connect_proxy(self, proxy:Gtk.Widget) """
        pass

    def do_create_menu(self, *args, **kwargs): # real signature unknown
        """ create_menu(self) -> Gtk.Widget """
        pass

    def do_create_menu_item(self, *args, **kwargs): # real signature unknown
        """ create_menu_item(self) -> Gtk.Widget """
        pass

    def do_create_tool_item(self, *args, **kwargs): # real signature unknown
        """ create_tool_item(self) -> Gtk.Widget """
        pass

    def do_disconnect_proxy(self, *args, **kwargs): # real signature unknown
        """ disconnect_proxy(self, proxy:Gtk.Widget) """
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

    def get_accel_closure(self): # real signature unknown; restored from __doc__
        """ get_accel_closure(self) -> GObject.Closure """
        pass

    def get_accel_path(self): # real signature unknown; restored from __doc__
        """ get_accel_path(self) -> str """
        return ""

    def get_always_show_image(self): # real signature unknown; restored from __doc__
        """ get_always_show_image(self) -> bool """
        return False

    def get_current_item(self): # real signature unknown; restored from __doc__
        """ get_current_item(self) -> Gtk.RecentInfo """
        pass

    def get_current_uri(self): # real signature unknown; restored from __doc__
        """ get_current_uri(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_filter(self): # real signature unknown; restored from __doc__
        """ get_filter(self) -> Gtk.RecentFilter """
        pass

    def get_gicon(self): # real signature unknown; restored from __doc__
        """ get_gicon(self) -> Gio.Icon """
        pass

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_is_important(self): # real signature unknown; restored from __doc__
        """ get_is_important(self) -> bool """
        return False

    def get_items(self): # real signature unknown; restored from __doc__
        """ get_items(self) -> list """
        return []

    def get_label(self): # real signature unknown; restored from __doc__
        """ get_label(self) -> str """
        return ""

    def get_limit(self): # real signature unknown; restored from __doc__
        """ get_limit(self) -> int """
        return 0

    def get_local_only(self): # real signature unknown; restored from __doc__
        """ get_local_only(self) -> bool """
        return False

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_proxies(self): # real signature unknown; restored from __doc__
        """ get_proxies(self) -> list """
        return []

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_select_multiple(self): # real signature unknown; restored from __doc__
        """ get_select_multiple(self) -> bool """
        return False

    def get_sensitive(self): # real signature unknown; restored from __doc__
        """ get_sensitive(self) -> bool """
        return False

    def get_short_label(self): # real signature unknown; restored from __doc__
        """ get_short_label(self) -> str """
        return ""

    def get_show_icons(self): # real signature unknown; restored from __doc__
        """ get_show_icons(self) -> bool """
        return False

    def get_show_not_found(self): # real signature unknown; restored from __doc__
        """ get_show_not_found(self) -> bool """
        return False

    def get_show_numbers(self): # real signature unknown; restored from __doc__
        """ get_show_numbers(self) -> bool """
        return False

    def get_show_private(self): # real signature unknown; restored from __doc__
        """ get_show_private(self) -> bool """
        return False

    def get_show_tips(self): # real signature unknown; restored from __doc__
        """ get_show_tips(self) -> bool """
        return False

    def get_sort_type(self): # real signature unknown; restored from __doc__
        """ get_sort_type(self) -> Gtk.RecentSortType """
        pass

    def get_stock_id(self): # real signature unknown; restored from __doc__
        """ get_stock_id(self) -> str """
        return ""

    def get_tooltip(self): # real signature unknown; restored from __doc__
        """ get_tooltip(self) -> str """
        return ""

    def get_uris(self): # real signature unknown; restored from __doc__
        """ get_uris(self) -> list, length:int """
        return []

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
        return False

    def get_visible_horizontal(self): # real signature unknown; restored from __doc__
        """ get_visible_horizontal(self) -> bool """
        return False

    def get_visible_vertical(self): # real signature unknown; restored from __doc__
        """ get_visible_vertical(self) -> bool """
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

    def is_sensitive(self): # real signature unknown; restored from __doc__
        """ is_sensitive(self) -> bool """
        return False

    def is_visible(self): # real signature unknown; restored from __doc__
        """ is_visible(self) -> bool """
        return False

    def list_filters(self): # real signature unknown; restored from __doc__
        """ list_filters(self) -> list """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, name, label=None, tooltip=None, stock_id=None): # real signature unknown; restored from __doc__
        """ new(name:str, label:str=None, tooltip:str=None, stock_id:str=None) -> Gtk.Action """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_for_manager(self, name, label=None, tooltip=None, stock_id=None, manager=None): # real signature unknown; restored from __doc__
        """ new_for_manager(name:str, label:str=None, tooltip:str=None, stock_id:str=None, manager:Gtk.RecentManager=None) -> Gtk.Action """
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

    def parser_finished(self, builder): # real signature unknown; restored from __doc__
        """ parser_finished(self, builder:Gtk.Builder) """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def remove_filter(self, filter): # real signature unknown; restored from __doc__
        """ remove_filter(self, filter:Gtk.RecentFilter) """
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

    def select_all(self): # real signature unknown; restored from __doc__
        """ select_all(self) """
        pass

    def select_uri(self, uri): # real signature unknown; restored from __doc__
        """ select_uri(self, uri:str) -> bool """
        return False

    def set_accel_group(self, accel_group=None): # real signature unknown; restored from __doc__
        """ set_accel_group(self, accel_group:Gtk.AccelGroup=None) """
        pass

    def set_accel_path(self, accel_path): # real signature unknown; restored from __doc__
        """ set_accel_path(self, accel_path:str) """
        pass

    def set_always_show_image(self, always_show): # real signature unknown; restored from __doc__
        """ set_always_show_image(self, always_show:bool) """
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_current_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_current_uri(self, uri:str) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_filter(self, filter=None): # real signature unknown; restored from __doc__
        """ set_filter(self, filter:Gtk.RecentFilter=None) """
        pass

    def set_gicon(self, icon): # real signature unknown; restored from __doc__
        """ set_gicon(self, icon:Gio.Icon) """
        pass

    def set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ set_icon_name(self, icon_name:str) """
        pass

    def set_is_important(self, is_important): # real signature unknown; restored from __doc__
        """ set_is_important(self, is_important:bool) """
        pass

    def set_label(self, label): # real signature unknown; restored from __doc__
        """ set_label(self, label:str) """
        pass

    def set_limit(self, limit): # real signature unknown; restored from __doc__
        """ set_limit(self, limit:int) """
        pass

    def set_local_only(self, local_only): # real signature unknown; restored from __doc__
        """ set_local_only(self, local_only:bool) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_select_multiple(self, select_multiple): # real signature unknown; restored from __doc__
        """ set_select_multiple(self, select_multiple:bool) """
        pass

    def set_sensitive(self, sensitive): # real signature unknown; restored from __doc__
        """ set_sensitive(self, sensitive:bool) """
        pass

    def set_short_label(self, short_label): # real signature unknown; restored from __doc__
        """ set_short_label(self, short_label:str) """
        pass

    def set_show_icons(self, show_icons): # real signature unknown; restored from __doc__
        """ set_show_icons(self, show_icons:bool) """
        pass

    def set_show_not_found(self, show_not_found): # real signature unknown; restored from __doc__
        """ set_show_not_found(self, show_not_found:bool) """
        pass

    def set_show_numbers(self, show_numbers): # real signature unknown; restored from __doc__
        """ set_show_numbers(self, show_numbers:bool) """
        pass

    def set_show_private(self, show_private): # real signature unknown; restored from __doc__
        """ set_show_private(self, show_private:bool) """
        pass

    def set_show_tips(self, show_tips): # real signature unknown; restored from __doc__
        """ set_show_tips(self, show_tips:bool) """
        pass

    def set_sort_func(self, sort_func, sort_data=None): # real signature unknown; restored from __doc__
        """ set_sort_func(self, sort_func:Gtk.RecentSortFunc, sort_data=None) """
        pass

    def set_sort_type(self, sort_type): # real signature unknown; restored from __doc__
        """ set_sort_type(self, sort_type:Gtk.RecentSortType) """
        pass

    def set_stock_id(self, stock_id): # real signature unknown; restored from __doc__
        """ set_stock_id(self, stock_id:str) """
        pass

    def set_tooltip(self, tooltip): # real signature unknown; restored from __doc__
        """ set_tooltip(self, tooltip:str) """
        pass

    def set_visible(self, visible): # real signature unknown; restored from __doc__
        """ set_visible(self, visible:bool) """
        pass

    def set_visible_horizontal(self, visible_horizontal): # real signature unknown; restored from __doc__
        """ set_visible_horizontal(self, visible_horizontal:bool) """
        pass

    def set_visible_vertical(self, visible_vertical): # real signature unknown; restored from __doc__
        """ set_visible_vertical(self, visible_vertical:bool) """
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

    def unblock_activate(self): # real signature unknown; restored from __doc__
        """ unblock_activate(self) """
        pass

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unselect_all(self): # real signature unknown; restored from __doc__
        """ unselect_all(self) """
        pass

    def unselect_uri(self, uri): # real signature unknown; restored from __doc__
        """ unselect_uri(self, uri:str) """
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

    def __init__(self, *args, **kwargs): # reliably restored by inspect
        """
        Initializer for a GObject based classes with support for property
                sets through the use of explicit keyword arguments.
        """
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

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    private_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fe82f255a00>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(RecentAction), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkRecentAction (94846038302496)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_for_manager': gi.FunctionInfo(new_for_manager), 'get_show_numbers': gi.FunctionInfo(get_show_numbers), 'set_show_numbers': gi.FunctionInfo(set_show_numbers), 'parent_instance': <property object at 0x7fe830fb2c70>, 'priv': <property object at 0x7fe830fb2d60>})"
    __gdoc__ = 'Object GtkRecentAction\n\nProperties from GtkRecentAction:\n  show-numbers -> gboolean: Show Numbers\n    Whether the items should be displayed with a number\n\nSignals from GtkRecentChooser:\n  selection-changed ()\n  item-activated ()\n\nSignals from GtkAction:\n  activate ()\n\nProperties from GtkAction:\n  name -> gchararray: Name\n    A unique name for the action.\n  label -> gchararray: Label\n    The label used for menu items and buttons that activate this action.\n  short-label -> gchararray: Short label\n    A shorter label that may be used on toolbar buttons.\n  tooltip -> gchararray: Tooltip\n    A tooltip for this action.\n  stock-id -> gchararray: Stock Icon\n    The stock icon displayed in widgets representing this action.\n  icon-name -> gchararray: Icon Name\n    The name of the icon from the icon theme\n  gicon -> GIcon: GIcon\n    The GIcon being displayed\n  visible-horizontal -> gboolean: Visible when horizontal\n    Whether the toolbar item is visible when the toolbar is in a horizontal orientation.\n  visible-vertical -> gboolean: Visible when vertical\n    Whether the toolbar item is visible when the toolbar is in a vertical orientation.\n  visible-overflown -> gboolean: Visible when overflown\n    When TRUE, toolitem proxies for this action are represented in the toolbar overflow menu.\n  is-important -> gboolean: Is important\n    Whether the action is considered important. When TRUE, toolitem proxies for this action show text in GTK_TOOLBAR_BOTH_HORIZ mode.\n  hide-if-empty -> gboolean: Hide if empty\n    When TRUE, empty menu proxies for this action are hidden.\n  sensitive -> gboolean: Sensitive\n    Whether the action is enabled.\n  visible -> gboolean: Visible\n    Whether the action is visible.\n  action-group -> GtkActionGroup: Action Group\n    The GtkActionGroup this GtkAction is associated with, or NULL (for internal use).\n  always-show-image -> gboolean: Always show image\n    Whether the image will always be shown\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkRecentAction (94846038302496)>'
    __info__ = ObjectInfo(RecentAction)


