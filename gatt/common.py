#!/usr/bin/python3
#
# @file    common.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-24 
#


import dbus
import dbus.mainloop.glib
import dbus.exceptions

try:
    from gi.repository import GObject
except ImportError:
    import gobject as GObject

BLUEZ_SERVICE_NAME = "org.bluez"
GATT_MANAGER_IFACE = "org.bluez.GattManager1"
DBUS_PROP_IFACE = "org.freedesktop.DBus.Properties"

class InvalidArgsException(dbus.exceptions.DBusException):
    _dbus_error_name = "org.freedesktop.DBus.Error.InvalidArgs"


class NotSupportedException(dbus.exceptions.DBusException):
    _dbus_error_name = "org.bluez.Error.NotSupported"


class NotPermittedException(dbus.exceptions.DBusException):
    _dbus_error_name = "org.bluez.Error.NotPermitted"

def value_to_byte_array(raw_val):
    value = []

    str_value = str(raw_val)

    for c in str_value:
        value.append(dbus.Byte(c.encode()))

    return value