# encoding: utf-8
# module gi.repository.GstRtsp
# from /usr/lib64/girepository-1.0/GstRtsp-1.0.typelib
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
import gobject as __gobject


class RTSPRange(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        RTSPRange()
    """
    def convert_units(self, range, unit): # real signature unknown; restored from __doc__
        """ convert_units(range:GstRtsp.RTSPTimeRange, unit:GstRtsp.RTSPRangeUnit) -> bool """
        return False

    def free(self, range): # real signature unknown; restored from __doc__
        """ free(range:GstRtsp.RTSPTimeRange) """
        pass

    def get_times(self, range): # real signature unknown; restored from __doc__
        """ get_times(range:GstRtsp.RTSPTimeRange) -> bool, min:int, max:int """
        return False

    def parse(self, rangestr): # real signature unknown; restored from __doc__
        """ parse(rangestr:str) -> GstRtsp.RTSPResult, range:GstRtsp.RTSPTimeRange """
        pass

    def to_string(self, range): # real signature unknown; restored from __doc__
        """ to_string(range:GstRtsp.RTSPTimeRange) -> str """
        return ""

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

    max = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(RTSPRange), '__module__': 'gi.repository.GstRtsp', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'RTSPRange' objects>, '__weakref__': <attribute '__weakref__' of 'RTSPRange' objects>, '__doc__': None, 'min': <property object at 0x7ff1b34d83b0>, 'max': <property object at 0x7ff1b34d84a0>, 'convert_units': gi.FunctionInfo(convert_units), 'free': gi.FunctionInfo(free), 'get_times': gi.FunctionInfo(get_times), 'parse': gi.FunctionInfo(parse), 'to_string': gi.FunctionInfo(to_string)})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(RTSPRange)


