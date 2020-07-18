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


from .WidgetsSourceListItem import WidgetsSourceListItem

class WidgetsSourceListExpandableItem(WidgetsSourceListItem):
    """
    :Constructors:
    
    ::
    
        WidgetsSourceListExpandableItem(**properties)
        new(name:str) -> Granite.WidgetsSourceListExpandableItem
    """
    def add(self, item): # real signature unknown; restored from __doc__
        """ add(self, item:Granite.WidgetsSourceListItem) """
        pass

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def collapse_all(self, inclusive, recursive): # real signature unknown; restored from __doc__
        """ collapse_all(self, inclusive:bool, recursive:bool) """
        pass

    def collapse_with_parents(self): # real signature unknown; restored from __doc__
        """ collapse_with_parents(self) """
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

    def contains(self, item): # real signature unknown; restored from __doc__
        """ contains(self, item:Granite.WidgetsSourceListItem) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_get_context_menu(self, *args, **kwargs): # real signature unknown
        """ get_context_menu(self) -> Gtk.Menu """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def expand_all(self, inclusive, recursive): # real signature unknown; restored from __doc__
        """ expand_all(self, inclusive:bool, recursive:bool) """
        pass

    def expand_with_parents(self): # real signature unknown; restored from __doc__
        """ expand_with_parents(self) """
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

    def get_activatable(self): # real signature unknown; restored from __doc__
        """ get_activatable(self) -> Gio.Icon """
        pass

    def get_activatable_tooltip(self): # real signature unknown; restored from __doc__
        """ get_activatable_tooltip(self) -> str """
        return ""

    def get_badge(self): # real signature unknown; restored from __doc__
        """ get_badge(self) -> str """
        return ""

    def get_children(self): # real signature unknown; restored from __doc__
        """ get_children(self) -> Gee.Collection """
        pass

    def get_collapsible(self): # real signature unknown; restored from __doc__
        """ get_collapsible(self) -> bool """
        return False

    def get_context_menu(self): # real signature unknown; restored from __doc__
        """ get_context_menu(self) -> Gtk.Menu """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_editable(self): # real signature unknown; restored from __doc__
        """ get_editable(self) -> bool """
        return False

    def get_expanded(self): # real signature unknown; restored from __doc__
        """ get_expanded(self) -> bool """
        return False

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon """
        pass

    def get_markup(self): # real signature unknown; restored from __doc__
        """ get_markup(self) -> str """
        return ""

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_n_children(self): # real signature unknown; restored from __doc__
        """ get_n_children(self) -> int """
        return 0

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Granite.WidgetsSourceListExpandableItem """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_selectable(self): # real signature unknown; restored from __doc__
        """ get_selectable(self) -> bool """
        return False

    def get_tooltip(self): # real signature unknown; restored from __doc__
        """ get_tooltip(self) -> str """
        return ""

    def get_visible(self): # real signature unknown; restored from __doc__
        """ get_visible(self) -> bool """
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

    def new(self, name): # real signature unknown; restored from __doc__
        """ new(name:str) -> Granite.WidgetsSourceListExpandableItem """
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

    def remove(self, item): # real signature unknown; restored from __doc__
        """ remove(self, item:Granite.WidgetsSourceListItem) """
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

    def set_activatable(self, value): # real signature unknown; restored from __doc__
        """ set_activatable(self, value:Gio.Icon) """
        pass

    def set_activatable_tooltip(self, value): # real signature unknown; restored from __doc__
        """ set_activatable_tooltip(self, value:str) """
        pass

    def set_badge(self, value): # real signature unknown; restored from __doc__
        """ set_badge(self, value:str) """
        pass

    def set_collapsible(self, value): # real signature unknown; restored from __doc__
        """ set_collapsible(self, value:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_editable(self, value): # real signature unknown; restored from __doc__
        """ set_editable(self, value:bool) """
        pass

    def set_expanded(self, value): # real signature unknown; restored from __doc__
        """ set_expanded(self, value:bool) """
        pass

    def set_icon(self, value): # real signature unknown; restored from __doc__
        """ set_icon(self, value:Gio.Icon) """
        pass

    def set_markup(self, value=None): # real signature unknown; restored from __doc__
        """ set_markup(self, value:str=None) """
        pass

    def set_name(self, value): # real signature unknown; restored from __doc__
        """ set_name(self, value:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_selectable(self, value): # real signature unknown; restored from __doc__
        """ set_selectable(self, value:bool) """
        pass

    def set_tooltip(self, value=None): # real signature unknown; restored from __doc__
        """ set_tooltip(self, value:str=None) """
        pass

    def set_visible(self, value): # real signature unknown; restored from __doc__
        """ set_visible(self, value:bool) """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f832efec4e0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(WidgetsSourceListExpandableItem), '__module__': 'gi.repository.Granite', '__gtype__': <GType GraniteWidgetsSourceListExpandableItem (31722416)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'contains': gi.FunctionInfo(contains), 'add': gi.FunctionInfo(add), 'remove': gi.FunctionInfo(remove), 'clear': gi.FunctionInfo(clear), 'expand_all': gi.FunctionInfo(expand_all), 'collapse_all': gi.FunctionInfo(collapse_all), 'expand_with_parents': gi.FunctionInfo(expand_with_parents), 'collapse_with_parents': gi.FunctionInfo(collapse_with_parents), 'get_collapsible': gi.FunctionInfo(get_collapsible), 'set_collapsible': gi.FunctionInfo(set_collapsible), 'get_expanded': gi.FunctionInfo(get_expanded), 'set_expanded': gi.FunctionInfo(set_expanded), 'get_n_children': gi.FunctionInfo(get_n_children), 'get_children': gi.FunctionInfo(get_children), 'parent_instance': <property object at 0x7f832ef8ac78>, 'priv': <property object at 0x7f832ef8acc8>})"
    __gdoc__ = 'Object GraniteWidgetsSourceListExpandableItem\n\nSignals from GraniteWidgetsSourceListExpandableItem:\n  toggled ()\n  child-added (GraniteWidgetsSourceListItem)\n  child-removed (GraniteWidgetsSourceListItem)\n\nProperties from GraniteWidgetsSourceListExpandableItem:\n  collapsible -> gboolean: collapsible\n    collapsible\n  expanded -> gboolean: expanded\n    expanded\n  n-children -> guint: n-children\n    n-children\n  children -> GeeCollection: children\n    children\n\nSignals from GraniteWidgetsSourceListItem:\n  action-activated ()\n  edited (gchararray)\n  activated ()\n\nProperties from GraniteWidgetsSourceListItem:\n  parent -> GraniteWidgetsSourceListExpandableItem: parent\n    parent\n  name -> gchararray: name\n    name\n  tooltip -> gchararray: tooltip\n    tooltip\n  markup -> gchararray: markup\n    markup\n  badge -> gchararray: badge\n    badge\n  editable -> gboolean: editable\n    editable\n  visible -> gboolean: visible\n    visible\n  selectable -> gboolean: selectable\n    selectable\n  icon -> GIcon: icon\n    icon\n  activatable -> GIcon: activatable\n    activatable\n  activatable-tooltip -> gchararray: activatable-tooltip\n    activatable-tooltip\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GraniteWidgetsSourceListExpandableItem (31722416)>'
    __info__ = ObjectInfo(WidgetsSourceListExpandableItem)


