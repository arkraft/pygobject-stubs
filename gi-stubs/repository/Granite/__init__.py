# encoding: utf-8
# module gi.repository.Granite
# from /usr/lib/x86_64-linux-gnu/girepository-1.0/Granite-1.0.typelib
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


# Variables with simple values

BADGE = 'badge'

CATEGORY_EXPANDER = 'category-expander'

COMPOSITED = 'composited'

CONTENT_VIEW = 'content-view'

CONTENT_VIEW_WINDOW = 'content-view-window'

DECORATED_WINDOW = 'decorated-window'

H1_TEXT = 'h1'

H2_TEXT = 'h2'

H3_TEXT = 'h3'

HELP_BUTTON = 'help_button'

OVERLAY_BAR = 'overlay-bar'

POPOVER = 'popover'

POPOVER_BG = 'popover_bg'

SOURCE_LIST = 'source-list'

STYLE_CLASS_ACCENT = 'accent'
STYLE_CLASS_AVATAR = 'avatar'

STYLE_CLASS_BACK_BUTTON = 'back-button'

STYLE_CLASS_BADGE = 'badge'
STYLE_CLASS_CARD = 'card'

STYLE_CLASS_CATEGORY_EXPANDER = 'category-expander'

STYLE_CLASS_CHECKERBOARD = 'checkerboard'

STYLE_CLASS_COLOR_BUTTON = 'color-button'

STYLE_CLASS_H1_LABEL = 'h1'

STYLE_CLASS_H2_LABEL = 'h2'

STYLE_CLASS_H3_LABEL = 'h3'

STYLE_CLASS_H4_LABEL = 'h4'

STYLE_CLASS_KEYCAP = 'keycap'

STYLE_CLASS_MODE_SWITCH = 'mode-switch'

STYLE_CLASS_OVERLAY_BAR = 'overlay-bar'

STYLE_CLASS_PRIMARY_LABEL = 'primary'

STYLE_CLASS_ROUNDED = 'rounded'
STYLE_CLASS_SEEKBAR = 'seek-bar'

STYLE_CLASS_SOURCE_LIST = 'source-list'

STYLE_CLASS_STORAGEBAR = 'storage-bar'
STYLE_CLASS_TERMINAL = 'terminal'
STYLE_CLASS_WELCOME = 'welcome'

THIN_PANE_SEPARATOR = 'sidebar-pane-separator'

TITLE_TEXT = 'title'

_namespace = 'Granite'

_version = '1.0'

__weakref__ = None

# functions

def accel_to_string(accel=None): # real signature unknown; restored from __doc__
    """ accel_to_string(accel:str=None) -> str """
    return ""

def contrasting_foreground_color(bg_color): # real signature unknown; restored from __doc__
    """ contrasting_foreground_color(bg_color:Gdk.RGBA) -> result:Gdk.RGBA """
    pass

def date_time_get_default_date_format(with_weekday, with_day, with_year): # real signature unknown; restored from __doc__
    """ date_time_get_default_date_format(with_weekday:bool, with_day:bool, with_year:bool) -> str """
    return ""

def date_time_get_default_time_format(is_12h, with_second): # real signature unknown; restored from __doc__
    """ date_time_get_default_time_format(is_12h:bool, with_second:bool) -> str """
    return ""

def date_time_get_relative_datetime(date_time): # real signature unknown; restored from __doc__
    """ date_time_get_relative_datetime(date_time:GLib.DateTime) -> str """
    return ""

def date_time_is_same_day(day1, day2): # real signature unknown; restored from __doc__
    """ date_time_is_same_day(day1:GLib.DateTime, day2:GLib.DateTime) -> bool """
    return False

def date_time_seconds_to_time(seconds): # real signature unknown; restored from __doc__
    """ date_time_seconds_to_time(seconds:int) -> str """
    return ""

def markup_accel_tooltip(accels=None, description=None): # real signature unknown; restored from __doc__
    """ markup_accel_tooltip(accels:list=None, description:str=None) -> str """
    return ""

