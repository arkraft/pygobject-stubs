# encoding: utf-8
# module gi.repository.Dazzle
# from /usr/lib64/girepository-1.0/Dazzle-1.0.typelib
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
import gi.overrides.Gio as __gi_overrides_Gio
import gi.overrides.GObject as __gi_overrides_GObject
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gio as __gi_repository_Gio
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class Suggestion(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Suggestion(**properties)
        new() -> Dazzle.Suggestion
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

    def do_get_icon(self, *args, **kwargs): # real signature unknown
        """ get_icon(self) -> Gio.Icon or None """
        pass

    def do_get_icon_surface(self, *args, **kwargs): # real signature unknown
        """ get_icon_surface(self, widget:Gtk.Widget) -> cairo.Surface or None """
        pass

    def do_get_secondary_icon(self, *args, **kwargs): # real signature unknown
        """ get_secondary_icon(self) -> Gio.Icon or None """
        pass

    def do_get_secondary_icon_surface(self, *args, **kwargs): # real signature unknown
        """ get_secondary_icon_surface(self, widget:Gtk.Widget) -> cairo.Surface or None """
        pass

    def do_replace_typed_text(self, *args, **kwargs): # real signature unknown
        """ replace_typed_text(self, typed_text:str) -> str or None """
        pass

    def do_suggest_suffix(self, *args, **kwargs): # real signature unknown
        """ suggest_suffix(self, typed_text:str) -> str or None """
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

    def get_icon(self): # real signature unknown; restored from __doc__
        """ get_icon(self) -> Gio.Icon or None """
        pass

    def get_icon_name(self): # real signature unknown; restored from __doc__
        """ get_icon_name(self) -> str """
        return ""

    def get_icon_surface(self, widget): # real signature unknown; restored from __doc__
        """ get_icon_surface(self, widget:Gtk.Widget) -> cairo.Surface or None """
        pass

    def get_id(self): # real signature unknown; restored from __doc__
        """ get_id(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_secondary_icon(self): # real signature unknown; restored from __doc__
        """ get_secondary_icon(self) -> Gio.Icon or None """
        pass

    def get_secondary_icon_name(self): # real signature unknown; restored from __doc__
        """ get_secondary_icon_name(self) -> str """
        return ""

    def get_secondary_icon_surface(self, widget): # real signature unknown; restored from __doc__
        """ get_secondary_icon_surface(self, widget:Gtk.Widget) -> cairo.Surface or None """
        pass

    def get_subtitle(self): # real signature unknown; restored from __doc__
        """ get_subtitle(self) -> str """
        return ""

    def get_title(self): # real signature unknown; restored from __doc__
        """ get_title(self) -> str """
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
        """ new() -> Dazzle.Suggestion """
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

    def replace_typed_text(self, typed_text): # real signature unknown; restored from __doc__
        """ replace_typed_text(self, typed_text:str) -> str or None """
        return ""

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ set_icon_name(self, icon_name:str) """
        pass

    def set_id(self, id): # real signature unknown; restored from __doc__
        """ set_id(self, id:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_secondary_icon_name(self, icon_name): # real signature unknown; restored from __doc__
        """ set_secondary_icon_name(self, icon_name:str) """
        pass

    def set_subtitle(self, subtitle): # real signature unknown; restored from __doc__
        """ set_subtitle(self, subtitle:str) """
        pass

    def set_title(self, title): # real signature unknown; restored from __doc__
        """ set_title(self, title:str) """
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

    def suggest_suffix(self, typed_text): # real signature unknown; restored from __doc__
        """ suggest_suffix(self, typed_text:str) -> str or None """
        return ""

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

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f3b25efe820>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Suggestion), '__module__': 'gi.repository.Dazzle', '__gtype__': <GType DzlSuggestion (93962411775744)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'get_icon': gi.FunctionInfo(get_icon), 'get_icon_name': gi.FunctionInfo(get_icon_name), 'get_icon_surface': gi.FunctionInfo(get_icon_surface), 'get_id': gi.FunctionInfo(get_id), 'get_secondary_icon': gi.FunctionInfo(get_secondary_icon), 'get_secondary_icon_name': gi.FunctionInfo(get_secondary_icon_name), 'get_secondary_icon_surface': gi.FunctionInfo(get_secondary_icon_surface), 'get_subtitle': gi.FunctionInfo(get_subtitle), 'get_title': gi.FunctionInfo(get_title), 'replace_typed_text': gi.FunctionInfo(replace_typed_text), 'set_icon_name': gi.FunctionInfo(set_icon_name), 'set_id': gi.FunctionInfo(set_id), 'set_secondary_icon_name': gi.FunctionInfo(set_secondary_icon_name), 'set_subtitle': gi.FunctionInfo(set_subtitle), 'set_title': gi.FunctionInfo(set_title), 'suggest_suffix': gi.FunctionInfo(suggest_suffix), 'do_get_icon': gi.VFuncInfo(get_icon), 'do_get_icon_surface': gi.VFuncInfo(get_icon_surface), 'do_get_secondary_icon': gi.VFuncInfo(get_secondary_icon), 'do_get_secondary_icon_surface': gi.VFuncInfo(get_secondary_icon_surface), 'do_replace_typed_text': gi.VFuncInfo(replace_typed_text), 'do_suggest_suffix': gi.VFuncInfo(suggest_suffix), 'parent_instance': <property object at 0x7f3b25f66360>})"
    __gdoc__ = 'Object DzlSuggestion\n\nSignals from DzlSuggestion:\n  replace-typed-text (gchararray) -> gchararray\n  suggest-suffix (gchararray) -> gchararray\n\nProperties from DzlSuggestion:\n  icon-name -> gchararray: Icon Name\n    The name of the icon to display\n  icon -> GIcon: Icon\n    The GIcon for the suggestion\n  secondary-icon-name -> gchararray: Secondary Icon Name\n    The name of the secondary icon to display\n  secondary-icon -> GIcon: Secondary Icon\n    The secondary GIcon for the suggestion on the right\n  id -> gchararray: Id\n    The suggestion identifier\n  subtitle -> gchararray: Subtitle\n    The subtitle of the suggestion\n  title -> gchararray: Title\n    The title of the suggestion\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType DzlSuggestion (93962411775744)>'
    __info__ = ObjectInfo(Suggestion)


