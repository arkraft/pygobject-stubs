# encoding: utf-8
# module gi.repository.GLib
# from /usr/lib64/girepository-1.0/GLib-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi._option as option # /usr/lib64/python3.8/site-packages/gi/_option.py
from gi._gi import OptionContext, OptionGroup, Pid, spawn_async

import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GLib as __gi_overrides_GLib
import gobject as __gobject


class VariantType(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(type_string:str) -> GLib.VariantType
        new_array(element:GLib.VariantType) -> GLib.VariantType
        new_dict_entry(key:GLib.VariantType, value:GLib.VariantType) -> GLib.VariantType
        new_maybe(element:GLib.VariantType) -> GLib.VariantType
        new_tuple(items:list) -> GLib.VariantType
    """
    def checked_(self, arg0): # real signature unknown; restored from __doc__
        """ checked_(arg0:str) -> GLib.VariantType """
        pass

    def copy(self): # real signature unknown; restored from __doc__
        """ copy(self) -> GLib.VariantType """
        pass

    def dup_string(self): # real signature unknown; restored from __doc__
        """ dup_string(self) -> str """
        return ""

    def element(self): # real signature unknown; restored from __doc__
        """ element(self) -> GLib.VariantType """
        pass

    def equal(self, type2): # real signature unknown; restored from __doc__
        """ equal(self, type2:GLib.VariantType) -> bool """
        return False

    def first(self): # real signature unknown; restored from __doc__
        """ first(self) -> GLib.VariantType """
        pass

    def free(self): # real signature unknown; restored from __doc__
        """ free(self) """
        pass

    def get_string_length(self): # real signature unknown; restored from __doc__
        """ get_string_length(self) -> int """
        return 0

    def hash(self): # real signature unknown; restored from __doc__
        """ hash(self) -> int """
        return 0

    def is_array(self): # real signature unknown; restored from __doc__
        """ is_array(self) -> bool """
        return False

    def is_basic(self): # real signature unknown; restored from __doc__
        """ is_basic(self) -> bool """
        return False

    def is_container(self): # real signature unknown; restored from __doc__
        """ is_container(self) -> bool """
        return False

    def is_definite(self): # real signature unknown; restored from __doc__
        """ is_definite(self) -> bool """
        return False

    def is_dict_entry(self): # real signature unknown; restored from __doc__
        """ is_dict_entry(self) -> bool """
        return False

    def is_maybe(self): # real signature unknown; restored from __doc__
        """ is_maybe(self) -> bool """
        return False

    def is_subtype_of(self, supertype): # real signature unknown; restored from __doc__
        """ is_subtype_of(self, supertype:GLib.VariantType) -> bool """
        return False

    def is_tuple(self): # real signature unknown; restored from __doc__
        """ is_tuple(self) -> bool """
        return False

    def is_variant(self): # real signature unknown; restored from __doc__
        """ is_variant(self) -> bool """
        return False

    def key(self): # real signature unknown; restored from __doc__
        """ key(self) -> GLib.VariantType """
        pass

    def new(self, type_string): # real signature unknown; restored from __doc__
        """ new(type_string:str) -> GLib.VariantType """
        pass

    def new_array(self, element): # real signature unknown; restored from __doc__
        """ new_array(element:GLib.VariantType) -> GLib.VariantType """
        pass

    def new_dict_entry(self, key, value): # real signature unknown; restored from __doc__
        """ new_dict_entry(key:GLib.VariantType, value:GLib.VariantType) -> GLib.VariantType """
        pass

    def new_maybe(self, element): # real signature unknown; restored from __doc__
        """ new_maybe(element:GLib.VariantType) -> GLib.VariantType """
        pass

    def new_tuple(self, items): # real signature unknown; restored from __doc__
        """ new_tuple(items:list) -> GLib.VariantType """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ next(self) -> GLib.VariantType """
        pass

    def n_items(self): # real signature unknown; restored from __doc__
        """ n_items(self) -> int """
        return 0

    def string_get_depth_(self, type_string): # real signature unknown; restored from __doc__
        """ string_get_depth_(type_string:str) -> int """
        return 0

    def string_is_valid(self, type_string): # real signature unknown; restored from __doc__
        """ string_is_valid(type_string:str) -> bool """
        return False

    def string_scan(self, string, limit=None): # real signature unknown; restored from __doc__
        """ string_scan(string:str, limit:str=None) -> bool, endptr:str """
        return False

    def value(self): # real signature unknown; restored from __doc__
        """ value(self) -> GLib.VariantType """
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
        """ new(type_string:str) -> GLib.VariantType """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VariantType), '__module__': 'gi.repository.GLib', '__gtype__': <GType GVariantType (94581033991360)>, '__dict__': <attribute '__dict__' of 'VariantType' objects>, '__weakref__': <attribute '__weakref__' of 'VariantType' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'new_array': gi.FunctionInfo(new_array), 'new_dict_entry': gi.FunctionInfo(new_dict_entry), 'new_maybe': gi.FunctionInfo(new_maybe), 'new_tuple': gi.FunctionInfo(new_tuple), 'copy': gi.FunctionInfo(copy), 'dup_string': gi.FunctionInfo(dup_string), 'element': gi.FunctionInfo(element), 'equal': gi.FunctionInfo(equal), 'first': gi.FunctionInfo(first), 'free': gi.FunctionInfo(free), 'get_string_length': gi.FunctionInfo(get_string_length), 'hash': gi.FunctionInfo(hash), 'is_array': gi.FunctionInfo(is_array), 'is_basic': gi.FunctionInfo(is_basic), 'is_container': gi.FunctionInfo(is_container), 'is_definite': gi.FunctionInfo(is_definite), 'is_dict_entry': gi.FunctionInfo(is_dict_entry), 'is_maybe': gi.FunctionInfo(is_maybe), 'is_subtype_of': gi.FunctionInfo(is_subtype_of), 'is_tuple': gi.FunctionInfo(is_tuple), 'is_variant': gi.FunctionInfo(is_variant), 'key': gi.FunctionInfo(key), 'n_items': gi.FunctionInfo(n_items), 'next': gi.FunctionInfo(next), 'value': gi.FunctionInfo(value), 'checked_': gi.FunctionInfo(checked_), 'string_get_depth_': gi.FunctionInfo(string_get_depth_), 'string_is_valid': gi.FunctionInfo(string_is_valid), 'string_scan': gi.FunctionInfo(string_scan), '__new__': <staticmethod object at 0x7f8513511190>, '__init__': <function nothing at 0x7f85136ebee0>})"
    __gtype__ = None # (!) real value is '<GType GVariantType (94581033991360)>'
    __info__ = StructInfo(VariantType)


