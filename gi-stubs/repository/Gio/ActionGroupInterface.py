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


class ActionGroupInterface(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        ActionGroupInterface()
    """
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

    def __init__(self): # real signature unknown; restored from __doc__
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

    action_added = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    action_enabled_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    action_removed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    action_state_changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    activate_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    change_action_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_action_enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_action_parameter_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_action_state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_action_state_hint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    get_action_state_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    g_iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    list_actions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    query_action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ActionGroupInterface), '__module__': 'gi.repository.Gio', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'ActionGroupInterface' objects>, '__weakref__': <attribute '__weakref__' of 'ActionGroupInterface' objects>, '__doc__': None, 'g_iface': <property object at 0x7f28ddf28d10>, 'has_action': <property object at 0x7f28ddf28e00>, 'list_actions': <property object at 0x7f28ddf28ef0>, 'get_action_enabled': <property object at 0x7f28ddfa1090>, 'get_action_parameter_type': <property object at 0x7f28ddfa1180>, 'get_action_state_type': <property object at 0x7f28ddfa1270>, 'get_action_state_hint': <property object at 0x7f28ddfa1360>, 'get_action_state': <property object at 0x7f28ddfa1450>, 'change_action_state': <property object at 0x7f28ddfa1540>, 'activate_action': <property object at 0x7f28ddfa15e0>, 'action_added': <property object at 0x7f28ddfa16d0>, 'action_removed': <property object at 0x7f28ddfa17c0>, 'action_enabled_changed': <property object at 0x7f28ddfa1900>, 'action_state_changed': <property object at 0x7f28ddfa19f0>, 'query_action': <property object at 0x7f28ddfa1a90>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(ActionGroupInterface)


