# encoding: utf-8
# module gi.repository.Gladeui
# from /usr/lib64/girepository-1.0/Gladeui-2.0.typelib
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
import gi.repository.GObject as __gi_repository_GObject
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class SignalDef(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(adaptor:Gladeui.WidgetAdaptor, for_type:GType, signal_id:int) -> Gladeui.SignalDef
    """
    def clone(self): # real signature unknown; restored from __doc__
        """ clone(self) -> Gladeui.SignalDef """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def deprecated(self): # real signature unknown; restored from __doc__
        """ deprecated(self) -> bool """
        return False

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_adaptor(self): # real signature unknown; restored from __doc__
        """ get_adaptor(self) -> Gladeui.WidgetAdaptor """
        pass

    def get_flags(self): # real signature unknown; restored from __doc__
        """ get_flags(self) -> GObject.SignalFlags """
        pass

    def get_name(self): # real signature unknown; restored from __doc__
        """ get_name(self) -> str """
        return ""

    def get_object_type_name(self): # real signature unknown; restored from __doc__
        """ get_object_type_name(self) -> str """
        return ""

    def new(self, adaptor, for_type, signal_id): # real signature unknown; restored from __doc__
        """ new(adaptor:Gladeui.WidgetAdaptor, for_type:GType, signal_id:int) -> Gladeui.SignalDef """
        pass

    def set_deprecated(self, deprecated): # real signature unknown; restored from __doc__
        """ set_deprecated(self, deprecated:bool) """
        pass

    def set_since(self, since_major, since_minor): # real signature unknown; restored from __doc__
        """ set_since(self, since_major:int, since_minor:int) """
        pass

    def since_major(self): # real signature unknown; restored from __doc__
        """ since_major(self) -> int """
        return 0

    def since_minor(self): # real signature unknown; restored from __doc__
        """ since_minor(self) -> int """
        return 0

    def update_from_node(self, node, domain): # real signature unknown; restored from __doc__
        """ update_from_node(self, node:Gladeui.XmlNode, domain:str) """
        pass

    def _clear_boxed(self, *args, **kwargs): # real signature unknown
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

    def __init__(*args, **kwargs): # reliably restored by inspect
        # no doc
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ new(adaptor:Gladeui.WidgetAdaptor, for_type:GType, signal_id:int) -> Gladeui.SignalDef """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(SignalDef), '__module__': 'gi.repository.Gladeui', '__gtype__': <GType GladeSignalDef (94653530807472)>, '__dict__': <attribute '__dict__' of 'SignalDef' objects>, '__weakref__': <attribute '__weakref__' of 'SignalDef' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'clone': gi.FunctionInfo(clone), 'deprecated': gi.FunctionInfo(deprecated), 'free': gi.FunctionInfo(free), 'get_adaptor': gi.FunctionInfo(get_adaptor), 'get_flags': gi.FunctionInfo(get_flags), 'get_name': gi.FunctionInfo(get_name), 'get_object_type_name': gi.FunctionInfo(get_object_type_name), 'set_deprecated': gi.FunctionInfo(set_deprecated), 'set_since': gi.FunctionInfo(set_since), 'since_major': gi.FunctionInfo(since_major), 'since_minor': gi.FunctionInfo(since_minor), 'update_from_node': gi.FunctionInfo(update_from_node), '__new__': <staticmethod object at 0x7f1341a4ba90>, '__init__': <function nothing at 0x7f1342e6cee0>})"
    __gtype__ = None # (!) real value is '<GType GladeSignalDef (94653530807472)>'
    __info__ = StructInfo(SignalDef)


