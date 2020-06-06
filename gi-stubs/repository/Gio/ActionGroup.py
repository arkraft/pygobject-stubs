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


class ActionGroup(__gobject.GInterface):
    # no doc
    def action_added(self, action_name): # real signature unknown; restored from __doc__
        """ action_added(self, action_name:str) """
        pass

    def action_enabled_changed(self, action_name, enabled): # real signature unknown; restored from __doc__
        """ action_enabled_changed(self, action_name:str, enabled:bool) """
        pass

    def action_removed(self, action_name): # real signature unknown; restored from __doc__
        """ action_removed(self, action_name:str) """
        pass

    def action_state_changed(self, action_name, state): # real signature unknown; restored from __doc__
        """ action_state_changed(self, action_name:str, state:GLib.Variant) """
        pass

    def activate_action(self, action_name, parameter=None): # real signature unknown; restored from __doc__
        """ activate_action(self, action_name:str, parameter:GLib.Variant=None) """
        pass

    def change_action_state(self, action_name, value): # real signature unknown; restored from __doc__
        """ change_action_state(self, action_name:str, value:GLib.Variant) """
        pass

    def get_action_enabled(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_enabled(self, action_name:str) -> bool """
        return False

    def get_action_parameter_type(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_parameter_type(self, action_name:str) -> GLib.VariantType or None """
        pass

    def get_action_state(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state(self, action_name:str) -> GLib.Variant or None """
        pass

    def get_action_state_hint(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state_hint(self, action_name:str) -> GLib.Variant or None """
        pass

    def get_action_state_type(self, action_name): # real signature unknown; restored from __doc__
        """ get_action_state_type(self, action_name:str) -> GLib.VariantType or None """
        pass

    def has_action(self, action_name): # real signature unknown; restored from __doc__
        """ has_action(self, action_name:str) -> bool """
        return False

    def list_actions(self): # real signature unknown; restored from __doc__
        """ list_actions(self) -> list """
        return []

    def query_action(self, action_name): # real signature unknown; restored from __doc__
        """ query_action(self, action_name:str) -> bool, enabled:bool, parameter_type:GLib.VariantType, state_type:GLib.VariantType, state_hint:GLib.Variant, state:GLib.Variant """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': InterfaceInfo(ActionGroup), '__module__': 'gi.repository.Gio', '__gtype__': <GType GActionGroup (94269255965424)>, '__dict__': <attribute '__dict__' of 'ActionGroup' objects>, '__weakref__': <attribute '__weakref__' of 'ActionGroup' objects>, '__doc__': None, '__gsignals__': {}, 'action_added': gi.FunctionInfo(action_added), 'action_enabled_changed': gi.FunctionInfo(action_enabled_changed), 'action_removed': gi.FunctionInfo(action_removed), 'action_state_changed': gi.FunctionInfo(action_state_changed), 'activate_action': gi.FunctionInfo(activate_action), 'change_action_state': gi.FunctionInfo(change_action_state), 'get_action_enabled': gi.FunctionInfo(get_action_enabled), 'get_action_parameter_type': gi.FunctionInfo(get_action_parameter_type), 'get_action_state': gi.FunctionInfo(get_action_state), 'get_action_state_hint': gi.FunctionInfo(get_action_state_hint), 'get_action_state_type': gi.FunctionInfo(get_action_state_type), 'has_action': gi.FunctionInfo(has_action), 'list_actions': gi.FunctionInfo(list_actions), 'query_action': gi.FunctionInfo(query_action)})"
    __gdoc__ = 'Interface GActionGroup\n\nSignals from GObject:\n  notify (GParam)\n\n'
    __gsignals__ = {}
    __gtype__ = None # (!) real value is '<GType GActionGroup (94269255965424)>'
    __info__ = InterfaceInfo(ActionGroup)


