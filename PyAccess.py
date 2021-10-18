from gi.repository import Gtk
from gi.repository.AppIndicator3 import Indicator, IndicatorCategory, IndicatorStatus

from GtkCustom import _create_menu_item, _create_menu_item_check, _createMoreMenu
from PyAccessUtils import setKeyboardLayout, copy_to_clip, notify_me, usb_access

APP_INDICATOR_ID = 'ca.bertsa.pyaccess'


class PyAccess:

    def __init__(self):
        self.item_keyboard = None
        self.menu = Gtk.Menu()

        self.item_copy_key = _create_menu_item("Copy Key", copy_to_clip)
        self.item_usb_access = _create_menu_item("Usb Access", usb_access)
        self.item_keyboard = _create_menu_item_check("Change keyboard layout", self.keyboardfn, active=True)
        self.item_quit = _create_menu_item("Quit", quit)

        self.item_sub_menu = _createMoreMenu(self.item_quit)

        self.menu.append(self.item_keyboard)
        self.menu.append(self.item_usb_access)
        self.menu.append(self.item_copy_key)
        self.menu.append(Gtk.SeparatorMenuItem())
        self.menu.append(self.item_sub_menu)
        self.menu.show_all()
        # noinspection PyArgumentList
        self.indicator: Indicator = Indicator.new(id=APP_INDICATOR_ID, icon_name='go-down-symbolic',
                                                  category=IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.menu)
        Gtk.main()

    def keyboardfn(self, _):
        if self.item_keyboard is None:
            return
        tag = 'Keyboard'
        try:
            if self.item_keyboard.get_active():
                setKeyboardLayout(0)
            else:
                setKeyboardLayout(1)
        except OSError:
            notify_me(tag, "Oops! Something went wrong!")
