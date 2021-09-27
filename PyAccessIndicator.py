import gi

from PyAccessUtils import setKeyboardLayout, copy_to_clip, notify_me, usb_access
from WindowAccess import open_window

gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import AppIndicator3, Gtk

APPINDICATOR_ID = 'ca.bertsa.pyaccess'


class PyAccessIndicator:
    # noinspection PyArgumentList
    def __init__(self):
        self.menu = Gtk.Menu()

        self.item_quit = Gtk.MenuItem()
        self.item_quit.set_label("Quit")
        self.item_quit.connect('activate', quit)

        self.item_copy_key = Gtk.MenuItem()
        self.item_copy_key.set_label("Copy key")
        self.item_copy_key.connect('activate', copy_to_clip)

        self.item_usb_access = Gtk.MenuItem()
        self.item_usb_access.set_label("Usb Access")
        self.item_usb_access.connect('activate', usb_access)

        self.item_keyboard = Gtk.CheckMenuItem()
        self.item_keyboard.set_label("Change keyboard layout")
        self.item_keyboard.connect('activate', self.keyboardfn)
        self.item_keyboard.activate()

        self.item_open = Gtk.MenuItem()
        self.item_open.set_label("Open")
        self.item_open.connect('activate', open_window)

        self.sub_menu = Gtk.Menu()
        self.sub_menu.append(self.item_open)
        self.sub_menu.append(self.item_quit)

        self.item_sub_menu = Gtk.MenuItem()
        self.item_sub_menu.set_label("More")
        self.item_sub_menu.set_submenu(self.sub_menu)

        self.menu.append(self.item_keyboard)
        self.menu.append(self.item_usb_access)
        self.menu.append(self.item_copy_key)
        self.menu.append(Gtk.SeparatorMenuItem())
        self.menu.append(self.item_sub_menu)
        self.menu.show_all()

        self.indicator = AppIndicator3.Indicator.new(APPINDICATOR_ID, 'go-down-symbolic',
                                                     AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.menu)
        # self.indicator.set_menu(self.menu)

        Gtk.main()

    # def get_current():
    #     return os.popen("cat /sys/module/hid_apple/parameters/fnmode").read()
    #

    def keyboardfn(self, _):
        tag = 'Keyboard'
        try:
            if self.item_keyboard.get_active():
                setKeyboardLayout(0)
            else:
                setKeyboardLayout(1)
        except OSError:
            notify_me(tag, "Oops! Something went wrong!")


if __name__ == "__main__":
    PyAccessIndicator()
