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


class VariantBuilder(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(type:GLib.VariantType) -> GLib.VariantBuilder
    """
    def add_value(self, value): # real signature unknown; restored from __doc__
        """ add_value(self, value:GLib.Variant) """
        pass

    def close(self): # real signature unknown; restored from __doc__
        """ close(self) """
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def end(self): # real signature unknown; restored from __doc__
        """ end(self) -> GLib.Variant """
        pass

    def new(self, type): # real signature unknown; restored from __doc__
        """ new(type:GLib.VariantType) -> GLib.VariantBuilder """
        pass

    def open(self, type): # real signature unknown; restored from __doc__
        """ open(self, type:GLib.VariantType) """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> GLib.VariantBuilder """
        pass

    def unref(self): # real signature unknown; restored from __doc__
        """ unref(self) """
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
        """ new(type:GLib.VariantType) -> GLib.VariantBuilder """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(VariantBuilder), '__module__': 'gi.repository.GLib', '__gtype__': <GType GVariantBuilder (94581033953632)>, '__dict__': <attribute '__dict__' of 'VariantBuilder' objects>, '__weakref__': <attribute '__weakref__' of 'VariantBuilder' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'add_value': gi.FunctionInfo(add_value), 'close': gi.FunctionInfo(close), 'end': gi.FunctionInfo(end), 'open': gi.FunctionInfo(open), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7f8513511070>, '__init__': <function nothing at 0x7f85136ebee0>})"
    __gtype__ = None # (!) real value is '<GType GVariantBuilder (94581033953632)>'
    __info__ = StructInfo(VariantBuilder)


