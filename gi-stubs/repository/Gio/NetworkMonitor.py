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


class NetworkMonitor(__gobject.GInterface):
    # no doc
    def can_reach(self, connectable, cancellable=None): # real signature unknown; restored from __doc__
        """ can_reach(self, connectable:Gio.SocketConnectable, cancellable:Gio.Cancellable=None) -> bool """
        return False

    def can_reach_async(self, connectable, cancellable=None, callback=None, user_data=None): # real signature unknown; restored from __doc__
        """ can_reach_async(self, connectable:Gio.SocketConnectable, cancellable:Gio.Cancellable=None, callback:Gio.AsyncReadyCallback=None, user_data=None) """
        pass

    def can_reach_finish(self, result): # real signature unknown; restored from __doc__
        """ can_reach_finish(self, result:Gio.AsyncResult) -> bool """
        return False

    def get_connectivity(self): # real signature unknown; restored from __doc__
        """ get_connectivity(self) -> Gio.NetworkConnectivity """
        pass

    def get_default(self): # real signature unknown; restored from __doc__
        """ get_default() -> Gio.NetworkMonitor """
        pass

    def get_network_available(self): # real signature unknown; restored from __doc__
        """ get_network_available(self) -> bool """
        return False

    def get_network_metered(self): # real signature unknown; restored from __doc__
        """ get_network_metered(self) -> bool """
        return False

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

    def __init__(self, *args, **kwargs): # real signature unknown
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

    __class__ = None # (!) real value is "<class 'gi.types.GObjectMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(NetworkMonitor), '__module__': 'gi.repository.Gio', '__gtype__': <GType GNetworkMonitor (94125582582368)>, '__dict__': <attribute '__dict__' of 'NetworkMonitor' objects>, '__weakref__': <attribute '__weakref__' of 'NetworkMonitor' objects>, '__doc__': None, '__gsignals__': {}, 'get_default': gi.FunctionInfo(get_default), 'can_reach': gi.FunctionInfo(can_reach), 'can_reach_async': gi.FunctionInfo(can_reach_async), 'can_reach_finish': gi.FunctionInfo(can_reach_finish), 'get_connectivity': gi.FunctionInfo(get_connectivity), 'get_network_available': gi.FunctionInfo(get_network_available), 'get_network_metered': gi.FunctionInfo(get_network_metered)})"
    __gdoc__ = 'Interface GNetworkMonitor\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GNetworkMonitor (94125582582368)>'
    __info__ = InterfaceInfo(NetworkMonitor)


