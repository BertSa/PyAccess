import os

import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')
import pyperclip as pc
from gi.repository import Gtk, Notify

APPINDICATOR_ID = 'ca.bertsa.pyaccess'
PATH_GH_TOKEN = 'privates/token_gh.bertsa'


def copy_to_clip(_):
    with open(PATH_GH_TOKEN) as file:
        token = file.read()
        pc.set_clipboard('xclip')
        pc.copy(token)


def quit():
    Notify.uninit()
    Gtk.main_quit()


def setKeyboardLayout(layout):
    os.system("sudo /opt/scripts/keyboardfn.sh " + str(layout))


def usb_access(_):
    tag = 'Usb Access'
    code_returned = os.system("sudo /opt/scripts/usbAccess.sh")
    if code_returned == 256:
        notify_me(tag, 'Device not connected!')
    elif code_returned == 0:
        notify_me(tag, 'Done!')
    else:
        notify_me(tag, 'Oops! Something went wrong!')


def notify_me(title, message):
    Notify.init(APPINDICATOR_ID)
    Notify.Notification.new(title, message, os.path.abspath('icon.png')).show()
