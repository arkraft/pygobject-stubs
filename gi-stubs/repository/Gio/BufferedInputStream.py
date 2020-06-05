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


from .FilterInputStream import FilterInputStream

from .Seekable import Seekable

class BufferedInputStream(FilterInputStream, Seekable):
    """
    :Constructors:
    
    ::
    
        BufferedInputStream(**properties)
        new(base_stream:Gio.InputStream) -> Gio.InputStream
        new_sized(base_stream:Gio.InputStream, size:int) -> Gio.InputStream
    """
    def bind_property(self, *args, **kwargs): # real signature unknown
        pass

    def bind_property_full(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def can_seek(self): # real signature unknown; restored from __doc__
        """ can_seek(self) -> bool """
        return False

    def can_truncate(self): # real signature unknown; restored from __doc__
        """ can_truncate(self) -> bool """
        return False

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def clear_pending(self): # real signature unknown; restored from __doc__
        """ clear_pending(self) """
        pass

    def close(self, cancellable=None): # real signature unknown; restored from __doc__
        """ close(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def close_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ close_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def close_finish(self, result): # real signature unknown; restored from __doc__
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
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

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def do_close_async(self, *args, **kwargs): # real signature unknown
        """ close_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_close_finish(self, *args, **kwargs): # real signature unknown
        """ close_finish(self, result:Gio.AsyncResult) -> bool """
        pass

    def do_close_fn(self, *args, **kwargs): # real signature unknown
        """ close_fn(self, cancellable:Gio.Cancellable=None) -> bool """
        pass

    def do_fill(self, *args, **kwargs): # real signature unknown
        """ fill(self, count:int, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_fill_async(self, *args, **kwargs): # real signature unknown
        """ fill_async(self, count:int, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_fill_finish(self, *args, **kwargs): # real signature unknown
        """ fill_finish(self, result:Gio.AsyncResult) -> int """
        pass

    def do_read_async(self, *args, **kwargs): # real signature unknown
        """ read_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) -> buffer:list """
        pass

    def do_read_finish(self, *args, **kwargs): # real signature unknown
        """ read_finish(self, result:Gio.AsyncResult) -> int """
        pass

    def do_read_fn(self, *args, **kwargs): # real signature unknown
        """ read_fn(self, buffer=None, count:int, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_skip(self, *args, **kwargs): # real signature unknown
        """ skip(self, count:int, cancellable:Gio.Cancellable=None) -> int """
        pass

    def do_skip_async(self, *args, **kwargs): # real signature unknown
        """ skip_async(self, count:int, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def do_skip_finish(self, *args, **kwargs): # real signature unknown
        """ skip_finish(self, result:Gio.AsyncResult) -> int """
        pass

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def fill(self, count, cancellable=None): # real signature unknown; restored from __doc__
        """ fill(self, count:int, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def fill_async(self, count, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ fill_async(self, count:int, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def fill_finish(self, result): # real signature unknown; restored from __doc__
        """ fill_finish(self, result:Gio.AsyncResult) -> int """
        return 0

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

    def get_available(self): # real signature unknown; restored from __doc__
        """ get_available(self) -> int """
        return 0

    def get_base_stream(self): # real signature unknown; restored from __doc__
        """ get_base_stream(self) -> Gio.InputStream """
        pass

    def get_buffer_size(self): # real signature unknown; restored from __doc__
        """ get_buffer_size(self) -> int """
        return 0

    def get_close_base_stream(self): # real signature unknown; restored from __doc__
        """ get_close_base_stream(self) -> bool """
        return False

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

    def has_pending(self): # real signature unknown; restored from __doc__
        """ has_pending(self) -> bool """
        return False

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

    def is_closed(self): # real signature unknown; restored from __doc__
        """ is_closed(self) -> bool """
        return False

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self, base_stream): # real signature unknown; restored from __doc__
        """ new(base_stream:Gio.InputStream) -> Gio.InputStream """
        pass

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_sized(self, base_stream, size): # real signature unknown; restored from __doc__
        """ new_sized(base_stream:Gio.InputStream, size:int) -> Gio.InputStream """
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

    def peek(self, buffer, offset): # real signature unknown; restored from __doc__
        """ peek(self, buffer:list, offset:int) -> int """
        return 0

    def peek_buffer(self): # real signature unknown; restored from __doc__
        """ peek_buffer(self) -> list, count:int """
        return []

    def read(self, cancellable=None): # real signature unknown; restored from __doc__
        """ read(self, cancellable:Gio.Cancellable=None) -> int, buffer:list """
        return 0

    def read_all(self, cancellable=None): # real signature unknown; restored from __doc__
        """ read_all(self, cancellable:Gio.Cancellable=None) -> bool, buffer:list, bytes_read:int """
        return False

    def read_all_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ read_all_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) -> buffer:list """
        pass

    def read_all_finish(self, result): # real signature unknown; restored from __doc__
        """ read_all_finish(self, result:Gio.AsyncResult) -> bool, bytes_read:int """
        return False

    def read_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ read_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) -> buffer:list """
        pass

    def read_byte(self, cancellable=None): # real signature unknown; restored from __doc__
        """ read_byte(self, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def read_bytes(self, count, cancellable=None): # real signature unknown; restored from __doc__
        """ read_bytes(self, count:int, cancellable:Gio.Cancellable=None) -> GLib.Bytes """
        pass

    def read_bytes_async(self, count, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ read_bytes_async(self, count:int, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def read_bytes_finish(self, result): # real signature unknown; restored from __doc__
        """ read_bytes_finish(self, result:Gio.AsyncResult) -> GLib.Bytes """
        pass

    def read_finish(self, result): # real signature unknown; restored from __doc__
        """ read_finish(self, result:Gio.AsyncResult) -> int """
        return 0

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

    def seek(self, offset, type, cancellable=None): # real signature unknown; restored from __doc__
        """ seek(self, offset:int, type:GLib.SeekType, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_buffer_size(self, size): # real signature unknown; restored from __doc__
        """ set_buffer_size(self, size:int) """
        pass

    def set_close_base_stream(self, close_base): # real signature unknown; restored from __doc__
        """ set_close_base_stream(self, close_base:bool) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_pending(self): # real signature unknown; restored from __doc__
        """ set_pending(self) -> bool """
        return False

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def skip(self, count, cancellable=None): # real signature unknown; restored from __doc__
        """ skip(self, count:int, cancellable:Gio.Cancellable=None) -> int """
        return 0

    def skip_async(self, count, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ skip_async(self, count:int, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def skip_finish(self, result): # real signature unknown; restored from __doc__
        """ skip_finish(self, result:Gio.AsyncResult) -> int """
        return 0

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

    def tell(self): # real signature unknown; restored from __doc__
        """ tell(self) -> int """
        return 0

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def truncate(self, offset, cancellable=None): # real signature unknown; restored from __doc__
        """ truncate(self, offset:int, cancellable:Gio.Cancellable=None) -> bool """
        return False

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

    base_stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    parent_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f28dd616a30>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(BufferedInputStream), '__module__': 'gi.repository.Gio', '__gtype__': <GType GBufferedInputStream (94125581793520)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'new_sized': gi.FunctionInfo(new_sized), 'fill': gi.FunctionInfo(fill), 'fill_async': gi.FunctionInfo(fill_async), 'fill_finish': gi.FunctionInfo(fill_finish), 'get_available': gi.FunctionInfo(get_available), 'get_buffer_size': gi.FunctionInfo(get_buffer_size), 'peek': gi.FunctionInfo(peek), 'peek_buffer': gi.FunctionInfo(peek_buffer), 'read_byte': gi.FunctionInfo(read_byte), 'set_buffer_size': gi.FunctionInfo(set_buffer_size), 'do_fill': gi.VFuncInfo(fill), 'do_fill_async': gi.VFuncInfo(fill_async), 'do_fill_finish': gi.VFuncInfo(fill_finish), 'parent_instance': <property object at 0x7f28ddf2d720>, 'priv': <property object at 0x7f28ddf2d810>})"
    __gdoc__ = 'Object GBufferedInputStream\n\nProperties from GBufferedInputStream:\n  buffer-size -> guint: Buffer Size\n    The size of the backend buffer\n\nProperties from GFilterInputStream:\n  base-stream -> GInputStream: The Filter Base Stream\n    The underlying base stream on which the io ops will be done.\n  close-base-stream -> gboolean: Close Base Stream\n    If the base stream should be closed when the filter stream is closed.\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GBufferedInputStream (94125581793520)>'
    __info__ = ObjectInfo(BufferedInputStream)


