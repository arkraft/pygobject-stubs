# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
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


class FeatureID(__gobject.GEnum):
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


    OGL_FEATURE_ID_ARBFP = 8
    OGL_FEATURE_ID_BUFFER_AGE = 25
    OGL_FEATURE_ID_DEPTH_RANGE = 13
    OGL_FEATURE_ID_DEPTH_TEXTURE = 20
    OGL_FEATURE_ID_FENCE = 22
    OGL_FEATURE_ID_GLES2_CONTEXT = 19
    OGL_FEATURE_ID_GLSL = 7
    OGL_FEATURE_ID_MAP_BUFFER_FOR_READ = 15
    OGL_FEATURE_ID_MAP_BUFFER_FOR_WRITE = 16
    OGL_FEATURE_ID_MIRRORED_REPEAT = 17
    OGL_FEATURE_ID_OFFSCREEN = 9
    OGL_FEATURE_ID_OFFSCREEN_MULTISAMPLE = 10
    OGL_FEATURE_ID_ONSCREEN_MULTIPLE = 11
    OGL_FEATURE_ID_PER_VERTEX_POINT_SIZE = 23
    OGL_FEATURE_ID_POINT_SPRITE = 14
    OGL_FEATURE_ID_PRESENTATION_TIME = 21
    OGL_FEATURE_ID_SHADER_TEXTURE_LOD = 26
    OGL_FEATURE_ID_SWAP_BUFFERS_EVENT = 18
    OGL_FEATURE_ID_TEXTURE_3D = 6
    OGL_FEATURE_ID_TEXTURE_NPOT = 4
    OGL_FEATURE_ID_TEXTURE_NPOT_BASIC = 1
    OGL_FEATURE_ID_TEXTURE_NPOT_MIPMAP = 2
    OGL_FEATURE_ID_TEXTURE_NPOT_REPEAT = 3
    OGL_FEATURE_ID_TEXTURE_RECTANGLE = 5
    OGL_FEATURE_ID_TEXTURE_RG = 24
    OGL_FEATURE_ID_UNSIGNED_INT_INDICES = 12
    __class__ = type
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'gi.repository.Cogl', '__dict__': <attribute '__dict__' of 'FeatureID' objects>, '__doc__': None, '__gtype__': <GType PyCoglFeatureID (93970932098864)>, '__enum_values__': {1: <enum COGL_FEATURE_ID_TEXTURE_NPOT_BASIC of type Cogl.FeatureID>, 2: <enum COGL_FEATURE_ID_TEXTURE_NPOT_MIPMAP of type Cogl.FeatureID>, 3: <enum COGL_FEATURE_ID_TEXTURE_NPOT_REPEAT of type Cogl.FeatureID>, 4: <enum COGL_FEATURE_ID_TEXTURE_NPOT of type Cogl.FeatureID>, 5: <enum COGL_FEATURE_ID_TEXTURE_RECTANGLE of type Cogl.FeatureID>, 6: <enum COGL_FEATURE_ID_TEXTURE_3D of type Cogl.FeatureID>, 7: <enum COGL_FEATURE_ID_GLSL of type Cogl.FeatureID>, 8: <enum COGL_FEATURE_ID_ARBFP of type Cogl.FeatureID>, 9: <enum COGL_FEATURE_ID_OFFSCREEN of type Cogl.FeatureID>, 10: <enum COGL_FEATURE_ID_OFFSCREEN_MULTISAMPLE of type Cogl.FeatureID>, 11: <enum COGL_FEATURE_ID_ONSCREEN_MULTIPLE of type Cogl.FeatureID>, 12: <enum COGL_FEATURE_ID_UNSIGNED_INT_INDICES of type Cogl.FeatureID>, 13: <enum COGL_FEATURE_ID_DEPTH_RANGE of type Cogl.FeatureID>, 14: <enum COGL_FEATURE_ID_POINT_SPRITE of type Cogl.FeatureID>, 15: <enum COGL_FEATURE_ID_MAP_BUFFER_FOR_READ of type Cogl.FeatureID>, 16: <enum COGL_FEATURE_ID_MAP_BUFFER_FOR_WRITE of type Cogl.FeatureID>, 17: <enum COGL_FEATURE_ID_MIRRORED_REPEAT of type Cogl.FeatureID>, 18: <enum COGL_FEATURE_ID_SWAP_BUFFERS_EVENT of type Cogl.FeatureID>, 19: <enum COGL_FEATURE_ID_GLES2_CONTEXT of type Cogl.FeatureID>, 20: <enum COGL_FEATURE_ID_DEPTH_TEXTURE of type Cogl.FeatureID>, 21: <enum COGL_FEATURE_ID_PRESENTATION_TIME of type Cogl.FeatureID>, 22: <enum COGL_FEATURE_ID_FENCE of type Cogl.FeatureID>, 23: <enum COGL_FEATURE_ID_PER_VERTEX_POINT_SIZE of type Cogl.FeatureID>, 24: <enum COGL_FEATURE_ID_TEXTURE_RG of type Cogl.FeatureID>, 25: <enum COGL_FEATURE_ID_BUFFER_AGE of type Cogl.FeatureID>, 26: <enum COGL_FEATURE_ID_SHADER_TEXTURE_LOD of type Cogl.FeatureID>}, '__info__': gi.EnumInfo(FeatureID), 'OGL_FEATURE_ID_TEXTURE_NPOT_BASIC': <enum COGL_FEATURE_ID_TEXTURE_NPOT_BASIC of type Cogl.FeatureID>, 'OGL_FEATURE_ID_TEXTURE_NPOT_MIPMAP': <enum COGL_FEATURE_ID_TEXTURE_NPOT_MIPMAP of type Cogl.FeatureID>, 'OGL_FEATURE_ID_TEXTURE_NPOT_REPEAT': <enum COGL_FEATURE_ID_TEXTURE_NPOT_REPEAT of type Cogl.FeatureID>, 'OGL_FEATURE_ID_TEXTURE_NPOT': <enum COGL_FEATURE_ID_TEXTURE_NPOT of type Cogl.FeatureID>, 'OGL_FEATURE_ID_TEXTURE_RECTANGLE': <enum COGL_FEATURE_ID_TEXTURE_RECTANGLE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_TEXTURE_3D': <enum COGL_FEATURE_ID_TEXTURE_3D of type Cogl.FeatureID>, 'OGL_FEATURE_ID_GLSL': <enum COGL_FEATURE_ID_GLSL of type Cogl.FeatureID>, 'OGL_FEATURE_ID_ARBFP': <enum COGL_FEATURE_ID_ARBFP of type Cogl.FeatureID>, 'OGL_FEATURE_ID_OFFSCREEN': <enum COGL_FEATURE_ID_OFFSCREEN of type Cogl.FeatureID>, 'OGL_FEATURE_ID_OFFSCREEN_MULTISAMPLE': <enum COGL_FEATURE_ID_OFFSCREEN_MULTISAMPLE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_ONSCREEN_MULTIPLE': <enum COGL_FEATURE_ID_ONSCREEN_MULTIPLE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_UNSIGNED_INT_INDICES': <enum COGL_FEATURE_ID_UNSIGNED_INT_INDICES of type Cogl.FeatureID>, 'OGL_FEATURE_ID_DEPTH_RANGE': <enum COGL_FEATURE_ID_DEPTH_RANGE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_POINT_SPRITE': <enum COGL_FEATURE_ID_POINT_SPRITE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_MAP_BUFFER_FOR_READ': <enum COGL_FEATURE_ID_MAP_BUFFER_FOR_READ of type Cogl.FeatureID>, 'OGL_FEATURE_ID_MAP_BUFFER_FOR_WRITE': <enum COGL_FEATURE_ID_MAP_BUFFER_FOR_WRITE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_MIRRORED_REPEAT': <enum COGL_FEATURE_ID_MIRRORED_REPEAT of type Cogl.FeatureID>, 'OGL_FEATURE_ID_SWAP_BUFFERS_EVENT': <enum COGL_FEATURE_ID_SWAP_BUFFERS_EVENT of type Cogl.FeatureID>, 'OGL_FEATURE_ID_GLES2_CONTEXT': <enum COGL_FEATURE_ID_GLES2_CONTEXT of type Cogl.FeatureID>, 'OGL_FEATURE_ID_DEPTH_TEXTURE': <enum COGL_FEATURE_ID_DEPTH_TEXTURE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_PRESENTATION_TIME': <enum COGL_FEATURE_ID_PRESENTATION_TIME of type Cogl.FeatureID>, 'OGL_FEATURE_ID_FENCE': <enum COGL_FEATURE_ID_FENCE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_PER_VERTEX_POINT_SIZE': <enum COGL_FEATURE_ID_PER_VERTEX_POINT_SIZE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_TEXTURE_RG': <enum COGL_FEATURE_ID_TEXTURE_RG of type Cogl.FeatureID>, 'OGL_FEATURE_ID_BUFFER_AGE': <enum COGL_FEATURE_ID_BUFFER_AGE of type Cogl.FeatureID>, 'OGL_FEATURE_ID_SHADER_TEXTURE_LOD': <enum COGL_FEATURE_ID_SHADER_TEXTURE_LOD of type Cogl.FeatureID>})"
    __enum_values__ = {
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
    }
    __gtype__ = None # (!) real value is '<GType PyCoglFeatureID (93970932098864)>'
    __info__ = gi.EnumInfo(FeatureID)


