from enum import Enum

import gi

from PyAccessUtils import setKeyboardLayout, copy_to_clip, notify_me, usb_access
from WindowAccess import open_window

gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk
from gi.repository.AppIndicator3 import Indicator, IndicatorCategory, IndicatorStatus

APP_INDICATOR_ID = 'ca.bertsa.pyaccess'


class _ItemType(Enum):
    Normal = 0
    Check = 1


def _create_menu_item(item_type: _ItemType, label: str, callback: callable, **kwargs):
    if item_type == _ItemType.Normal:
        item = Gtk.MenuItem()
    elif item_type == _ItemType.Check:
        item = Gtk.CheckMenuItem()
        if kwargs.get('active', False):
            item.activate()
    # noinspection PyUnboundLocalVariable
    item.set_label(label)
    item.connect('activate', callback)
    return item


def _createMoreMenu(*args):
    """
    :type args: callable
    """
    sub_menu = Gtk.Menu()
    for item in args:
        sub_menu.append(item)
    item_sub_menu = Gtk.MenuItem()
    item_sub_menu.set_label("More")
    item_sub_menu.set_submenu(sub_menu)
    return item_sub_menu


class PyAccessIndicator:
    # noinspection PyArgumentList
    def __init__(self):
        self.menu = Gtk.Menu()

        self.item_copy_key = _create_menu_item(_ItemType.Normal, "Copy Key", copy_to_clip)
        self.item_usb_access = _create_menu_item(_ItemType.Normal, "Usb Access", usb_access)
        self.item_keyboard = _create_menu_item(_ItemType.Check, "Change keyboard layout", self.keyboardfn, active=True)
        self.item_open = _create_menu_item(_ItemType.Normal, "Open", open_window)
        self.item_quit = _create_menu_item(_ItemType.Normal, "Quit", quit)

        self.item_sub_menu = _createMoreMenu(self.item_open, self.item_quit)

        self.menu.append(self.item_keyboard)
        self.menu.append(self.item_usb_access)
        self.menu.append(self.item_copy_key)
        self.menu.append(Gtk.SeparatorMenuItem())
        self.menu.append(self.item_sub_menu)
        self.menu.show_all()

        self.indicator = Indicator.new(APP_INDICATOR_ID, 'go-down-symbolic',
                                       IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.menu)

        Gtk.main()

    def keyboardfn(self, _):
        tag = 'Keyboard'
        try:
            if self.item_keyboard.get_active():
                setKeyboardLayout(0)
            else:
                setKeyboardLayout(1)
        except OSError:
            notify_me(tag, "Oops! Something went wrong!")
