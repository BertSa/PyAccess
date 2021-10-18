from gi.repository import Gtk


def _create_menu_item_check(label: str, callback: callable, active: bool):
    """Create a basic CheckMenuItem

    :param label: Name you want to be labeled
    :param callback: Methode that's gonna be called
    :param active: Will activate if True
    :return: Return an item menu
    :rtype: Gtk.CheckMenuItem
    """
    item = Gtk.CheckMenuItem()
    item.set_label(label)
    item.connect('activate', callback)
    if active:
        item.activate()
    return item


def _create_menu_item(label: str, callback):
    """Create a basic MenuItem

    :param label: Name you want to be labeled
    :param callback: Methode that's gonna be called
    :return: Return an item menu
    :rtype: Gtk.MenuItem
    """
    item = Gtk.MenuItem()
    item.set_label(label)
    item.connect('activate', callback)
    return item


def _createMoreMenu(*args):
    """Create a subMenu named more

    :param args: MenuItem you want inside the more submenu
    :type args: Gtk.MenuItem
    :return: Return a submenu
    :rtype: Gtk.Menu
    """
    sub_menu = Gtk.Menu()
    for item in args:
        sub_menu.append(item)
    item_sub_menu = Gtk.MenuItem()
    item_sub_menu.set_label("More")
    item_sub_menu.set_submenu(sub_menu)
    return item_sub_menu
