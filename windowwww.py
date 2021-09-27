import gi

gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import AppIndicator3, Gtk, Notify as notify
import os
import pyperclip as pc

APPINDICATOR_ID = 'PyAccess'


def copy_to_clip():
    with open('privates/token_gh.bertsa') as file:
        token = file.read()
        pc.set_clipboard('xclip')
        pc.copy(token)


def quit():
    notify.uninit()
    Gtk.main_quit()


def setKeyboardLayout(layout):
    os.system("sudo /opt/scripts/keyboardfn.sh " + str(layout))


class PyAccessIndicator:
    def __init__(self):
        self.menu = Gtk.Menu()

        self.item_quit = Gtk.MenuItem()
        self.item_quit.set_label("Quit")
        self.item_quit.connect('activate', quit)

        self.item_copy_key = Gtk.MenuItem()
        self.item_copy_key.set_label("Copy key")
        self.item_copy_key.connect('activate', copy_to_clip)

        self.item_keyboard = Gtk.CheckMenuItem()
        self.item_keyboard.set_label("Change keyboard layout")
        self.item_keyboard.connect('activate', self.keyboardfn)
        self.item_keyboard.activate()

        self.item_separator = Gtk.SeparatorMenuItem()

        self.menu.insert(self.item_copy_key, 0)
        self.menu.insert(self.item_keyboard, 1)
        self.menu.insert(self.item_separator, 2)
        self.menu.insert(self.item_quit, 3)
        self.menu.show_all()

        self.indicator = AppIndicator3.Indicator.new(APPINDICATOR_ID, 'go-down-symbolic',
                                                     AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.menu)

        Gtk.main()

    # def get_current():
    #     return os.popen("cat /sys/module/hid_apple/parameters/fnmode").read()
    #

    def keyboardfn(self, _):
        tag = 'Keyboard'
        if self.item_keyboard.get_active():
            setKeyboardLayout(0)
        else:
            setKeyboardLayout(1)
        self.notify_me(tag, "Keyboard layout as been successfuly updated")

    def usb_access(self, _):
        tag = 'Usb Access'
        code_returned = os.system("sudo /opt/scripts/usbAccess.sh")
        if code_returned == 256:
            self.notify_me(tag, 'Device not connected!')
        elif code_returned == 0:
            self.notify_me(tag, 'Done!')
        else:
            self.notify_me(tag, 'Oops! Something went wrong!')

    @staticmethod
    def notify_me(title, message):
        notify.init(APPINDICATOR_ID)
        notify.Notification.new(title, message, os.path.abspath('icon.png')).show()


if __name__ == "__main__":
    PyAccessIndicator()
