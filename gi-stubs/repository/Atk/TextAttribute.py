# encoding: utf-8
# module gi.repository.Atk
# from /usr/lib64/girepository-1.0/Atk-1.0.typelib
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
import gobject as __gobject


class TextAttribute(__gobject.GEnum):
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

    def for_name(self, name): # real signature unknown; restored from __doc__
        """ for_name(name:str) -> Atk.TextAttribute """
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

    def get_name(self, attr): # real signature unknown; restored from __doc__
        """ get_name(attr:Atk.TextAttribute) -> str """
        return ""

    def get_value(self, attr, index_): # real signature unknown; restored from __doc__
        """ get_value(attr:Atk.TextAttribute, index_:int) -> str or None """
        return ""

    def register(self, name): # real signature unknown; restored from __doc__
        """ register(name:str) -> Atk.TextAttribute """
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


    BG_COLOR = 18
    BG_FULL_HEIGHT = 9
    BG_STIPPLE = 20
    DIRECTION = 23
    EDITABLE = 5
    FAMILY_NAME = 17
    FG_COLOR = 19
    FG_STIPPLE = 21
    INDENT = 3
    INVALID = 0
    INVISIBLE = 4
    JUSTIFICATION = 24
    LANGUAGE = 16
    LAST_DEFINED = 29
    LEFT_MARGIN = 1
    PIXELS_ABOVE_LINES = 6
    PIXELS_BELOW_LINES = 7
    PIXELS_INSIDE_WRAP = 8
    RIGHT_MARGIN = 2
    RISE = 10
    SCALE = 14
    SIZE = 13
    STRETCH = 25
    STRIKETHROUGH = 12
    STYLE = 27
    TEXT_POSITION = 28
    UNDERLINE = 11
    VARIANT = 26
    WEIGHT = 15
    WRAP_MODE = 22
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Atk', '__dict__': <attribute '__dict__' of 'TextAttribute' objects>, '__doc__': None, '__gtype__': <GType AtkTextAttribute (93922956064272)>, '__enum_values__': {0: <enum ATK_TEXT_ATTR_INVALID of type Atk.TextAttribute>, 1: <enum ATK_TEXT_ATTR_LEFT_MARGIN of type Atk.TextAttribute>, 2: <enum ATK_TEXT_ATTR_RIGHT_MARGIN of type Atk.TextAttribute>, 3: <enum ATK_TEXT_ATTR_INDENT of type Atk.TextAttribute>, 4: <enum ATK_TEXT_ATTR_INVISIBLE of type Atk.TextAttribute>, 5: <enum ATK_TEXT_ATTR_EDITABLE of type Atk.TextAttribute>, 6: <enum ATK_TEXT_ATTR_PIXELS_ABOVE_LINES of type Atk.TextAttribute>, 7: <enum ATK_TEXT_ATTR_PIXELS_BELOW_LINES of type Atk.TextAttribute>, 8: <enum ATK_TEXT_ATTR_PIXELS_INSIDE_WRAP of type Atk.TextAttribute>, 9: <enum ATK_TEXT_ATTR_BG_FULL_HEIGHT of type Atk.TextAttribute>, 10: <enum ATK_TEXT_ATTR_RISE of type Atk.TextAttribute>, 11: <enum ATK_TEXT_ATTR_UNDERLINE of type Atk.TextAttribute>, 12: <enum ATK_TEXT_ATTR_STRIKETHROUGH of type Atk.TextAttribute>, 13: <enum ATK_TEXT_ATTR_SIZE of type Atk.TextAttribute>, 14: <enum ATK_TEXT_ATTR_SCALE of type Atk.TextAttribute>, 15: <enum ATK_TEXT_ATTR_WEIGHT of type Atk.TextAttribute>, 16: <enum ATK_TEXT_ATTR_LANGUAGE of type Atk.TextAttribute>, 17: <enum ATK_TEXT_ATTR_FAMILY_NAME of type Atk.TextAttribute>, 18: <enum ATK_TEXT_ATTR_BG_COLOR of type Atk.TextAttribute>, 19: <enum ATK_TEXT_ATTR_FG_COLOR of type Atk.TextAttribute>, 20: <enum ATK_TEXT_ATTR_BG_STIPPLE of type Atk.TextAttribute>, 21: <enum ATK_TEXT_ATTR_FG_STIPPLE of type Atk.TextAttribute>, 22: <enum ATK_TEXT_ATTR_WRAP_MODE of type Atk.TextAttribute>, 23: <enum ATK_TEXT_ATTR_DIRECTION of type Atk.TextAttribute>, 24: <enum ATK_TEXT_ATTR_JUSTIFICATION of type Atk.TextAttribute>, 25: <enum ATK_TEXT_ATTR_STRETCH of type Atk.TextAttribute>, 26: <enum ATK_TEXT_ATTR_VARIANT of type Atk.TextAttribute>, 27: <enum ATK_TEXT_ATTR_STYLE of type Atk.TextAttribute>, 28: <enum ATK_TEXT_ATTR_TEXT_POSITION of type Atk.TextAttribute>, 29: <enum ATK_TEXT_ATTR_LAST_DEFINED of type Atk.TextAttribute>}, '__info__': gi.EnumInfo(TextAttribute), 'INVALID': <enum ATK_TEXT_ATTR_INVALID of type Atk.TextAttribute>, 'LEFT_MARGIN': <enum ATK_TEXT_ATTR_LEFT_MARGIN of type Atk.TextAttribute>, 'RIGHT_MARGIN': <enum ATK_TEXT_ATTR_RIGHT_MARGIN of type Atk.TextAttribute>, 'INDENT': <enum ATK_TEXT_ATTR_INDENT of type Atk.TextAttribute>, 'INVISIBLE': <enum ATK_TEXT_ATTR_INVISIBLE of type Atk.TextAttribute>, 'EDITABLE': <enum ATK_TEXT_ATTR_EDITABLE of type Atk.TextAttribute>, 'PIXELS_ABOVE_LINES': <enum ATK_TEXT_ATTR_PIXELS_ABOVE_LINES of type Atk.TextAttribute>, 'PIXELS_BELOW_LINES': <enum ATK_TEXT_ATTR_PIXELS_BELOW_LINES of type Atk.TextAttribute>, 'PIXELS_INSIDE_WRAP': <enum ATK_TEXT_ATTR_PIXELS_INSIDE_WRAP of type Atk.TextAttribute>, 'BG_FULL_HEIGHT': <enum ATK_TEXT_ATTR_BG_FULL_HEIGHT of type Atk.TextAttribute>, 'RISE': <enum ATK_TEXT_ATTR_RISE of type Atk.TextAttribute>, 'UNDERLINE': <enum ATK_TEXT_ATTR_UNDERLINE of type Atk.TextAttribute>, 'STRIKETHROUGH': <enum ATK_TEXT_ATTR_STRIKETHROUGH of type Atk.TextAttribute>, 'SIZE': <enum ATK_TEXT_ATTR_SIZE of type Atk.TextAttribute>, 'SCALE': <enum ATK_TEXT_ATTR_SCALE of type Atk.TextAttribute>, 'WEIGHT': <enum ATK_TEXT_ATTR_WEIGHT of type Atk.TextAttribute>, 'LANGUAGE': <enum ATK_TEXT_ATTR_LANGUAGE of type Atk.TextAttribute>, 'FAMILY_NAME': <enum ATK_TEXT_ATTR_FAMILY_NAME of type Atk.TextAttribute>, 'BG_COLOR': <enum ATK_TEXT_ATTR_BG_COLOR of type Atk.TextAttribute>, 'FG_COLOR': <enum ATK_TEXT_ATTR_FG_COLOR of type Atk.TextAttribute>, 'BG_STIPPLE': <enum ATK_TEXT_ATTR_BG_STIPPLE of type Atk.TextAttribute>, 'FG_STIPPLE': <enum ATK_TEXT_ATTR_FG_STIPPLE of type Atk.TextAttribute>, 'WRAP_MODE': <enum ATK_TEXT_ATTR_WRAP_MODE of type Atk.TextAttribute>, 'DIRECTION': <enum ATK_TEXT_ATTR_DIRECTION of type Atk.TextAttribute>, 'JUSTIFICATION': <enum ATK_TEXT_ATTR_JUSTIFICATION of type Atk.TextAttribute>, 'STRETCH': <enum ATK_TEXT_ATTR_STRETCH of type Atk.TextAttribute>, 'VARIANT': <enum ATK_TEXT_ATTR_VARIANT of type Atk.TextAttribute>, 'STYLE': <enum ATK_TEXT_ATTR_STYLE of type Atk.TextAttribute>, 'TEXT_POSITION': <enum ATK_TEXT_ATTR_TEXT_POSITION of type Atk.TextAttribute>, 'LAST_DEFINED': <enum ATK_TEXT_ATTR_LAST_DEFINED of type Atk.TextAttribute>, 'for_name': gi.FunctionInfo(for_name), 'get_name': gi.FunctionInfo(get_name), 'get_value': gi.FunctionInfo(get_value), 'register': gi.FunctionInfo(register)})"
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
        29: 29,
    }
    __gtype__ = None # (!) real value is '<GType AtkTextAttribute (93922956064272)>'
    __info__ = gi.EnumInfo(TextAttribute)


