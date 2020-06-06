# encoding: utf-8
# module gi.repository.AppStream
# from /usr/lib64/girepository-1.0/AppStream-1.0.typelib
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


class Release(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        Release(**properties)
        new() -> AppStream.Release
    """
    def add_artifact(self, artifact): # real signature unknown; restored from __doc__
        """ add_artifact(self, artifact:AppStream.Artifact) """
        pass

    def add_checksum(self, cs): # real signature unknown; restored from __doc__
        """ add_checksum(self, cs:AppStream.Checksum) """
        pass

    def add_issue(self, issue): # real signature unknown; restored from __doc__
        """ add_issue(self, issue:AppStream.Issue) """
        pass

    def add_location(self, location): # real signature unknown; restored from __doc__
        """ add_location(self, location:str) """
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

    def get_active_locale(self): # real signature unknown; restored from __doc__
        """ get_active_locale(self) -> str """
        return ""

    def get_artifacts(self): # real signature unknown; restored from __doc__
        """ get_artifacts(self) -> list """
        return []

    def get_checksum(self, kind): # real signature unknown; restored from __doc__
        """ get_checksum(self, kind:AppStream.ChecksumKind) -> AppStream.Checksum or None """
        pass

    def get_checksums(self): # real signature unknown; restored from __doc__
        """ get_checksums(self) -> list """
        return []

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_date(self): # real signature unknown; restored from __doc__
        """ get_date(self) -> str """
        return ""

    def get_date_eol(self): # real signature unknown; restored from __doc__
        """ get_date_eol(self) -> str """
        return ""

    def get_description(self): # real signature unknown; restored from __doc__
        """ get_description(self) -> str or None """
        return ""

    def get_issues(self): # real signature unknown; restored from __doc__
        """ get_issues(self) -> list """
        return []

    def get_kind(self): # real signature unknown; restored from __doc__
        """ get_kind(self) -> AppStream.ReleaseKind """
        pass

    def get_locations(self): # real signature unknown; restored from __doc__
        """ get_locations(self) -> list """
        return []

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_size(self, kind): # real signature unknown; restored from __doc__
        """ get_size(self, kind:AppStream.SizeKind) -> int """
        return 0

    def get_timestamp(self): # real signature unknown; restored from __doc__
        """ get_timestamp(self) -> int """
        return 0

    def get_timestamp_eol(self): # real signature unknown; restored from __doc__
        """ get_timestamp_eol(self) -> int """
        return 0

    def get_urgency(self): # real signature unknown; restored from __doc__
        """ get_urgency(self) -> AppStream.UrgencyKind """
        pass

    def get_url(self, url_kind): # real signature unknown; restored from __doc__
        """ get_url(self, url_kind:AppStream.ReleaseUrlKind) -> str or None """
        return ""

    def get_version(self): # real signature unknown; restored from __doc__
        """ get_version(self) -> str or None """
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

    def kind_from_string(self, kind_str): # real signature unknown; restored from __doc__
        """ kind_from_string(kind_str:str) -> AppStream.ReleaseKind """
        pass

    def kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ kind_to_string(kind:AppStream.ReleaseKind) -> str """
        return ""

    def list_properties(self): # real signature unknown; restored from __doc__
        """ list_properties(self) -> list, n_properties:int """
        return []

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> AppStream.Release """
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

    def run_dispose(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_active_locale(self, locale): # real signature unknown; restored from __doc__
        """ set_active_locale(self, locale:str) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_date(self, date): # real signature unknown; restored from __doc__
        """ set_date(self, date:str) """
        pass

    def set_date_eol(self, date): # real signature unknown; restored from __doc__
        """ set_date_eol(self, date:str) """
        pass

    def set_description(self, description, locale): # real signature unknown; restored from __doc__
        """ set_description(self, description:str, locale:str) """
        pass

    def set_kind(self, kind): # real signature unknown; restored from __doc__
        """ set_kind(self, kind:AppStream.ReleaseKind) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_size(self, size, kind): # real signature unknown; restored from __doc__
        """ set_size(self, size:int, kind:AppStream.SizeKind) """
        pass

    def set_timestamp(self, timestamp): # real signature unknown; restored from __doc__
        """ set_timestamp(self, timestamp:int) """
        pass

    def set_timestamp_eol(self, timestamp): # real signature unknown; restored from __doc__
        """ set_timestamp_eol(self, timestamp:int) """
        pass

    def set_urgency(self, urgency): # real signature unknown; restored from __doc__
        """ set_urgency(self, urgency:AppStream.UrgencyKind) """
        pass

    def set_url(self, url_kind, url): # real signature unknown; restored from __doc__
        """ set_url(self, url_kind:AppStream.ReleaseUrlKind, url:str) """
        pass

    def set_version(self, version): # real signature unknown; restored from __doc__
        """ set_version(self, version:str) """
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

    def url_kind_from_string(self, kind_str): # real signature unknown; restored from __doc__
        """ url_kind_from_string(kind_str:str) -> AppStream.ReleaseUrlKind """
        pass

    def url_kind_to_string(self, kind): # real signature unknown; restored from __doc__
        """ url_kind_to_string(kind:AppStream.ReleaseUrlKind) -> str """
        return ""

    def vercmp(self, rel2): # real signature unknown; restored from __doc__
        """ vercmp(self, rel2:AppStream.Release) -> int """
        return 0

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


    props = None # (!) real value is '<gi._gi.GProps object at 0x7f75420d4910>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(Release), '__module__': 'gi.repository.AppStream', '__gtype__': <GType AsRelease (94779631170576)>, '__doc__': None, '__gsignals__': {}, 'new': gi.FunctionInfo(new), 'kind_from_string': gi.FunctionInfo(kind_from_string), 'kind_to_string': gi.FunctionInfo(kind_to_string), 'url_kind_from_string': gi.FunctionInfo(url_kind_from_string), 'url_kind_to_string': gi.FunctionInfo(url_kind_to_string), 'add_artifact': gi.FunctionInfo(add_artifact), 'add_checksum': gi.FunctionInfo(add_checksum), 'add_issue': gi.FunctionInfo(add_issue), 'add_location': gi.FunctionInfo(add_location), 'get_active_locale': gi.FunctionInfo(get_active_locale), 'get_artifacts': gi.FunctionInfo(get_artifacts), 'get_checksum': gi.FunctionInfo(get_checksum), 'get_checksums': gi.FunctionInfo(get_checksums), 'get_date': gi.FunctionInfo(get_date), 'get_date_eol': gi.FunctionInfo(get_date_eol), 'get_description': gi.FunctionInfo(get_description), 'get_issues': gi.FunctionInfo(get_issues), 'get_kind': gi.FunctionInfo(get_kind), 'get_locations': gi.FunctionInfo(get_locations), 'get_size': gi.FunctionInfo(get_size), 'get_timestamp': gi.FunctionInfo(get_timestamp), 'get_timestamp_eol': gi.FunctionInfo(get_timestamp_eol), 'get_urgency': gi.FunctionInfo(get_urgency), 'get_url': gi.FunctionInfo(get_url), 'get_version': gi.FunctionInfo(get_version), 'set_active_locale': gi.FunctionInfo(set_active_locale), 'set_date': gi.FunctionInfo(set_date), 'set_date_eol': gi.FunctionInfo(set_date_eol), 'set_description': gi.FunctionInfo(set_description), 'set_kind': gi.FunctionInfo(set_kind), 'set_size': gi.FunctionInfo(set_size), 'set_timestamp': gi.FunctionInfo(set_timestamp), 'set_timestamp_eol': gi.FunctionInfo(set_timestamp_eol), 'set_urgency': gi.FunctionInfo(set_urgency), 'set_url': gi.FunctionInfo(set_url), 'set_version': gi.FunctionInfo(set_version), 'vercmp': gi.FunctionInfo(vercmp), 'parent_instance': <property object at 0x7f7542197900>})"
    __gdoc__ = 'Object AsRelease\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType AsRelease (94779631170576)>'
    __info__ = ObjectInfo(Release)


