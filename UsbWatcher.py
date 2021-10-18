from time import sleep

import pyudev
from pyudev import MonitorObserver


class UsbWatcher:
    def __init__(self, callback):
        self.context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(self.context)
        monitor.filter_by(subsystem='input')
        # noinspection PyTypeChecker
        self.observer = MonitorObserver(monitor, callback, name="monitor-observer")

    def get_usb_devices_connected(self):
        my_list = set()
        devices = self.context.list_devices(subsystem='input', ID_INPUT_MOUSE=True)
        for device in devices:
            if device.sys_name.startswith('event'):
                model = device.properties.get("ID_MODEL")
                if model is not None:
                    my_list.add(model)
        return my_list

    def start_watching(self):
        self.observer.start()
        try:
            while True:
                sleep(100000000)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()
