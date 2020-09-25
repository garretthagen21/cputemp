#!/usr/bin/python3
#
# @file    descriptor.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-24 
#

from gatt.common import *

GATT_DESC_IFACE = "org.bluez.GattDescriptor1"


class Descriptor(dbus.service.Object):
    def __init__(self, characteristic, uuid, flags, description="Unnamed Descriptor"):
        index = characteristic.get_next_index()
        self.path = characteristic.path + '/desc' + str(index)
        self.uuid = uuid
        self.flags = flags
        self.chrc = characteristic
        self.bus = characteristic.get_bus()
        self.description = description
        dbus.service.Object.__init__(self, self.bus, self.path)

    def get_properties(self):
        return {
            GATT_DESC_IFACE: {
                'Characteristic': self.chrc.get_path(),
                'UUID': self.uuid,
                'Flags': self.flags,
            }
        }

    def get_path(self):
        return dbus.ObjectPath(self.path)

    @dbus.service.method(DBUS_PROP_IFACE,
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        if interface != GATT_DESC_IFACE:
            raise InvalidArgsException()

        return self.get_properties()[GATT_DESC_IFACE]

    @dbus.service.method(GATT_DESC_IFACE,
                         in_signature='a{sv}',
                         out_signature='ay')
    def ReadValue(self, options):
        value = []
        for c in self.description:
            value.append(dbus.Byte(c.encode()))

        return value

    @dbus.service.method(GATT_DESC_IFACE, in_signature='aya{sv}')
    def WriteValue(self, value, options):
        if not self.writable:
            raise NotPermittedException()
        self.value = value
