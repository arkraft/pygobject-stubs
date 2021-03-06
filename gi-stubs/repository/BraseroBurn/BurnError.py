# encoding: utf-8
# module gi.repository.BraseroBurn
# from /usr/lib64/girepository-1.0/BraseroBurn-3.1.typelib
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
import gi.overrides.Gtk as __gi_overrides_Gtk
import gi.repository.Gtk as __gi_repository_Gtk
import gobject as __gobject


class BurnError(__gobject.GEnum):
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


    ERROR_BAD_CHECKSUM = 27
    ERROR_DISK_SPACE = 6
    ERROR_DRIVE_BUSY = 5
    ERROR_EMPTY = 7
    ERROR_ENCRYPTION_KEY = 32
    ERROR_FILE_FOLDER = 11
    ERROR_FILE_INVALID = 10
    ERROR_FILE_NOT_FOUND = 13
    ERROR_FILE_NOT_LOCAL = 14
    ERROR_FILE_PLAYLIST = 12
    ERROR_GENERAL = 1
    ERROR_IMAGE_INVALID = 17
    ERROR_IMAGE_JOLIET = 18
    ERROR_IMAGE_LAST_SESSION = 19
    ERROR_INPUT_INVALID = 8
    ERROR_MEDIUM_INVALID = 21
    ERROR_MEDIUM_NEED_RELOADING = 26
    ERROR_MEDIUM_NONE = 20
    ERROR_MEDIUM_NOT_REWRITABLE = 25
    ERROR_MEDIUM_NOT_WRITABLE = 24
    ERROR_MEDIUM_NO_DATA = 23
    ERROR_MEDIUM_SPACE = 22
    ERROR_MISSING_APP_AND_PLUGIN = 28
    ERROR_NONE = 0
    ERROR_OUTPUT_NONE = 9
    ERROR_PERMISSION = 4
    ERROR_PLUGIN_MISBEHAVIOR = 2
    ERROR_SLOW_DMA = 3
    ERROR_TMP_DIRECTORY = 31
    ERROR_WRITE_IMAGE = 16
    ERROR_WRITE_MEDIUM = 15
    WARNING_CHECKSUM = 29
    WARNING_INSERT_AFTER_COPY = 30
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.BraseroBurn', '__dict__': <attribute '__dict__' of 'BurnError' objects>, '__doc__': None, '__gtype__': <GType PyBraseroBurnBurnError (94320849267584)>, '__enum_values__': {0: <enum BRASERO_BURN_ERROR_NONE of type BraseroBurn.BurnError>, 1: <enum BRASERO_BURN_ERROR_GENERAL of type BraseroBurn.BurnError>, 2: <enum BRASERO_BURN_ERROR_PLUGIN_MISBEHAVIOR of type BraseroBurn.BurnError>, 3: <enum BRASERO_BURN_ERROR_SLOW_DMA of type BraseroBurn.BurnError>, 4: <enum BRASERO_BURN_ERROR_PERMISSION of type BraseroBurn.BurnError>, 5: <enum BRASERO_BURN_ERROR_DRIVE_BUSY of type BraseroBurn.BurnError>, 6: <enum BRASERO_BURN_ERROR_DISK_SPACE of type BraseroBurn.BurnError>, 7: <enum BRASERO_BURN_ERROR_EMPTY of type BraseroBurn.BurnError>, 8: <enum BRASERO_BURN_ERROR_INPUT_INVALID of type BraseroBurn.BurnError>, 9: <enum BRASERO_BURN_ERROR_OUTPUT_NONE of type BraseroBurn.BurnError>, 10: <enum BRASERO_BURN_ERROR_FILE_INVALID of type BraseroBurn.BurnError>, 11: <enum BRASERO_BURN_ERROR_FILE_FOLDER of type BraseroBurn.BurnError>, 12: <enum BRASERO_BURN_ERROR_FILE_PLAYLIST of type BraseroBurn.BurnError>, 13: <enum BRASERO_BURN_ERROR_FILE_NOT_FOUND of type BraseroBurn.BurnError>, 14: <enum BRASERO_BURN_ERROR_FILE_NOT_LOCAL of type BraseroBurn.BurnError>, 15: <enum BRASERO_BURN_ERROR_WRITE_MEDIUM of type BraseroBurn.BurnError>, 16: <enum BRASERO_BURN_ERROR_WRITE_IMAGE of type BraseroBurn.BurnError>, 17: <enum BRASERO_BURN_ERROR_IMAGE_INVALID of type BraseroBurn.BurnError>, 18: <enum BRASERO_BURN_ERROR_IMAGE_JOLIET of type BraseroBurn.BurnError>, 19: <enum BRASERO_BURN_ERROR_IMAGE_LAST_SESSION of type BraseroBurn.BurnError>, 20: <enum BRASERO_BURN_ERROR_MEDIUM_NONE of type BraseroBurn.BurnError>, 21: <enum BRASERO_BURN_ERROR_MEDIUM_INVALID of type BraseroBurn.BurnError>, 22: <enum BRASERO_BURN_ERROR_MEDIUM_SPACE of type BraseroBurn.BurnError>, 23: <enum BRASERO_BURN_ERROR_MEDIUM_NO_DATA of type BraseroBurn.BurnError>, 24: <enum BRASERO_BURN_ERROR_MEDIUM_NOT_WRITABLE of type BraseroBurn.BurnError>, 25: <enum BRASERO_BURN_ERROR_MEDIUM_NOT_REWRITABLE of type BraseroBurn.BurnError>, 26: <enum BRASERO_BURN_ERROR_MEDIUM_NEED_RELOADING of type BraseroBurn.BurnError>, 27: <enum BRASERO_BURN_ERROR_BAD_CHECKSUM of type BraseroBurn.BurnError>, 28: <enum BRASERO_BURN_ERROR_MISSING_APP_AND_PLUGIN of type BraseroBurn.BurnError>, 29: <enum BRASERO_BURN_WARNING_CHECKSUM of type BraseroBurn.BurnError>, 30: <enum BRASERO_BURN_WARNING_INSERT_AFTER_COPY of type BraseroBurn.BurnError>, 31: <enum BRASERO_BURN_ERROR_TMP_DIRECTORY of type BraseroBurn.BurnError>, 32: <enum BRASERO_BURN_ERROR_ENCRYPTION_KEY of type BraseroBurn.BurnError>}, '__info__': gi.EnumInfo(BurnError), 'ERROR_NONE': <enum BRASERO_BURN_ERROR_NONE of type BraseroBurn.BurnError>, 'ERROR_GENERAL': <enum BRASERO_BURN_ERROR_GENERAL of type BraseroBurn.BurnError>, 'ERROR_PLUGIN_MISBEHAVIOR': <enum BRASERO_BURN_ERROR_PLUGIN_MISBEHAVIOR of type BraseroBurn.BurnError>, 'ERROR_SLOW_DMA': <enum BRASERO_BURN_ERROR_SLOW_DMA of type BraseroBurn.BurnError>, 'ERROR_PERMISSION': <enum BRASERO_BURN_ERROR_PERMISSION of type BraseroBurn.BurnError>, 'ERROR_DRIVE_BUSY': <enum BRASERO_BURN_ERROR_DRIVE_BUSY of type BraseroBurn.BurnError>, 'ERROR_DISK_SPACE': <enum BRASERO_BURN_ERROR_DISK_SPACE of type BraseroBurn.BurnError>, 'ERROR_EMPTY': <enum BRASERO_BURN_ERROR_EMPTY of type BraseroBurn.BurnError>, 'ERROR_INPUT_INVALID': <enum BRASERO_BURN_ERROR_INPUT_INVALID of type BraseroBurn.BurnError>, 'ERROR_OUTPUT_NONE': <enum BRASERO_BURN_ERROR_OUTPUT_NONE of type BraseroBurn.BurnError>, 'ERROR_FILE_INVALID': <enum BRASERO_BURN_ERROR_FILE_INVALID of type BraseroBurn.BurnError>, 'ERROR_FILE_FOLDER': <enum BRASERO_BURN_ERROR_FILE_FOLDER of type BraseroBurn.BurnError>, 'ERROR_FILE_PLAYLIST': <enum BRASERO_BURN_ERROR_FILE_PLAYLIST of type BraseroBurn.BurnError>, 'ERROR_FILE_NOT_FOUND': <enum BRASERO_BURN_ERROR_FILE_NOT_FOUND of type BraseroBurn.BurnError>, 'ERROR_FILE_NOT_LOCAL': <enum BRASERO_BURN_ERROR_FILE_NOT_LOCAL of type BraseroBurn.BurnError>, 'ERROR_WRITE_MEDIUM': <enum BRASERO_BURN_ERROR_WRITE_MEDIUM of type BraseroBurn.BurnError>, 'ERROR_WRITE_IMAGE': <enum BRASERO_BURN_ERROR_WRITE_IMAGE of type BraseroBurn.BurnError>, 'ERROR_IMAGE_INVALID': <enum BRASERO_BURN_ERROR_IMAGE_INVALID of type BraseroBurn.BurnError>, 'ERROR_IMAGE_JOLIET': <enum BRASERO_BURN_ERROR_IMAGE_JOLIET of type BraseroBurn.BurnError>, 'ERROR_IMAGE_LAST_SESSION': <enum BRASERO_BURN_ERROR_IMAGE_LAST_SESSION of type BraseroBurn.BurnError>, 'ERROR_MEDIUM_NONE': <enum BRASERO_BURN_ERROR_MEDIUM_NONE of type BraseroBurn.BurnError>, 'ERROR_MEDIUM_INVALID': <enum BRASERO_BURN_ERROR_MEDIUM_INVALID of type BraseroBurn.BurnError>, 'ERROR_MEDIUM_SPACE': <enum BRASERO_BURN_ERROR_MEDIUM_SPACE of type BraseroBurn.BurnError>, 'ERROR_MEDIUM_NO_DATA': <enum BRASERO_BURN_ERROR_MEDIUM_NO_DATA of type BraseroBurn.BurnError>, 'ERROR_MEDIUM_NOT_WRITABLE': <enum BRASERO_BURN_ERROR_MEDIUM_NOT_WRITABLE of type BraseroBurn.BurnError>, 'ERROR_MEDIUM_NOT_REWRITABLE': <enum BRASERO_BURN_ERROR_MEDIUM_NOT_REWRITABLE of type BraseroBurn.BurnError>, 'ERROR_MEDIUM_NEED_RELOADING': <enum BRASERO_BURN_ERROR_MEDIUM_NEED_RELOADING of type BraseroBurn.BurnError>, 'ERROR_BAD_CHECKSUM': <enum BRASERO_BURN_ERROR_BAD_CHECKSUM of type BraseroBurn.BurnError>, 'ERROR_MISSING_APP_AND_PLUGIN': <enum BRASERO_BURN_ERROR_MISSING_APP_AND_PLUGIN of type BraseroBurn.BurnError>, 'WARNING_CHECKSUM': <enum BRASERO_BURN_WARNING_CHECKSUM of type BraseroBurn.BurnError>, 'WARNING_INSERT_AFTER_COPY': <enum BRASERO_BURN_WARNING_INSERT_AFTER_COPY of type BraseroBurn.BurnError>, 'ERROR_TMP_DIRECTORY': <enum BRASERO_BURN_ERROR_TMP_DIRECTORY of type BraseroBurn.BurnError>, 'ERROR_ENCRYPTION_KEY': <enum BRASERO_BURN_ERROR_ENCRYPTION_KEY of type BraseroBurn.BurnError>})"
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
        30: 30,
        31: 31,
        32: 32,
    }
    __gtype__ = None # (!) real value is '<GType PyBraseroBurnBurnError (94320849267584)>'
    __info__ = gi.EnumInfo(BurnError)


