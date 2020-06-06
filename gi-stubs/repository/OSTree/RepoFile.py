# encoding: utf-8
# module gi.repository.OSTree
# from /usr/lib64/girepository-1.0/OSTree-1.0.typelib
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


class RepoFile(__gi_overrides_GObject.Object, __gi_repository_Gio.File):
    """
    :Constructors:
    
    ::
    
        RepoFile(**properties)
    """
    def append_to(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ append_to(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def append_to_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ append_to_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def append_to_finish(self, res): # real signature unknown; restored from __doc__
        """ append_to_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

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

    def copy(self, destination, flags, cancellable=None, progress_callback=None, progress_callback_data=None): # real signature unknown; restored from __doc__
        """ copy(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None) -> bool """
        return False

    def copy_async(self, destination, flags, io_priority, cancellable=None, progress_callback=None, progress_callback_data=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ copy_async(self, destination:Gio.File, flags:Gio.FileCopyFlags, io_priority:int, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def copy_attributes(self, destination, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ copy_attributes(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def copy_finish(self, res): # real signature unknown; restored from __doc__
        """ copy_finish(self, res:Gio.AsyncResult) -> bool """
        return False

    def create(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ create(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def create_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_finish(self, res): # real signature unknown; restored from __doc__
        """ create_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def create_readwrite(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ create_readwrite(self, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def create_readwrite_async(self, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ create_readwrite_async(self, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def create_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ create_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def delete(self, cancellable=None): # real signature unknown; restored from __doc__
        """ delete(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def delete_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ delete_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def delete_finish(self, result): # real signature unknown; restored from __doc__
        """ delete_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def disconnect(*args, **kwargs): # reliably restored by inspect
        """ signal_handler_disconnect(instance:GObject.Object, handler_id:int) """
        pass

    def disconnect_by_func(self, *args, **kwargs): # real signature unknown
        pass

    def dup(self): # real signature unknown; restored from __doc__
        """ dup(self) -> Gio.File """
        pass

    def eject_mountable(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject_mountable(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def eject_mountable_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ eject_mountable_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def eject_mountable_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ eject_mountable_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def emit(self, *args, **kwargs): # real signature unknown
        pass

    def emit_stop_by_name(self, detailed_signal): # reliably restored by inspect
        """ Deprecated, please use stop_emission_by_name. """
        pass

    def ensure_resolved(self): # real signature unknown; restored from __doc__
        """ ensure_resolved(self) -> bool """
        return False

    def enumerate_children(self, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ enumerate_children(self, attributes:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileEnumerator """
        pass

    def enumerate_children_async(self, attributes, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ enumerate_children_async(self, attributes:str, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def enumerate_children_finish(self, res): # real signature unknown; restored from __doc__
        """ enumerate_children_finish(self, res:Gio.AsyncResult) -> Gio.FileEnumerator """
        pass

    def equal(self, file2): # real signature unknown; restored from __doc__
        """ equal(self, file2:Gio.File) -> bool """
        return False

    def find_enclosing_mount(self, cancellable=None): # real signature unknown; restored from __doc__
        """ find_enclosing_mount(self, cancellable:Gio.Cancellable=None) -> Gio.Mount """
        pass

    def find_enclosing_mount_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ find_enclosing_mount_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def find_enclosing_mount_finish(self, res): # real signature unknown; restored from __doc__
        """ find_enclosing_mount_finish(self, res:Gio.AsyncResult) -> Gio.Mount """
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

    def get_basename(self): # real signature unknown; restored from __doc__
        """ get_basename(self) -> str or None """
        return ""

    def get_checksum(self): # real signature unknown; restored from __doc__
        """ get_checksum(self) -> str """
        return ""

    def get_child(self, name): # real signature unknown; restored from __doc__
        """ get_child(self, name:str) -> Gio.File """
        pass

    def get_child_for_display_name(self, display_name): # real signature unknown; restored from __doc__
        """ get_child_for_display_name(self, display_name:str) -> Gio.File """
        pass

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_parent(self): # real signature unknown; restored from __doc__
        """ get_parent(self) -> Gio.File or None """
        pass

    def get_parse_name(self): # real signature unknown; restored from __doc__
        """ get_parse_name(self) -> str """
        return ""

    def get_path(self): # real signature unknown; restored from __doc__
        """ get_path(self) -> str or None """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_relative_path(self, descendant): # real signature unknown; restored from __doc__
        """ get_relative_path(self, descendant:Gio.File) -> str or None """
        return ""

    def get_repo(self): # real signature unknown; restored from __doc__
        """ get_repo(self) -> OSTree.Repo """
        pass

    def get_root(self): # real signature unknown; restored from __doc__
        """ get_root(self) -> OSTree.RepoFile """
        pass

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_uri_scheme(self): # real signature unknown; restored from __doc__
        """ get_uri_scheme(self) -> str """
        return ""

    def get_xattrs(self, cancellable=None): # real signature unknown; restored from __doc__
        """ get_xattrs(self, cancellable:Gio.Cancellable=None) -> bool, out_xattrs:GLib.Variant """
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

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def has_parent(self, parent=None): # real signature unknown; restored from __doc__
        """ has_parent(self, parent:Gio.File=None) -> bool """
        return False

    def has_prefix(self, prefix): # real signature unknown; restored from __doc__
        """ has_prefix(self, prefix:Gio.File) -> bool """
        return False

    def has_uri_scheme(self, uri_scheme): # real signature unknown; restored from __doc__
        """ has_uri_scheme(self, uri_scheme:str) -> bool """
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

    def is_floating(self): # real signature unknown; restored from __doc__
        """ is_floating(self) -> bool """
        return False

    def is_native(self): # real signature unknown; restored from __doc__
        """ is_native(self) -> bool """
        return False

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def load_bytes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_bytes(self, cancellable:Gio.Cancellable=None) -> GLib.Bytes, etag_out:str """
        pass

    def load_bytes_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_bytes_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_bytes_finish(self, result): # real signature unknown; restored from __doc__
        """ load_bytes_finish(self, result:Gio.AsyncResult) -> GLib.Bytes, etag_out:str """
        pass

    def load_contents(self, cancellable=None): # real signature unknown; restored from __doc__
        """ load_contents(self, cancellable:Gio.Cancellable=None) -> bool, contents:list, etag_out:str """
        return False

    def load_contents_async(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ load_contents_async(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def load_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ load_contents_finish(self, res:Gio.AsyncResult) -> bool, contents:list, etag_out:str """
        return False

    def load_partial_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ load_partial_contents_finish(self, res:Gio.AsyncResult) -> bool, contents:list, etag_out:str """
        return False

    def make_directory(self, cancellable=None): # real signature unknown; restored from __doc__
        """ make_directory(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def make_directory_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ make_directory_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def make_directory_finish(self, result): # real signature unknown; restored from __doc__
        """ make_directory_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def make_directory_with_parents(self, cancellable=None): # real signature unknown; restored from __doc__
        """ make_directory_with_parents(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def make_symbolic_link(self, symlink_value, cancellable=None): # real signature unknown; restored from __doc__
        """ make_symbolic_link(self, symlink_value:str, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def measure_disk_usage_finish(self, result): # real signature unknown; restored from __doc__
        """ measure_disk_usage_finish(self, result:Gio.AsyncResult) -> bool, disk_usage:int, num_dirs:int, num_files:int """
        return False

    def monitor(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def monitor_directory(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor_directory(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def monitor_file(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ monitor_file(self, flags:Gio.FileMonitorFlags, cancellable:Gio.Cancellable=None) -> Gio.FileMonitor """
        pass

    def mount_enclosing_volume(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mount_enclosing_volume(self, flags:Gio.MountMountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mount_enclosing_volume_finish(self, result): # real signature unknown; restored from __doc__
        """ mount_enclosing_volume_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def mount_mountable(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ mount_mountable(self, flags:Gio.MountMountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def mount_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ mount_mountable_finish(self, result:Gio.AsyncResult) -> Gio.File """
        pass

    def move(self, destination, flags, cancellable=None, progress_callback=None, progress_callback_data=None): # real signature unknown; restored from __doc__
        """ move(self, destination:Gio.File, flags:Gio.FileCopyFlags, cancellable:Gio.Cancellable=None, progress_callback:Gio.FileProgressCallback=None, progress_callback_data=None) -> bool """
        return False

    def newv(self, object_type, parameters): # real signature unknown; restored from __doc__
        """ newv(object_type:GType, parameters:list) -> GObject.Object """
        pass

    def new_for_commandline_arg(self, arg): # real signature unknown; restored from __doc__
        """ new_for_commandline_arg(arg:str) -> Gio.File """
        pass

    def new_for_commandline_arg_and_cwd(self, arg, cwd): # real signature unknown; restored from __doc__
        """ new_for_commandline_arg_and_cwd(arg:str, cwd:str) -> Gio.File """
        pass

    def new_for_path(self, path): # real signature unknown; restored from __doc__
        """ new_for_path(path:str) -> Gio.File """
        pass

    def new_for_uri(self, uri): # real signature unknown; restored from __doc__
        """ new_for_uri(uri:str) -> Gio.File """
        pass

    def new_tmp(self, tmpl=None): # real signature unknown; restored from __doc__
        """ new_tmp(tmpl:str=None) -> Gio.File, iostream:Gio.FileIOStream """
        pass

    def notify(self, property_name): # real signature unknown; restored from __doc__
        """ notify(self, property_name:str) """
        pass

    def notify_by_pspec(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def open_readwrite(self, cancellable=None): # real signature unknown; restored from __doc__
        """ open_readwrite(self, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def open_readwrite_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ open_readwrite_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def open_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ open_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def override_property(self, property_id, name): # real signature unknown; restored from __doc__
        """ override_property(self, property_id:int, name:str) """
        pass

    def parse_name(self, parse_name): # real signature unknown; restored from __doc__
        """ parse_name(parse_name:str) -> Gio.File """
        pass

    def peek_path(self): # real signature unknown; restored from __doc__
        """ peek_path(self) -> str or None """
        return ""

    def poll_mountable(self, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ poll_mountable(self, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def poll_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ poll_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def query_default_handler(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_default_handler(self, cancellable:Gio.Cancellable=None) -> Gio.AppInfo """
        pass

    def query_default_handler_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_default_handler_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_default_handler_finish(self, result): # real signature unknown; restored from __doc__
        """ query_default_handler_finish(self, result:Gio.AsyncResult) -> Gio.AppInfo """
        pass

    def query_exists(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_exists(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def query_filesystem_info(self, attributes, cancellable=None): # real signature unknown; restored from __doc__
        """ query_filesystem_info(self, attributes:str, cancellable:Gio.Cancellable=None) -> Gio.FileInfo """
        pass

    def query_filesystem_info_async(self, attributes, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_filesystem_info_async(self, attributes:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_filesystem_info_finish(self, res): # real signature unknown; restored from __doc__
        """ query_filesystem_info_finish(self, res:Gio.AsyncResult) -> Gio.FileInfo """
        pass

    def query_file_type(self, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ query_file_type(self, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileType """
        pass

    def query_info(self, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ query_info(self, attributes:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> Gio.FileInfo """
        pass

    def query_info_async(self, attributes, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ query_info_async(self, attributes:str, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def query_info_finish(self, res): # real signature unknown; restored from __doc__
        """ query_info_finish(self, res:Gio.AsyncResult) -> Gio.FileInfo """
        pass

    def query_settable_attributes(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_settable_attributes(self, cancellable:Gio.Cancellable=None) -> Gio.FileAttributeInfoList """
        pass

    def query_writable_namespaces(self, cancellable=None): # real signature unknown; restored from __doc__
        """ query_writable_namespaces(self, cancellable:Gio.Cancellable=None) -> Gio.FileAttributeInfoList """
        pass

    def read(self, cancellable=None): # real signature unknown; restored from __doc__
        """ read(self, cancellable:Gio.Cancellable=None) -> Gio.FileInputStream """
        pass

    def read_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ read_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def read_finish(self, res): # real signature unknown; restored from __doc__
        """ read_finish(self, res:Gio.AsyncResult) -> Gio.FileInputStream """
        pass

    def ref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def ref_sink(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace(self, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileOutputStream """
        pass

    def replace_async(self, etag=None, make_backup, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_async(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents(self, contents, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace_contents(self, contents:list, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> bool, new_etag:str """
        return False

    def replace_contents_async(self, contents, etag=None, make_backup, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_contents_async(self, contents:list, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents_bytes_async(self, contents, etag=None, make_backup, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_contents_bytes_async(self, contents:GLib.Bytes, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_contents_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_contents_finish(self, res:Gio.AsyncResult) -> bool, new_etag:str """
        return False

    def replace_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_finish(self, res:Gio.AsyncResult) -> Gio.FileOutputStream """
        pass

    def replace_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def replace_readwrite(self, etag=None, make_backup, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ replace_readwrite(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, cancellable:Gio.Cancellable=None) -> Gio.FileIOStream """
        pass

    def replace_readwrite_async(self, etag=None, make_backup, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ replace_readwrite_async(self, etag:str=None, make_backup:bool, flags:Gio.FileCreateFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def replace_readwrite_finish(self, res): # real signature unknown; restored from __doc__
        """ replace_readwrite_finish(self, res:Gio.AsyncResult) -> Gio.FileIOStream """
        pass

    def resolve_relative_path(self, relative_path): # real signature unknown; restored from __doc__
        """ resolve_relative_path(self, relative_path:str) -> Gio.File """
        pass

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_attribute(self, attribute, type, value_p=None, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute(self, attribute:str, type:Gio.FileAttributeType, value_p=None, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attributes_async(self, info, flags, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_attributes_async(self, info:Gio.FileInfo, flags:Gio.FileQueryInfoFlags, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_attributes_finish(self, result): # real signature unknown; restored from __doc__
        """ set_attributes_finish(self, result:Gio.AsyncResult) -> bool, info:Gio.FileInfo """
        return False

    def set_attributes_from_info(self, info, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attributes_from_info(self, info:Gio.FileInfo, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_byte_string(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_byte_string(self, attribute:str, value:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_int32(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_int32(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_int64(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_int64(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_string(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_string(self, attribute:str, value:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_uint32(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_uint32(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_attribute_uint64(self, attribute, value, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ set_attribute_uint64(self, attribute:str, value:int, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_display_name(self, display_name, cancellable=None): # real signature unknown; restored from __doc__
        """ set_display_name(self, display_name:str, cancellable:Gio.Cancellable=None) -> Gio.File """
        pass

    def set_display_name_async(self, display_name, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_display_name_async(self, display_name:str, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def set_display_name_finish(self, res): # real signature unknown; restored from __doc__
        """ set_display_name_finish(self, res:Gio.AsyncResult) -> Gio.File """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def start_mountable(self, flags, start_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ start_mountable(self, flags:Gio.DriveStartFlags, start_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def start_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ start_mountable_finish(self, result:Gio.AsyncResult) -> bool """
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

    def stop_mountable(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ stop_mountable(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def stop_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ stop_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def supports_thread_contexts(self): # real signature unknown; restored from __doc__
        """ supports_thread_contexts(self) -> bool """
        return False

    def thaw_notify(self): # real signature unknown; restored from __doc__
        """ thaw_notify(self) """
        pass

    def trash(self, cancellable=None): # real signature unknown; restored from __doc__
        """ trash(self, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def trash_async(self, io_priority, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ trash_async(self, io_priority:int, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def trash_finish(self, result): # real signature unknown; restored from __doc__
        """ trash_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def tree_find_child(self, name): # real signature unknown; restored from __doc__
        """ tree_find_child(self, name:str) -> int, is_dir:bool, out_container:GLib.Variant """
        return 0

    def tree_get_contents(self): # real signature unknown; restored from __doc__
        """ tree_get_contents(self) -> GLib.Variant """
        pass

    def tree_get_contents_checksum(self): # real signature unknown; restored from __doc__
        """ tree_get_contents_checksum(self) -> str """
        return ""

    def tree_get_metadata(self): # real signature unknown; restored from __doc__
        """ tree_get_metadata(self) -> GLib.Variant """
        pass

    def tree_get_metadata_checksum(self): # real signature unknown; restored from __doc__
        """ tree_get_metadata_checksum(self) -> str """
        return ""

    def tree_query_child(self, n, attributes, flags, cancellable=None): # real signature unknown; restored from __doc__
        """ tree_query_child(self, n:int, attributes:str, flags:Gio.FileQueryInfoFlags, cancellable:Gio.Cancellable=None) -> bool, out_info:Gio.FileInfo """
        return False

    def tree_set_metadata(self, checksum, metadata): # real signature unknown; restored from __doc__
        """ tree_set_metadata(self, checksum:str, metadata:GLib.Variant) """
        pass

    def unmount_mountable(self, flags, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount_mountable(self, flags:Gio.MountUnmountFlags, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_mountable_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_mountable_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def unmount_mountable_with_operation(self, flags, mount_operation=None, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ unmount_mountable_with_operation(self, flags:Gio.MountUnmountFlags, mount_operation:Gio.MountOperation=None, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def unmount_mountable_with_operation_finish(self, result): # real signature unknown; restored from __doc__
        """ unmount_mountable_with_operation_finish(self, result:Gio.AsyncResult) -> bool """
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

    g_type_instance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7feceb5bfdc0>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(RepoFile), '__module__': 'gi.repository.OSTree', '__gtype__': <GType OstreeRepoFile (94405993335040)>, '__doc__': None, '__gsignals__': {}, 'ensure_resolved': gi.FunctionInfo(ensure_resolved), 'get_checksum': gi.FunctionInfo(get_checksum), 'get_repo': gi.FunctionInfo(get_repo), 'get_root': gi.FunctionInfo(get_root), 'get_xattrs': gi.FunctionInfo(get_xattrs), 'tree_find_child': gi.FunctionInfo(tree_find_child), 'tree_get_contents': gi.FunctionInfo(tree_get_contents), 'tree_get_contents_checksum': gi.FunctionInfo(tree_get_contents_checksum), 'tree_get_metadata': gi.FunctionInfo(tree_get_metadata), 'tree_get_metadata_checksum': gi.FunctionInfo(tree_get_metadata_checksum), 'tree_query_child': gi.FunctionInfo(tree_query_child), 'tree_set_metadata': gi.FunctionInfo(tree_set_metadata)})"
    __gdoc__ = 'Object OstreeRepoFile\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType OstreeRepoFile (94405993335040)>'
    __info__ = ObjectInfo(RepoFile)


