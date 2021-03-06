# encoding: utf-8
# module gi.repository.ECal
# from /usr/lib64/girepository-1.0/ECal-2.0.typelib
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
import gi.repository.EDataServer as __gi_repository_EDataServer
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class ComponentParameterBag(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new() -> ECal.ComponentParameterBag
        new_from_property(property:ICalGLib.Property, func:ECal.ComponentParameterBagFilterFunc=None, user_data=None) -> ECal.ComponentParameterBag
    """
    def add(self, param): # real signature unknown; restored from __doc__
        """ add(self, param:ICalGLib.Parameter) """
        pass

    def assign(self, src_bag): # real signature unknown; restored from __doc__
        """ assign(self, src_bag:ECal.ComponentParameterBag) """
        pass

    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self) """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> ECal.ComponentParameterBag """
        pass

    def fill_property(self, property): # real signature unknown; restored from __doc__
        """ fill_property(self, property:ICalGLib.Property) """
        pass

    def get(self, index): # real signature unknown; restored from __doc__
        """ get(self, index:int) -> ICalGLib.Parameter or None """
        pass

    def get_count(self): # real signature unknown; restored from __doc__
        """ get_count(self) -> int """
        return 0

    def get_first_by_kind(self, kind): # real signature unknown; restored from __doc__
        """ get_first_by_kind(self, kind:ICalGLib.ParameterKind) -> int """
        return 0

    def new(self): # real signature unknown; restored from __doc__
        """ new() -> ECal.ComponentParameterBag """
        pass

    def new_from_property(self, property, func=None, user_data=None): # real signature unknown; restored from __doc__
        """ new_from_property(property:ICalGLib.Property, func:ECal.ComponentParameterBagFilterFunc=None, user_data=None) -> ECal.ComponentParameterBag """
        pass

    def remove(self, index): # real signature unknown; restored from __doc__
        """ remove(self, index:int) """
        pass

    def remove_by_kind(self, kind, all): # real signature unknown; restored from __doc__
        """ remove_by_kind(self, kind:ICalGLib.ParameterKind, all:bool) -> int """
        return 0

    def set_from_property(self, property, func=None, user_data=None): # real signature unknown; restored from __doc__
        """ set_from_property(self, property:ICalGLib.Property, func:ECal.ComponentParameterBagFilterFunc=None, user_data=None) """
        pass

    def take(self, param): # real signature unknown; restored from __doc__
        """ take(self, param:ICalGLib.Parameter) """
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
        """ new() -> ECal.ComponentParameterBag """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(ComponentParameterBag), '__module__': 'gi.repository.ECal', '__gtype__': <GType ECalComponentParameterBag (94764814897200)>, '__dict__': <attribute '__dict__' of 'ComponentParameterBag' objects>, '__weakref__': <attribute '__weakref__' of 'ComponentParameterBag' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_from_property': gi.FunctionInfo(new_from_property), 'add': gi.FunctionInfo(add), 'assign': gi.FunctionInfo(assign), 'clear': gi.FunctionInfo(clear), 'copy': gi.FunctionInfo(copy), 'fill_property': gi.FunctionInfo(fill_property), 'get': gi.FunctionInfo(get), 'get_count': gi.FunctionInfo(get_count), 'get_first_by_kind': gi.FunctionInfo(get_first_by_kind), 'remove': gi.FunctionInfo(remove), 'remove_by_kind': gi.FunctionInfo(remove_by_kind), 'set_from_property': gi.FunctionInfo(set_from_property), 'take': gi.FunctionInfo(take), '__new__': <staticmethod object at 0x7fe5cce05c70>, '__init__': <function nothing at 0x7fe5cd0d7ee0>})"
    __gtype__ = None # (!) real value is '<GType ECalComponentParameterBag (94764814897200)>'
    __info__ = StructInfo(ComponentParameterBag)


