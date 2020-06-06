# encoding: utf-8
# module gi.repository.Gtk
# from /usr/lib64/girepository-1.0/Gtk-2.0.typelib
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


from .Buildable import Buildable

from .CellLayout import CellLayout

class CellArea(__gi_repository_GObject.InitiallyUnowned, Buildable, CellLayout):
    """
    :Constructors:
    
    ::
    
        CellArea(**properties)
    """
    def activate(self, context, widget, cell_area, flags, edit_only): # real signature unknown; restored from __doc__
        """ activate(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState, edit_only:bool) -> bool """
        return False

    def activate_cell(self, widget, renderer, event, cell_area, flags): # real signature unknown; restored from __doc__
        """ activate_cell(self, widget:Gtk.Widget, renderer:Gtk.CellRenderer, event:Gdk.Event, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) -> bool """
        return False

    def add(self, renderer): # real signature unknown; restored from __doc__
        """ add(self, renderer:Gtk.CellRenderer) """
        pass

    def add_attribute(self, cell, attribute, column): # real signature unknown; restored from __doc__
        """ add_attribute(self, cell:Gtk.CellRenderer, attribute:str, column:int) """
        pass

    def add_child(self, builder, child, type=None): # real signature unknown; restored from __doc__
        """ add_child(self, builder:Gtk.Builder, child:GObject.Object, type:str=None) """
        pass

    def add_focus_sibling(self, renderer, sibling): # real signature unknown; restored from __doc__
        """ add_focus_sibling(self, renderer:Gtk.CellRenderer, sibling:Gtk.CellRenderer) """
        pass

    def apply_attributes(self, tree_model, iter, is_expander, is_expanded): # real signature unknown; restored from __doc__
        """ apply_attributes(self, tree_model:Gtk.TreeModel, iter:Gtk.TreeIter, is_expander:bool, is_expanded:bool) """
        pass

    def attribute_connect(self, renderer, attribute, column): # real signature unknown; restored from __doc__
        """ attribute_connect(self, renderer:Gtk.CellRenderer, attribute:str, column:int) """
        pass

    def attribute_disconnect(self, renderer, attribute): # real signature unknown; restored from __doc__
        """ attribute_disconnect(self, renderer:Gtk.CellRenderer, attribute:str) """
        pass

    def attribute_get_column(self, renderer, attribute): # real signature unknown; restored from __doc__
        """ attribute_get_column(self, renderer:Gtk.CellRenderer, attribute:str) -> int """
        return 0

    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def cell_get_property(self, renderer, property_name, value): # real signature unknown; restored from __doc__
        """ cell_get_property(self, renderer:Gtk.CellRenderer, property_name:str, value:GObject.Value) """
        pass

    def cell_set_property(self, renderer, property_name, value): # real signature unknown; restored from __doc__
        """ cell_set_property(self, renderer:Gtk.CellRenderer, property_name:str, value:GObject.Value) """
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def clear_attributes(self, cell): # real signature unknown; restored from __doc__
        """ clear_attributes(self, cell:Gtk.CellRenderer) """
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

    def construct_child(self, builder, name): # real signature unknown; restored from __doc__
        """ construct_child(self, builder:Gtk.Builder, name:str) -> GObject.Object """
        pass

    def copy_context(self, context): # real signature unknown; restored from __doc__
        """ copy_context(self, context:Gtk.CellAreaContext) -> Gtk.CellAreaContext """
        pass

    def create_context(self): # real signature unknown; restored from __doc__
        """ create_context(self) -> Gtk.CellAreaContext """
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

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_activate(self, *args, **kwargs): # real signature unknown
        """ activate(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState, edit_only:bool) -> bool """
        pass

    def do_add(self, *args, **kwargs): # real signature unknown
        """ add(self, renderer:Gtk.CellRenderer) """
        pass

    def do_apply_attributes(self, *args, **kwargs): # real signature unknown
        """ apply_attributes(self, tree_model:Gtk.TreeModel, iter:Gtk.TreeIter, is_expander:bool, is_expanded:bool) """
        pass

    def do_copy_context(self, *args, **kwargs): # real signature unknown
        """ copy_context(self, context:Gtk.CellAreaContext) -> Gtk.CellAreaContext """
        pass

    def do_create_context(self, *args, **kwargs): # real signature unknown
        """ create_context(self) -> Gtk.CellAreaContext """
        pass

    def do_event(self, *args, **kwargs): # real signature unknown
        """ event(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, event:Gdk.Event, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) -> int """
        pass

    def do_focus(self, *args, **kwargs): # real signature unknown
        """ focus(self, direction:Gtk.DirectionType) -> bool """
        pass

    def do_foreach(self, *args, **kwargs): # real signature unknown
        """ foreach(self, callback:Gtk.CellCallback, callback_data=None) """
        pass

    def do_foreach_alloc(self, *args, **kwargs): # real signature unknown
        """ foreach_alloc(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, cell_area:Gdk.Rectangle, background_area:Gdk.Rectangle, callback:Gtk.CellAllocCallback, callback_data=None) """
        pass

    def do_get_cell_property(self, *args, **kwargs): # real signature unknown
        """ get_cell_property(self, renderer:Gtk.CellRenderer, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def do_get_preferred_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height(self, context:Gtk.CellAreaContext, widget:Gtk.Widget) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_height_for_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_height_for_width(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, width:int) -> minimum_height:int, natural_height:int """
        pass

    def do_get_preferred_width(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width(self, context:Gtk.CellAreaContext, widget:Gtk.Widget) -> minimum_width:int, natural_width:int """
        pass

    def do_get_preferred_width_for_height(self, *args, **kwargs): # real signature unknown
        """ get_preferred_width_for_height(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, height:int) -> minimum_width:int, natural_width:int """
        pass

    def do_get_request_mode(self, *args, **kwargs): # real signature unknown
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
        pass

    def do_is_activatable(self, *args, **kwargs): # real signature unknown
        """ is_activatable(self) -> bool """
        pass

    def do_remove(self, *args, **kwargs): # real signature unknown
        """ remove(self, renderer:Gtk.CellRenderer) """
        pass

    def do_render(self, *args, **kwargs): # real signature unknown
        """ render(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, cr:cairo.Context, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState, paint_focus:bool) """
        pass

    def do_set_cell_property(self, *args, **kwargs): # real signature unknown
        """ set_cell_property(self, renderer:Gtk.CellRenderer, property_id:int, value:GObject.Value, pspec:GObject.ParamSpec) """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def event(self, context, widget, event, cell_area, flags): # real signature unknown; restored from __doc__
        """ event(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, event:Gdk.Event, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState) -> int """
        return 0

    @classmethod
    def find_cell_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_cell_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def find_property(self, property_name): # real signature unknown; restored from __doc__
        """ find_property(self, property_name:str) -> GObject.ParamSpec """
        pass

    def focus(self, direction): # real signature unknown; restored from __doc__
        """ focus(self, direction:Gtk.DirectionType) -> bool """
        return False

    def force_floating(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def foreach(self, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ foreach(self, callback:Gtk.CellCallback, callback_data=None) """
        pass

    def foreach_alloc(self, context, widget, cell_area, background_area, callback, callback_data=None): # real signature unknown; restored from __doc__
        """ foreach_alloc(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, cell_area:Gdk.Rectangle, background_area:Gdk.Rectangle, callback:Gtk.CellAllocCallback, callback_data=None) """
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

    def get_area(self): # real signature unknown; restored from __doc__
        """ get_area(self) -> Gtk.CellArea or None """
        pass

    def get_cells(self): # real signature unknown; restored from __doc__
        """ get_cells(self) -> list """
        return []

    def get_cell_allocation(self, context, widget, renderer, cell_area): # real signature unknown; restored from __doc__
        """ get_cell_allocation(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, renderer:Gtk.CellRenderer, cell_area:Gdk.Rectangle) -> allocation:Gdk.Rectangle """
        pass

    def get_cell_at_position(self, context, widget, cell_area, x, y): # real signature unknown; restored from __doc__
        """ get_cell_at_position(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, cell_area:Gdk.Rectangle, x:int, y:int) -> Gtk.CellRenderer, alloc_area:Gdk.Rectangle """
        pass

    def get_current_path_string(self): # real signature unknown; restored from __doc__
        """ get_current_path_string(self) -> str """
        return ""

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_edited_cell(self): # real signature unknown; restored from __doc__
        """ get_edited_cell(self) -> Gtk.CellRenderer """
        pass

    def get_edit_widget(self): # real signature unknown; restored from __doc__
        """ get_edit_widget(self) -> Gtk.CellEditable """
        pass

    def get_focus_cell(self): # real signature unknown; restored from __doc__
        """ get_focus_cell(self) -> Gtk.CellRenderer """
        pass

    def get_focus_from_sibling(self, renderer): # real signature unknown; restored from __doc__
        """ get_focus_from_sibling(self, renderer:Gtk.CellRenderer) -> Gtk.CellRenderer or None """
        pass

    def get_focus_siblings(self, renderer): # real signature unknown; restored from __doc__
        """ get_focus_siblings(self, renderer:Gtk.CellRenderer) -> list """
        return []

    def get_internal_child(self, builder, childname): # real signature unknown; restored from __doc__
        """ get_internal_child(self, builder:Gtk.Builder, childname:str) -> GObject.Object """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_preferred_height(self, context, widget): # real signature unknown; restored from __doc__
        """ get_preferred_height(self, context:Gtk.CellAreaContext, widget:Gtk.Widget) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_height_for_width(self, context, widget, width): # real signature unknown; restored from __doc__
        """ get_preferred_height_for_width(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, width:int) -> minimum_height:int, natural_height:int """
        pass

    def get_preferred_width(self, context, widget): # real signature unknown; restored from __doc__
        """ get_preferred_width(self, context:Gtk.CellAreaContext, widget:Gtk.Widget) -> minimum_width:int, natural_width:int """
        pass

    def get_preferred_width_for_height(self, context, widget, height): # real signature unknown; restored from __doc__
        """ get_preferred_width_for_height(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, height:int) -> minimum_width:int, natural_width:int """
        pass

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_request_mode(self): # real signature unknown; restored from __doc__
        """ get_request_mode(self) -> Gtk.SizeRequestMode """
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

    def has_renderer(self, renderer): # real signature unknown; restored from __doc__
        """ has_renderer(self, renderer:Gtk.CellRenderer) -> bool """
        return False

    def inner_cell_area(self, widget, cell_area): # real signature unknown; restored from __doc__
        """ inner_cell_area(self, widget:Gtk.Widget, cell_area:Gdk.Rectangle) -> inner_area:Gdk.Rectangle """
        pass

    @classmethod
    def install_cell_property(self, property_id, pspec): # real signature unknown; restored from __doc__
        """ install_cell_property(self, property_id:int, pspec:GObject.ParamSpec) """
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

    def is_activatable(self): # real signature unknown; restored from __doc__
        """ is_activatable(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_focus_sibling(self, renderer, sibling): # real signature unknown; restored from __doc__
        """ is_focus_sibling(self, renderer:Gtk.CellRenderer, sibling:Gtk.CellRenderer) -> bool """
        return False

    @classmethod
    def list_cell_properties(self): # real signature unknown; restored from __doc__
        """ list_cell_properties(self) -> list, n_properties:int """
        return []

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
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

    def pack_end(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_end(self, cell:Gtk.CellRenderer, expand:bool) """
        pass

    def pack_start(self, cell, expand): # real signature unknown; restored from __doc__
        """ pack_start(self, cell:Gtk.CellRenderer, expand:bool) """
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

    def remove(self, renderer): # real signature unknown; restored from __doc__
        """ remove(self, renderer:Gtk.CellRenderer) """
        pass

    def remove_focus_sibling(self, renderer, sibling): # real signature unknown; restored from __doc__
        """ remove_focus_sibling(self, renderer:Gtk.CellRenderer, sibling:Gtk.CellRenderer) """
        pass

    def render(self, context, widget, cr, background_area, cell_area, flags, paint_focus): # real signature unknown; restored from __doc__
        """ render(self, context:Gtk.CellAreaContext, widget:Gtk.Widget, cr:cairo.Context, background_area:Gdk.Rectangle, cell_area:Gdk.Rectangle, flags:Gtk.CellRendererState, paint_focus:bool) """
        pass

    def reorder(self, cell, position): # real signature unknown; restored from __doc__
        """ reorder(self, cell:Gtk.CellRenderer, position:int) """
        pass

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def request_renderer(self, renderer, orientation, widget, for_size): # real signature unknown; restored from __doc__
        """ request_renderer(self, renderer:Gtk.CellRenderer, orientation:Gtk.Orientation, widget:Gtk.Widget, for_size:int) -> minimum_size:int, natural_size:int """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_buildable_property(self, builder, name, value): # real signature unknown; restored from __doc__
        """ set_buildable_property(self, builder:Gtk.Builder, name:str, value:GObject.Value) """
        pass

    def set_cell_data_func(self, cell, func=None, func_data=None): # real signature unknown; restored from __doc__
        """ set_cell_data_func(self, cell:Gtk.CellRenderer, func:Gtk.CellLayoutDataFunc=None, func_data=None) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_focus_cell(self, renderer): # real signature unknown; restored from __doc__
        """ set_focus_cell(self, renderer:Gtk.CellRenderer) """
        pass

    def set_name(self, name): # real signature unknown; restored from __doc__
        """ set_name(self, name:str) """
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

    def stop_editing(self, canceled): # real signature unknown; restored from __doc__
        """ stop_editing(self, canceled:bool) """
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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fc639ecb760>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(CellArea), '__module__': 'gi.repository.Gtk', '__gtype__': <GType GtkCellArea (93897368115040)>, '__doc__': None, '__gsignals__': {}, 'find_cell_property': <classmethod object at 0x7fc63a7c4b80>, 'install_cell_property': <classmethod object at 0x7fc63a7c4ac0>, 'list_cell_properties': <classmethod object at 0x7fc63a7c4b50>, 'activate': gi.FunctionInfo(activate), 'activate_cell': gi.FunctionInfo(activate_cell), 'add': gi.FunctionInfo(add), 'add_focus_sibling': gi.FunctionInfo(add_focus_sibling), 'apply_attributes': gi.FunctionInfo(apply_attributes), 'attribute_connect': gi.FunctionInfo(attribute_connect), 'attribute_disconnect': gi.FunctionInfo(attribute_disconnect), 'attribute_get_column': gi.FunctionInfo(attribute_get_column), 'cell_get_property': gi.FunctionInfo(cell_get_property), 'cell_set_property': gi.FunctionInfo(cell_set_property), 'copy_context': gi.FunctionInfo(copy_context), 'create_context': gi.FunctionInfo(create_context), 'event': gi.FunctionInfo(event), 'focus': gi.FunctionInfo(focus), 'foreach': gi.FunctionInfo(foreach), 'foreach_alloc': gi.FunctionInfo(foreach_alloc), 'get_cell_allocation': gi.FunctionInfo(get_cell_allocation), 'get_cell_at_position': gi.FunctionInfo(get_cell_at_position), 'get_current_path_string': gi.FunctionInfo(get_current_path_string), 'get_edit_widget': gi.FunctionInfo(get_edit_widget), 'get_edited_cell': gi.FunctionInfo(get_edited_cell), 'get_focus_cell': gi.FunctionInfo(get_focus_cell), 'get_focus_from_sibling': gi.FunctionInfo(get_focus_from_sibling), 'get_focus_siblings': gi.FunctionInfo(get_focus_siblings), 'get_preferred_height': gi.FunctionInfo(get_preferred_height), 'get_preferred_height_for_width': gi.FunctionInfo(get_preferred_height_for_width), 'get_preferred_width': gi.FunctionInfo(get_preferred_width), 'get_preferred_width_for_height': gi.FunctionInfo(get_preferred_width_for_height), 'get_request_mode': gi.FunctionInfo(get_request_mode), 'has_renderer': gi.FunctionInfo(has_renderer), 'inner_cell_area': gi.FunctionInfo(inner_cell_area), 'is_activatable': gi.FunctionInfo(is_activatable), 'is_focus_sibling': gi.FunctionInfo(is_focus_sibling), 'remove': gi.FunctionInfo(remove), 'remove_focus_sibling': gi.FunctionInfo(remove_focus_sibling), 'render': gi.FunctionInfo(render), 'request_renderer': gi.FunctionInfo(request_renderer), 'set_focus_cell': gi.FunctionInfo(set_focus_cell), 'stop_editing': gi.FunctionInfo(stop_editing), 'do_activate': gi.VFuncInfo(activate), 'do_add': gi.VFuncInfo(add), 'do_apply_attributes': gi.VFuncInfo(apply_attributes), 'do_copy_context': gi.VFuncInfo(copy_context), 'do_create_context': gi.VFuncInfo(create_context), 'do_event': gi.VFuncInfo(event), 'do_focus': gi.VFuncInfo(focus), 'do_foreach': gi.VFuncInfo(foreach), 'do_foreach_alloc': gi.VFuncInfo(foreach_alloc), 'do_get_cell_property': gi.VFuncInfo(get_cell_property), 'do_get_preferred_height': gi.VFuncInfo(get_preferred_height), 'do_get_preferred_height_for_width': gi.VFuncInfo(get_preferred_height_for_width), 'do_get_preferred_width': gi.VFuncInfo(get_preferred_width), 'do_get_preferred_width_for_height': gi.VFuncInfo(get_preferred_width_for_height), 'do_get_request_mode': gi.VFuncInfo(get_request_mode), 'do_is_activatable': gi.VFuncInfo(is_activatable), 'do_remove': gi.VFuncInfo(remove), 'do_render': gi.VFuncInfo(render), 'do_set_cell_property': gi.VFuncInfo(set_cell_property), 'parent_instance': <property object at 0x7fc63a7cb8b0>, 'priv': <property object at 0x7fc63a7cb9f0>})"
    __gdoc__ = 'Object GtkCellArea\n\nSignals from GtkCellArea:\n  apply-attributes (GtkTreeModel, GtkTreeIter, gboolean, gboolean)\n  add-editable (GtkCellRenderer, GtkCellEditable, GdkRectangle, gchararray)\n  remove-editable (GtkCellRenderer, GtkCellEditable)\n  focus-changed (GtkCellRenderer, gchararray)\n\nProperties from GtkCellArea:\n  focus-cell -> GtkCellRenderer: Focus Cell\n    The cell which currently has focus\n  edited-cell -> GtkCellRenderer: Edited Cell\n    The cell which is currently being edited\n  edit-widget -> GtkCellEditable: Edit Widget\n    The widget currently editing the edited cell\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GtkCellArea (93897368115040)>'
    __info__ = ObjectInfo(CellArea)


