import gi

gi.require_version('AppIndicator3', '0.1')
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from PyAccess import PyAccess

if __name__ == "__main__":
    PyAccess().start()