def services_application_set_badge(count, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
    """ services_application_set_badge(count:int, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
    pass

def services_application_set_badge_finish(_res_): # real signature unknown; restored from __doc__
    """ services_application_set_badge_finish(_res_:Gio.AsyncResult) -> bool """
    return False

def services_application_set_badge_visible(visible, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
    """ services_application_set_badge_visible(visible:bool, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
    pass

def services_application_set_badge_visible_finish(_res_): # real signature unknown; restored from __doc__
    """ services_application_set_badge_visible_finish(_res_:Gio.AsyncResult) -> bool """
    return False

def services_application_set_progress(progress, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
    """ services_application_set_progress(progress:float, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
    pass

def services_application_set_progress_finish(_res_): # real signature unknown; restored from __doc__
    """ services_application_set_progress_finish(_res_:Gio.AsyncResult) -> bool """
    return False

def services_application_set_progress_visible(visible, _callback_=None, _callback__target=None): # real signature unknown; restored from __doc__
    """ services_application_set_progress_visible(visible:bool, _callback_:Gio.AsyncReadyCallback=None, _callback__target=None) """
    pass

def services_application_set_progress_visible_finish(_res_): # real signature unknown; restored from __doc__
    """ services_application_set_progress_visible_finish(_res_:Gio.AsyncResult) -> bool """
    return False

def text_style_get_stylesheet(): # real signature unknown; restored from __doc__
    """ text_style_get_stylesheet() -> str, style_class:str """
    return ""

def widgets_storage_bar_item_description_get_class(description): # real signature unknown; restored from __doc__
    """ widgets_storage_bar_item_description_get_class(description:Granite.WidgetsStorageBarItemDescription) -> str """
    return ""

def widgets_storage_bar_item_description_get_name(description): # real signature unknown; restored from __doc__
    """ widgets_storage_bar_item_description_get_name(description:Granite.WidgetsStorageBarItemDescription) -> str """
    return ""

def widgets_utils_apply_text_style_to_label(text_style, label): # real signature unknown; restored from __doc__
    """ widgets_utils_apply_text_style_to_label(text_style:Granite.TextStyle, label:Gtk.Label) """
    pass

def widgets_utils_get_button_layout_schema(): # real signature unknown; restored from __doc__
    """ widgets_utils_get_button_layout_schema() -> str """
    return ""

def widgets_utils_get_css_provider(stylesheet): # real signature unknown; restored from __doc__
    """ widgets_utils_get_css_provider(stylesheet:str) -> Gtk.CssProvider """
    pass

def widgets_utils_get_default_close_button_position(): # real signature unknown; restored from __doc__
    """ widgets_utils_get_default_close_button_position() -> bool, position:Granite.CloseButtonPosition """
    return False

def widgets_utils_set_color_primary(window, color, priority): # real signature unknown; restored from __doc__
    """ widgets_utils_set_color_primary(window:Gtk.Widget, color:Gdk.RGBA, priority:int) -> Gtk.CssProvider """
    pass

def widgets_utils_set_theming(widget, stylesheet, class_name=None, priority): # real signature unknown; restored from __doc__
    """ widgets_utils_set_theming(widget:Gtk.Widget, stylesheet:str, class_name:str=None, priority:int) -> Gtk.CssProvider """
    pass

def widgets_utils_set_theming_for_screen(screen, stylesheet, priority): # real signature unknown; restored from __doc__
    """ widgets_utils_set_theming_for_screen(screen:Gdk.Screen, stylesheet:str, priority:int) -> Gtk.CssProvider """
    pass

def __delattr__(*args, **kwargs): # real signature unknown
    """ Implement delattr(self, name). """
    pass

def __dir__(*args, **kwargs): # real signature unknown
    pass

def __eq__(*args, **kwargs): # real signature unknown
    """ Return self==value. """
    pass

def __format__(*args, **kwargs): # real signature unknown
    """ default object formatter """
    pass

def __getattribute__(*args, **kwargs): # real signature unknown
    """ Return getattr(self, name). """
    pass

def __getattr__(*args, **kwargs): # real signature unknown
    pass

def __ge__(*args, **kwargs): # real signature unknown
    """ Return self>=value. """
    pass

def __gt__(*args, **kwargs): # real signature unknown
    """ Return self>value. """
    pass

def __hash__(*args, **kwargs): # real signature unknown
    """ Return hash(self). """
    pass

def __init_subclass__(*args, **kwargs): # real signature unknown
    """
    This method is called when a class is subclassed.
    
    The default implementation does nothing. It may be
    overridden to extend subclasses.
    """
    pass

def __init__(*args, **kwargs): # real signature unknown
    """ Might raise gi._gi.RepositoryError """
    pass

def __le__(*args, **kwargs): # real signature unknown
    """ Return self<=value. """
    pass

def __lt__(*args, **kwargs): # real signature unknown
    """ Return self<value. """
    pass

@staticmethod # known case of __new__
def __new__(*args, **kwargs): # real signature unknown
    """ Create and return a new object.  See help(type) for accurate signature. """
    pass

def __ne__(*args, **kwargs): # real signature unknown
    """ Return self!=value. """
    pass

def __reduce_ex__(*args, **kwargs): # real signature unknown
    """ helper for pickle """
    pass

def __reduce__(*args, **kwargs): # real signature unknown
    """ helper for pickle """
    pass

def __repr__(*args, **kwargs): # real signature unknown
    pass

def __setattr__(*args, **kwargs): # real signature unknown
    """ Implement setattr(self, name, value). """
    pass

def __sizeof__(): # real signature unknown; restored from __doc__
    """
    __sizeof__() -> int
    size of object in memory, in bytes
    """
    return 0

def __str__(*args, **kwargs): # real signature unknown
    """ Return str(self). """
    pass

def __subclasshook__(*args, **kwargs): # real signature unknown
    """
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).
    """
    pass

# classes

from .AccelLabel import AccelLabel
from .AccelLabelClass import AccelLabelClass
from .AccelLabelPrivate import AccelLabelPrivate
from .Application import Application
from .ApplicationClass import ApplicationClass
from .ApplicationPrivate import ApplicationPrivate
from .AsyncImage import AsyncImage
from .AsyncImageClass import AsyncImageClass
from .AsyncImagePrivate import AsyncImagePrivate
from .CloseButtonPosition import CloseButtonPosition
from .CollapseMode import CollapseMode
from .ContractorError import ContractorError
from .DrawingBufferSurface import DrawingBufferSurface
from .DrawingBufferSurfaceClass import DrawingBufferSurfaceClass
from .DrawingBufferSurfacePrivate import DrawingBufferSurfacePrivate
from .DrawingColorClass import DrawingColorClass
from .DrawingColorPrivate import DrawingColorPrivate
from .DrawingUtilities import DrawingUtilities
from .DrawingUtilitiesClass import DrawingUtilitiesClass
from .DrawingUtilitiesPrivate import DrawingUtilitiesPrivate
from .GtkPatchAboutDialog import GtkPatchAboutDialog
from .GtkPatchAboutDialogClass import GtkPatchAboutDialogClass
from .GtkPatchAboutDialogPrivate import GtkPatchAboutDialogPrivate
from .HeaderLabel import HeaderLabel
from .HeaderLabelClass import HeaderLabelClass
from .HeaderLabelPrivate import HeaderLabelPrivate
from .MessageDialog import MessageDialog
from .MessageDialogClass import MessageDialogClass
from .MessageDialogPrivate import MessageDialogPrivate
from .ModeSwitch import ModeSwitch
from .ModeSwitchClass import ModeSwitchClass
from .ModeSwitchPrivate import ModeSwitchPrivate
from .SeekBar import SeekBar
from .SeekBarClass import SeekBarClass
from .SeekBarPrivate import SeekBarPrivate
from .ServicesContract import ServicesContract
from .ServicesContractIface import ServicesContractIface
from .ServicesContractorProxy import ServicesContractorProxy
from .ServicesContractorProxyClass import ServicesContractorProxyClass
from .ServicesContractorProxyPrivate import ServicesContractorProxyPrivate
from .ServicesIconFactory import ServicesIconFactory
from .ServicesIconFactoryClass import ServicesIconFactoryClass
from .ServicesIconFactoryPrivate import ServicesIconFactoryPrivate
from .ServicesLogger import ServicesLogger
from .ServicesLoggerClass import ServicesLoggerClass
from .ServicesLoggerPrivate import ServicesLoggerPrivate
from .ServicesLogLevel import ServicesLogLevel
from .ServicesPaths import ServicesPaths
from .ServicesPathsClass import ServicesPathsClass
from .ServicesPathsPrivate import ServicesPathsPrivate
from .ServicesSettings import ServicesSettings
from .ServicesSettingsClass import ServicesSettingsClass
from .ServicesSettingsPrivate import ServicesSettingsPrivate
from .ServicesSettingsSerializable import ServicesSettingsSerializable
from .ServicesSettingsSerializableIface import ServicesSettingsSerializableIface
from .ServicesSimpleCommand import ServicesSimpleCommand
from .ServicesSimpleCommandClass import ServicesSimpleCommandClass
from .ServicesSimpleCommandPrivate import ServicesSimpleCommandPrivate
from .ServicesSystem import ServicesSystem
from .ServicesSystemClass import ServicesSystemClass
from .ServicesSystemPrivate import ServicesSystemPrivate
from .Settings import Settings
from .SettingsClass import SettingsClass
from .SettingsColorScheme import SettingsColorScheme
from .SettingsPage import SettingsPage
from .SettingsPageClass import SettingsPageClass
from .SettingsPagePrivate import SettingsPagePrivate
from .SettingsPageStatusType import SettingsPageStatusType
from .SettingsPrivate import SettingsPrivate
from .SettingsSidebar import SettingsSidebar
from .SettingsSidebarClass import SettingsSidebarClass
from .SettingsSidebarPrivate import SettingsSidebarPrivate
from .SimpleSettingsPage import SimpleSettingsPage
from .SimpleSettingsPageClass import SimpleSettingsPageClass
from .SimpleSettingsPagePrivate import SimpleSettingsPagePrivate
from .TextStyle import TextStyle
from .WidgetsAboutDialog import WidgetsAboutDialog
from .WidgetsAboutDialogClass import WidgetsAboutDialogClass
from .WidgetsAboutDialogPrivate import WidgetsAboutDialogPrivate
from .WidgetsAlertView import WidgetsAlertView
from .WidgetsAlertViewClass import WidgetsAlertViewClass
from .WidgetsAlertViewPrivate import WidgetsAlertViewPrivate
from .WidgetsAppMenu import WidgetsAppMenu
from .WidgetsAppMenuClass import WidgetsAppMenuClass
from .WidgetsAppMenuPrivate import WidgetsAppMenuPrivate
from .WidgetsAvatar import WidgetsAvatar
from .WidgetsAvatarClass import WidgetsAvatarClass
from .WidgetsAvatarPrivate import WidgetsAvatarPrivate
from .WidgetsCellRendererBadge import WidgetsCellRendererBadge
from .WidgetsCellRendererBadgeClass import WidgetsCellRendererBadgeClass
from .WidgetsCellRendererBadgePrivate import WidgetsCellRendererBadgePrivate
from .WidgetsCellRendererExpander import WidgetsCellRendererExpander
from .WidgetsCellRendererExpanderClass import WidgetsCellRendererExpanderClass
from .WidgetsCellRendererExpanderPrivate import WidgetsCellRendererExpanderPrivate
from .WidgetsCollapsiblePaned import WidgetsCollapsiblePaned
from .WidgetsCollapsiblePanedClass import WidgetsCollapsiblePanedClass
from .WidgetsCollapsiblePanedPrivate import WidgetsCollapsiblePanedPrivate
from .WidgetsCompositedWindow import WidgetsCompositedWindow
from .WidgetsCompositedWindowClass import WidgetsCompositedWindowClass
from .WidgetsCompositedWindowPrivate import WidgetsCompositedWindowPrivate
from .WidgetsDatePicker import WidgetsDatePicker
from .WidgetsDatePickerClass import WidgetsDatePickerClass
from .WidgetsDatePickerPrivate import WidgetsDatePickerPrivate
from .WidgetsDynamicNotebook import WidgetsDynamicNotebook
from .WidgetsDynamicNotebookClass import WidgetsDynamicNotebookClass
from .WidgetsDynamicNotebookPrivate import WidgetsDynamicNotebookPrivate
from .WidgetsDynamicNotebookTabBarBehavior import WidgetsDynamicNotebookTabBarBehavior
from .WidgetsModeButton import WidgetsModeButton
from .WidgetsModeButtonClass import WidgetsModeButtonClass
from .WidgetsModeButtonPrivate import WidgetsModeButtonPrivate
from .WidgetsOverlayBar import WidgetsOverlayBar
from .WidgetsOverlayBarClass import WidgetsOverlayBarClass
from .WidgetsOverlayBarPrivate import WidgetsOverlayBarPrivate
from .WidgetsSourceList import WidgetsSourceList
from .WidgetsSourceListClass import WidgetsSourceListClass
from .WidgetsSourceListDragDest import WidgetsSourceListDragDest
from .WidgetsSourceListDragDestIface import WidgetsSourceListDragDestIface
from .WidgetsSourceListDragSource import WidgetsSourceListDragSource
from .WidgetsSourceListDragSourceIface import WidgetsSourceListDragSourceIface
from .WidgetsSourceListItem import WidgetsSourceListItem
from .WidgetsSourceListExpandableItem import WidgetsSourceListExpandableItem
from .WidgetsSourceListExpandableItemClass import WidgetsSourceListExpandableItemClass
from .WidgetsSourceListExpandableItemPrivate import WidgetsSourceListExpandableItemPrivate
from .WidgetsSourceListItemClass import WidgetsSourceListItemClass
from .WidgetsSourceListItemPrivate import WidgetsSourceListItemPrivate
from .WidgetsSourceListPrivate import WidgetsSourceListPrivate
from .WidgetsSourceListSortable import WidgetsSourceListSortable
from .WidgetsSourceListSortableIface import WidgetsSourceListSortableIface
from .WidgetsStorageBar import WidgetsStorageBar
from .WidgetsStorageBarClass import WidgetsStorageBarClass
from .WidgetsStorageBarItemDescription import WidgetsStorageBarItemDescription
from .WidgetsStorageBarPrivate import WidgetsStorageBarPrivate
from .WidgetsTab import WidgetsTab
from .WidgetsTabClass import WidgetsTabClass
from .WidgetsTabPrivate import WidgetsTabPrivate
from .WidgetsTimePicker import WidgetsTimePicker
from .WidgetsTimePickerClass import WidgetsTimePickerClass
from .WidgetsTimePickerPrivate import WidgetsTimePickerPrivate
from .WidgetsToast import WidgetsToast
from .WidgetsToastClass import WidgetsToastClass
from .WidgetsToastPrivate import WidgetsToastPrivate
from .WidgetsWelcome import WidgetsWelcome
from .WidgetsWelcomeButton import WidgetsWelcomeButton
from .WidgetsWelcomeButtonClass import WidgetsWelcomeButtonClass
from .WidgetsWelcomeButtonPrivate import WidgetsWelcomeButtonPrivate
from .WidgetsWelcomeClass import WidgetsWelcomeClass
from .WidgetsWelcomePrivate import WidgetsWelcomePrivate
from .__class__ import __class__
# variables with complex values

__loader__ = None # (!) real value is '<gi.importer.DynamicImporter object at 0x7f833a3744e0>'

__path__ = [
    '/usr/lib/x86_64-linux-gnu/girepository-1.0/Granite-1.0.typelib',
]

__spec__ = None # (!) real value is "ModuleSpec(name='gi.repository.Granite', loader=<gi.importer.DynamicImporter object at 0x7f833a3744e0>)"

