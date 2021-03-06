# encoding: utf-8
# module gi.repository.GUPnPAV
# from /usr/lib64/girepository-1.0/GUPnPAV-1.0.typelib
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


class DIDLLiteResource(__gi_overrides_GObject.Object):
    """
    :Constructors:
    
    ::
    
        DIDLLiteResource(**properties)
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

    def get_audio_channels(self): # real signature unknown; restored from __doc__
        """ get_audio_channels(self) -> int """
        return 0

    def get_bitrate(self): # real signature unknown; restored from __doc__
        """ get_bitrate(self) -> int """
        return 0

    def get_bits_per_sample(self): # real signature unknown; restored from __doc__
        """ get_bits_per_sample(self) -> int """
        return 0

    def get_cleartext_size(self): # real signature unknown; restored from __doc__
        """ get_cleartext_size(self) -> int """
        return 0

    def get_color_depth(self): # real signature unknown; restored from __doc__
        """ get_color_depth(self) -> int """
        return 0

    def get_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_dlna_namespace(self): # real signature unknown; restored from __doc__
        """ get_dlna_namespace(self) -> libxml2.NsPtr """
        pass

    def get_duration(self): # real signature unknown; restored from __doc__
        """ get_duration(self) -> int """
        return 0

    def get_height(self): # real signature unknown; restored from __doc__
        """ get_height(self) -> int """
        return 0

    def get_import_uri(self): # real signature unknown; restored from __doc__
        """ get_import_uri(self) -> str """
        return ""

    def get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_protection(self): # real signature unknown; restored from __doc__
        """ get_protection(self) -> str """
        return ""

    def get_protocol_info(self): # real signature unknown; restored from __doc__
        """ get_protocol_info(self) -> GUPnPAV.ProtocolInfo """
        pass

    def get_pv_namespace(self): # real signature unknown; restored from __doc__
        """ get_pv_namespace(self) -> libxml2.NsPtr """
        pass

    def get_qdata(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def get_sample_freq(self): # real signature unknown; restored from __doc__
        """ get_sample_freq(self) -> int """
        return 0

    def get_size(self): # real signature unknown; restored from __doc__
        """ get_size(self) -> int """
        return 0

    def get_size64(self): # real signature unknown; restored from __doc__
        """ get_size64(self) -> int """
        return 0

    def get_subtitle_file_type(self): # real signature unknown; restored from __doc__
        """ get_subtitle_file_type(self) -> str """
        return ""

    def get_subtitle_file_uri(self): # real signature unknown; restored from __doc__
        """ get_subtitle_file_uri(self) -> str """
        return ""

    def get_track_total(self): # real signature unknown; restored from __doc__
        """ get_track_total(self) -> int """
        return 0

    def get_update_count(self): # real signature unknown; restored from __doc__
        """ get_update_count(self) -> int """
        return 0

    def get_uri(self): # real signature unknown; restored from __doc__
        """ get_uri(self) -> str """
        return ""

    def get_width(self): # real signature unknown; restored from __doc__
        """ get_width(self) -> int """
        return 0

    def get_xml_node(self): # real signature unknown; restored from __doc__
        """ get_xml_node(self) -> libxml2.Node """
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

    def set_audio_channels(self, n_channels): # real signature unknown; restored from __doc__
        """ set_audio_channels(self, n_channels:int) """
        pass

    def set_bitrate(self, bitrate): # real signature unknown; restored from __doc__
        """ set_bitrate(self, bitrate:int) """
        pass

    def set_bits_per_sample(self, sample_size): # real signature unknown; restored from __doc__
        """ set_bits_per_sample(self, sample_size:int) """
        pass

    def set_cleartext_size(self, cleartext_size): # real signature unknown; restored from __doc__
        """ set_cleartext_size(self, cleartext_size:int) """
        pass

    def set_color_depth(self, color_depth): # real signature unknown; restored from __doc__
        """ set_color_depth(self, color_depth:int) """
        pass

    def set_data(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def set_duration(self, duration): # real signature unknown; restored from __doc__
        """ set_duration(self, duration:int) """
        pass

    def set_height(self, height): # real signature unknown; restored from __doc__
        """ set_height(self, height:int) """
        pass

    def set_import_uri(self, import_uri): # real signature unknown; restored from __doc__
        """ set_import_uri(self, import_uri:str) """
        pass

    def set_properties(self, *args, **kwargs): # real signature unknown
        pass

    def set_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_protection(self, protection): # real signature unknown; restored from __doc__
        """ set_protection(self, protection:str) """
        pass

    def set_protocol_info(self, info): # real signature unknown; restored from __doc__
        """ set_protocol_info(self, info:GUPnPAV.ProtocolInfo) """
        pass

    def set_sample_freq(self, sample_freq): # real signature unknown; restored from __doc__
        """ set_sample_freq(self, sample_freq:int) """
        pass

    def set_size(self, size): # real signature unknown; restored from __doc__
        """ set_size(self, size:int) """
        pass

    def set_size64(self, size): # real signature unknown; restored from __doc__
        """ set_size64(self, size:int) """
        pass

    def set_subtitle_file_type(self, type=None): # real signature unknown; restored from __doc__
        """ set_subtitle_file_type(self, type:str=None) """
        pass

    def set_subtitle_file_uri(self, uri=None): # real signature unknown; restored from __doc__
        """ set_subtitle_file_uri(self, uri:str=None) """
        pass

    def set_track_total(self, track_total): # real signature unknown; restored from __doc__
        """ set_track_total(self, track_total:int) """
        pass

    def set_update_count(self, update_count): # real signature unknown; restored from __doc__
        """ set_update_count(self, update_count:int) """
        pass

    def set_uri(self, uri): # real signature unknown; restored from __doc__
        """ set_uri(self, uri:str) """
        pass

    def set_width(self, width): # real signature unknown; restored from __doc__
        """ set_width(self, width:int) """
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

    def track_total_is_set(self): # real signature unknown; restored from __doc__
        """ track_total_is_set(self) -> bool """
        return False

    def unref(self, *args, **kargs): # reliably restored by inspect
        # no doc
        pass

    def unset_track_total(self): # real signature unknown; restored from __doc__
        """ unset_track_total(self) """
        pass

    def unset_update_count(self): # real signature unknown; restored from __doc__
        """ unset_update_count(self) """
        pass

    def update_count_is_set(self): # real signature unknown; restored from __doc__
        """ update_count_is_set(self) -> bool """
        return False

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

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    priv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ref_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __gpointer__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __grefcount__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    props = None # (!) real value is '<gi._gi.GProps object at 0x7fda4e242f10>'
    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': ObjectInfo(DIDLLiteResource), '__module__': 'gi.repository.GUPnPAV', '__gtype__': <GType GUPnPDIDLLiteResource (94653147774656)>, '__doc__': None, '__gsignals__': {}, 'get_audio_channels': gi.FunctionInfo(get_audio_channels), 'get_bitrate': gi.FunctionInfo(get_bitrate), 'get_bits_per_sample': gi.FunctionInfo(get_bits_per_sample), 'get_cleartext_size': gi.FunctionInfo(get_cleartext_size), 'get_color_depth': gi.FunctionInfo(get_color_depth), 'get_dlna_namespace': gi.FunctionInfo(get_dlna_namespace), 'get_duration': gi.FunctionInfo(get_duration), 'get_height': gi.FunctionInfo(get_height), 'get_import_uri': gi.FunctionInfo(get_import_uri), 'get_protection': gi.FunctionInfo(get_protection), 'get_protocol_info': gi.FunctionInfo(get_protocol_info), 'get_pv_namespace': gi.FunctionInfo(get_pv_namespace), 'get_sample_freq': gi.FunctionInfo(get_sample_freq), 'get_size': gi.FunctionInfo(get_size), 'get_size64': gi.FunctionInfo(get_size64), 'get_subtitle_file_type': gi.FunctionInfo(get_subtitle_file_type), 'get_subtitle_file_uri': gi.FunctionInfo(get_subtitle_file_uri), 'get_track_total': gi.FunctionInfo(get_track_total), 'get_update_count': gi.FunctionInfo(get_update_count), 'get_uri': gi.FunctionInfo(get_uri), 'get_width': gi.FunctionInfo(get_width), 'get_xml_node': gi.FunctionInfo(get_xml_node), 'set_audio_channels': gi.FunctionInfo(set_audio_channels), 'set_bitrate': gi.FunctionInfo(set_bitrate), 'set_bits_per_sample': gi.FunctionInfo(set_bits_per_sample), 'set_cleartext_size': gi.FunctionInfo(set_cleartext_size), 'set_color_depth': gi.FunctionInfo(set_color_depth), 'set_duration': gi.FunctionInfo(set_duration), 'set_height': gi.FunctionInfo(set_height), 'set_import_uri': gi.FunctionInfo(set_import_uri), 'set_protection': gi.FunctionInfo(set_protection), 'set_protocol_info': gi.FunctionInfo(set_protocol_info), 'set_sample_freq': gi.FunctionInfo(set_sample_freq), 'set_size': gi.FunctionInfo(set_size), 'set_size64': gi.FunctionInfo(set_size64), 'set_subtitle_file_type': gi.FunctionInfo(set_subtitle_file_type), 'set_subtitle_file_uri': gi.FunctionInfo(set_subtitle_file_uri), 'set_track_total': gi.FunctionInfo(set_track_total), 'set_update_count': gi.FunctionInfo(set_update_count), 'set_uri': gi.FunctionInfo(set_uri), 'set_width': gi.FunctionInfo(set_width), 'track_total_is_set': gi.FunctionInfo(track_total_is_set), 'unset_track_total': gi.FunctionInfo(unset_track_total), 'unset_update_count': gi.FunctionInfo(unset_update_count), 'update_count_is_set': gi.FunctionInfo(update_count_is_set), 'parent': <property object at 0x7fda4e184590>, 'priv': <property object at 0x7fda4e184680>})"
    __gdoc__ = 'Object GUPnPDIDLLiteResource\n\nProperties from GUPnPDIDLLiteResource:\n  xml-node -> gpointer: XMLNode\n    The pointer to res node in XML document.\n  xml-doc -> GUPnPAVXMLDoc: XMLDoc\n    The reference to XML document containing this object.\n  dlna-namespace -> gpointer: XML namespace\n    Pointer to the DLNA metadata namespace registered with the resource.\n  pv-namespace -> gpointer: XML namespace\n    Pointer to the PV metadata namespace registered with the resource.\n  uri -> gchararray: URI\n    The URI associated with this resource\n  import-uri -> gchararray: ImportURI\n    The import URI associated with this resource\n  protocol-info -> GUPnPProtocolInfo: ProtocolInfo\n    The protocol info associated with this resource\n  size -> glong: Size\n    The size (in bytes) of this resource.\n  size64 -> gint64: Size64\n    The size (in bytes) of this resource.\n  cleartext-size -> gint64: ClearTextSize\n    The clear text size (in bytes) of this resource.\n  duration -> glong: Duration\n    The duration (in seconds) of this resource.\n  bitrate -> gint: Bitrate\n    The bitrate of this resource.\n  sample-freq -> gint: SampleFrequency\n    The sample frequency of this resource.\n  bits-per-sample -> gint: BitsPerSample\n    The sample size of this resource.\n  protection -> gchararray: Protection\n    The protection system used by this resource.\n  audio-channels -> gint: AudioChannels\n    The number of audio channels in this resource.\n  width -> gint: Width\n    The width of this image/video resource.\n  height -> gint: Height\n    The height of this image/video resource.\n  color-depth -> gint: ColorDepth\n    The color-depth of this image/video resource.\n  update-count -> guint: UpdateCount\n    The update count of this resource.\n  track-total -> guint: TrackTotal\n    The number of tracks of this resource.\n  subtitle-file-type -> gchararray: Subtitle file type\n    Type of the external subtitle file\n  subtitle-file-uri -> gchararray: Subtitle file uri\n    Uri of the external subtitle file\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GUPnPDIDLLiteResource (94653147774656)>'
    __info__ = ObjectInfo(DIDLLiteResource)


