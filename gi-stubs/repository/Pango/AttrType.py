# encoding: utf-8
# module gi.repository.Pango
# from /usr/lib64/girepository-1.0/Pango-1.0.typelib
# by generator 1.147
# no doc

# imports
import gi as __gi
import gi.overrides as __gi_overrides
import gi.overrides.GObject as __gi_overrides_GObject
import gobject as __gobject


class AttrType(__gobject.GEnum):
    # no doc
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        Return integer ratio.
        
        Return a pair of integers, whose ratio is exactly equal to the original int
        and with a positive denominator.
        
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        """
        pass

    def bit_length(self): # real signature unknown; restored from __doc__
        """
        Number of bits necessary to represent self in binary.
        
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        """
        pass

    def conjugate(self, *args, **kwargs): # real signature unknown
        """ Returns self, the complex conjugate of any int. """
        pass

    def from_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return the integer represented by the given array of bytes.
        
          bytes
            Holds the array of bytes to convert.  The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Indicates whether two's complement is used to represent the integer.
        """
        pass

    def get_name(self, type): # real signature unknown; restored from __doc__
        """ get_name(type:Pango.AttrType) -> str or None """
        return ""

    def register(self, name): # real signature unknown; restored from __doc__
        """ register(name:str) -> Pango.AttrType """
        pass

    def to_bytes(self, *args, **kwargs): # real signature unknown
        """
        Return an array of bytes representing an integer.
        
          length
            Length of bytes object to use.  An OverflowError is raised if the
            integer is not representable with the given number of bytes.
          byteorder
            The byte order used to represent the integer.  If byteorder is 'big',
            the most significant byte is at the beginning of the byte array.  If
            byteorder is 'little', the most significant byte is at the end of the
            byte array.  To request the native byte order of the host system, use
            `sys.byteorder' as the byte order value.
          signed
            Determines whether two's complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __ceil__(self, *args, **kwargs): # real signature unknown
        """ Ceiling of an Integral returns itself. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __floor__(self, *args, **kwargs): # real signature unknown
        """ Flooring an Integral returns itself. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __round__(self, *args, **kwargs): # real signature unknown
        """
        Rounding an Integral returns itself.
        Rounding with an ndigits argument also returns an integer.
        """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Returns size in memory, in bytes. """
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

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs): # real signature unknown
        """ Truncating an Integral returns itself. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    denominator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the denominator of a rational number in lowest terms"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    numerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the numerator of a rational number in lowest terms"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""

    value_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value_nick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ABSOLUTE_SIZE = 20
    ALLOW_BREAKS = 26
    BACKGROUND = 10
    BACKGROUND_ALPHA = 25
    FALLBACK = 16
    FAMILY = 2
    FONT_DESC = 8
    FONT_FEATURES = 23
    FOREGROUND = 9
    FOREGROUND_ALPHA = 24
    GRAVITY = 21
    GRAVITY_HINT = 22
    INSERT_HYPHENS = 28
    INVALID = 0
    LANGUAGE = 1
    LETTER_SPACING = 17
    RISE = 13
    SCALE = 15
    SHAPE = 14
    SHOW = 27
    SIZE = 7
    STRETCH = 6
    STRIKETHROUGH = 12
    STRIKETHROUGH_COLOR = 19
    STYLE = 3
    UNDERLINE = 11
    UNDERLINE_COLOR = 18
    VARIANT = 5
    WEIGHT = 4
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Pango', '__dict__': <attribute '__dict__' of 'AttrType' objects>, '__doc__': None, '__gtype__': <GType PangoAttrType (94187428956224)>, '__enum_values__': {0: <enum PANGO_ATTR_INVALID of type Pango.AttrType>, 1: <enum PANGO_ATTR_LANGUAGE of type Pango.AttrType>, 2: <enum PANGO_ATTR_FAMILY of type Pango.AttrType>, 3: <enum PANGO_ATTR_STYLE of type Pango.AttrType>, 4: <enum PANGO_ATTR_WEIGHT of type Pango.AttrType>, 5: <enum PANGO_ATTR_VARIANT of type Pango.AttrType>, 6: <enum PANGO_ATTR_STRETCH of type Pango.AttrType>, 7: <enum PANGO_ATTR_SIZE of type Pango.AttrType>, 8: <enum PANGO_ATTR_FONT_DESC of type Pango.AttrType>, 9: <enum PANGO_ATTR_FOREGROUND of type Pango.AttrType>, 10: <enum PANGO_ATTR_BACKGROUND of type Pango.AttrType>, 11: <enum PANGO_ATTR_UNDERLINE of type Pango.AttrType>, 12: <enum PANGO_ATTR_STRIKETHROUGH of type Pango.AttrType>, 13: <enum PANGO_ATTR_RISE of type Pango.AttrType>, 14: <enum PANGO_ATTR_SHAPE of type Pango.AttrType>, 15: <enum PANGO_ATTR_SCALE of type Pango.AttrType>, 16: <enum PANGO_ATTR_FALLBACK of type Pango.AttrType>, 17: <enum PANGO_ATTR_LETTER_SPACING of type Pango.AttrType>, 18: <enum PANGO_ATTR_UNDERLINE_COLOR of type Pango.AttrType>, 19: <enum PANGO_ATTR_STRIKETHROUGH_COLOR of type Pango.AttrType>, 20: <enum PANGO_ATTR_ABSOLUTE_SIZE of type Pango.AttrType>, 21: <enum PANGO_ATTR_GRAVITY of type Pango.AttrType>, 22: <enum PANGO_ATTR_GRAVITY_HINT of type Pango.AttrType>, 23: <enum PANGO_ATTR_FONT_FEATURES of type Pango.AttrType>, 24: <enum PANGO_ATTR_FOREGROUND_ALPHA of type Pango.AttrType>, 25: <enum PANGO_ATTR_BACKGROUND_ALPHA of type Pango.AttrType>, 26: <enum PANGO_ATTR_ALLOW_BREAKS of type Pango.AttrType>, 27: <enum PANGO_ATTR_SHOW of type Pango.AttrType>, 28: <enum PANGO_ATTR_INSERT_HYPHENS of type Pango.AttrType>}, '__info__': gi.EnumInfo(AttrType), 'INVALID': <enum PANGO_ATTR_INVALID of type Pango.AttrType>, 'LANGUAGE': <enum PANGO_ATTR_LANGUAGE of type Pango.AttrType>, 'FAMILY': <enum PANGO_ATTR_FAMILY of type Pango.AttrType>, 'STYLE': <enum PANGO_ATTR_STYLE of type Pango.AttrType>, 'WEIGHT': <enum PANGO_ATTR_WEIGHT of type Pango.AttrType>, 'VARIANT': <enum PANGO_ATTR_VARIANT of type Pango.AttrType>, 'STRETCH': <enum PANGO_ATTR_STRETCH of type Pango.AttrType>, 'SIZE': <enum PANGO_ATTR_SIZE of type Pango.AttrType>, 'FONT_DESC': <enum PANGO_ATTR_FONT_DESC of type Pango.AttrType>, 'FOREGROUND': <enum PANGO_ATTR_FOREGROUND of type Pango.AttrType>, 'BACKGROUND': <enum PANGO_ATTR_BACKGROUND of type Pango.AttrType>, 'UNDERLINE': <enum PANGO_ATTR_UNDERLINE of type Pango.AttrType>, 'STRIKETHROUGH': <enum PANGO_ATTR_STRIKETHROUGH of type Pango.AttrType>, 'RISE': <enum PANGO_ATTR_RISE of type Pango.AttrType>, 'SHAPE': <enum PANGO_ATTR_SHAPE of type Pango.AttrType>, 'SCALE': <enum PANGO_ATTR_SCALE of type Pango.AttrType>, 'FALLBACK': <enum PANGO_ATTR_FALLBACK of type Pango.AttrType>, 'LETTER_SPACING': <enum PANGO_ATTR_LETTER_SPACING of type Pango.AttrType>, 'UNDERLINE_COLOR': <enum PANGO_ATTR_UNDERLINE_COLOR of type Pango.AttrType>, 'STRIKETHROUGH_COLOR': <enum PANGO_ATTR_STRIKETHROUGH_COLOR of type Pango.AttrType>, 'ABSOLUTE_SIZE': <enum PANGO_ATTR_ABSOLUTE_SIZE of type Pango.AttrType>, 'GRAVITY': <enum PANGO_ATTR_GRAVITY of type Pango.AttrType>, 'GRAVITY_HINT': <enum PANGO_ATTR_GRAVITY_HINT of type Pango.AttrType>, 'FONT_FEATURES': <enum PANGO_ATTR_FONT_FEATURES of type Pango.AttrType>, 'FOREGROUND_ALPHA': <enum PANGO_ATTR_FOREGROUND_ALPHA of type Pango.AttrType>, 'BACKGROUND_ALPHA': <enum PANGO_ATTR_BACKGROUND_ALPHA of type Pango.AttrType>, 'ALLOW_BREAKS': <enum PANGO_ATTR_ALLOW_BREAKS of type Pango.AttrType>, 'SHOW': <enum PANGO_ATTR_SHOW of type Pango.AttrType>, 'INSERT_HYPHENS': <enum PANGO_ATTR_INSERT_HYPHENS of type Pango.AttrType>, 'get_name': gi.FunctionInfo(get_name), 'register': gi.FunctionInfo(register)})"
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
    }
    __gtype__ = None # (!) real value is '<GType PangoAttrType (94187428956224)>'
    __info__ = gi.EnumInfo(AttrType)


