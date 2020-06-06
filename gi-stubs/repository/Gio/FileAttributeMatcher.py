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


class FileAttributeMatcher(__gi.Boxed):
    """
    :Constructors:
    
    ::
    
        new(attributes:str) -> Gio.FileAttributeMatcher
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def enumerate_namespace(self, ns): # real signature unknown; restored from __doc__
        """ enumerate_namespace(self, ns:str) -> bool """
        return False

    def enumerate_next(self): # real signature unknown; restored from __doc__
        """ enumerate_next(self) -> str """
        return ""

    def matches(self, attribute): # real signature unknown; restored from __doc__
        """ matches(self, attribute:str) -> bool """
        return False

    def matches_only(self, attribute): # real signature unknown; restored from __doc__
        """ matches_only(self, attribute:str) -> bool """
        return False

    def new(self, attributes): # real signature unknown; restored from __doc__
        """ new(attributes:str) -> Gio.FileAttributeMatcher """
        pass

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gio.FileAttributeMatcher """
        pass

    def subtract(self, subtract): # real signature unknown; restored from __doc__
        """ subtract(self, subtract:Gio.FileAttributeMatcher) -> Gio.FileAttributeMatcher """
        pass

    def to_string(self): # real signature unknown; restored from __doc__
        """ to_string(self) -> str """
        return ""

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
        """ new(attributes:str) -> Gio.FileAttributeMatcher """
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
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FileAttributeMatcher), '__module__': 'gi.repository.Gio', '__gtype__': <GType GFileAttributeMatcher (94269256904432)>, '__dict__': <attribute '__dict__' of 'FileAttributeMatcher' objects>, '__weakref__': <attribute '__weakref__' of 'FileAttributeMatcher' objects>, '__doc__': None, 'new': gi.FunctionInfo(new), 'enumerate_namespace': gi.FunctionInfo(enumerate_namespace), 'enumerate_next': gi.FunctionInfo(enumerate_next), 'matches': gi.FunctionInfo(matches), 'matches_only': gi.FunctionInfo(matches_only), 'ref': gi.FunctionInfo(ref), 'subtract': gi.FunctionInfo(subtract), 'to_string': gi.FunctionInfo(to_string), 'unref': gi.FunctionInfo(unref), '__new__': <staticmethod object at 0x7f4b8804d910>, '__init__': <function nothing at 0x7f4b882c3ee0>})"
    __gtype__ = None # (!) real value is '<GType GFileAttributeMatcher (94269256904432)>'
    __info__ = StructInfo(FileAttributeMatcher)


