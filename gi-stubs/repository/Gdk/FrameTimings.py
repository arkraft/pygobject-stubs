# encoding: utf-8
# module gi.repository.Gdk
# from /usr/lib64/girepository-1.0/Gdk-2.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gi.repository.Gio as __gi_repository_Gio
import gobject as __gobject


class FrameTimings(__gi.Boxed):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def get_complete(self): # real signature unknown; restored from __doc__
        """ get_complete(self) -> bool """
        return False

    def get_frame_counter(self): # real signature unknown; restored from __doc__
        """ get_frame_counter(self) -> int """
        return 0

    def get_frame_time(self): # real signature unknown; restored from __doc__
        """ get_frame_time(self) -> int """
        return 0

    def get_predicted_presentation_time(self): # real signature unknown; restored from __doc__
        """ get_predicted_presentation_time(self) -> int """
        return 0

    def get_presentation_time(self): # real signature unknown; restored from __doc__
        """ get_presentation_time(self) -> int """
        return 0

    def get_refresh_interval(self): # real signature unknown; restored from __doc__
        """ get_refresh_interval(self) -> int """
        return 0

    def ref(self): # real signature unknown; restored from __doc__
        """ ref(self) -> Gdk.FrameTimings """
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

    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(FrameTimings), '__module__': 'gi.repository.Gdk', '__gtype__': <GType GdkFrameTimings (94915769035600)>, '__dict__': <attribute '__dict__' of 'FrameTimings' objects>, '__weakref__': <attribute '__weakref__' of 'FrameTimings' objects>, '__doc__': None, 'get_complete': gi.FunctionInfo(get_complete), 'get_frame_counter': gi.FunctionInfo(get_frame_counter), 'get_frame_time': gi.FunctionInfo(get_frame_time), 'get_predicted_presentation_time': gi.FunctionInfo(get_predicted_presentation_time), 'get_presentation_time': gi.FunctionInfo(get_presentation_time), 'get_refresh_interval': gi.FunctionInfo(get_refresh_interval), 'ref': gi.FunctionInfo(ref), 'unref': gi.FunctionInfo(unref)})"
    __gtype__ = None # (!) real value is '<GType GdkFrameTimings (94915769035600)>'
    __info__ = StructInfo(FrameTimings)


