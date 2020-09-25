#!/usr/bin/python3
#
# @file    characteristic.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-24 
#

from gatt.common import *

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"




class Characteristic(dbus.service.Object):
    """
    org.bluez.GattCharacteristic1 interface implementation
    """
    DEFAULT_NOTIFY_TIMEOUT = 1000


    def __init__(self, service, uuid, flags, description="Unnamed Characteristic",
                 notify_timeout=DEFAULT_NOTIFY_TIMEOUT,
                 on_write_callbacks=[]):

        index = service.get_next_index()
        self.notifying = False
        self.path = service.path + '/char' + str(index)
        self.bus = service.get_bus()
        self.uuid = uuid
        self.service = service
        self.flags = flags
        self.descriptors = []
        self.next_index = 0
        self.description = description
        self.on_write_callbacks = on_write_callbacks
        self.notify_timeout = notify_timeout
        self.current_bytes = value_to_byte_array("")
        dbus.service.Object.__init__(self, self.bus, self.path)

    def get_properties(self):
        return {
            GATT_CHRC_IFACE: {
                'Service': self.service.get_path(),
                'UUID': self.uuid,
                'Flags': self.flags,
                'Descriptors': dbus.Array(
                    self.get_descriptor_paths(),
                    signature='o')
            }
        }

    def get_path(self):
        return dbus.ObjectPath(self.path)

    def get_bus(self):
        bus = self.bus

        return bus

    def get_next_index(self):
        idx = self.next_index
        self.next_index += 1

        return idx

    def add_descriptor(self, descriptor):
        self.descriptors.append(descriptor)

    def get_descriptor_paths(self):
        result = []
        for desc in self.descriptors:
            result.append(desc.get_path())
        return result

    def get_descriptors(self):
        return self.descriptors

    def set_value(self, new_val, update=True):
        self.current_bytes = value_to_byte_array(new_val)
        if update:
            self.update()

    def get_value(self):
        return str(self.current_bytes)

    def update(self):
        self.PropertiesChanged(GATT_CHRC_IFACE, {"Value": self.current_bytes}, [])


    def _on_notification_timer_trigger(self):

        print("NotifCallback NotifyingStatus: " + str(self.notifying))
        if self.notifying:
            self.update()
            print("Notification Callback Set for " + self.description + ": " + self.uuid)

        return self.notifying

    @dbus.service.method(GATT_CHRC_IFACE,
                         in_signature='a{sv}',
                         out_signature='ay')
    def ReadValue(self, options):
        print("ReadValue() for " + self.description + ": " + self.uuid)
        return self.current_bytes

    @dbus.service.method(GATT_CHRC_IFACE, in_signature='aya{sv}')
    def WriteValue(self, value, options):
        print("WriteValue() " + self.description + ": " + self.uuid)
        self.current_bytes = value

        # Update observers
        value_str = self.get_value()
        for write_callback in self.on_write_callbacks:
            write_callback(value_str)

    @dbus.service.method(GATT_CHRC_IFACE)
    def StartNotify(self):
        print("StartNotify NotifyingStatus: " + str(self.notifying))

        if self.notifying:
            return

        print("StartNotify() for Characteristic " + self.uuid)
        self.notifying = True
        self.update()


    @dbus.service.method(GATT_CHRC_IFACE)
    def StopNotify(self):
        print("StopNotify() for " + self.description + ": " + self.uuid)
        self.notifying = False

    @dbus.service.method(DBUS_PROP_IFACE,
                         in_signature='s',
                         out_signature='a{sv}')
    def GetAll(self, interface):
        if interface != GATT_CHRC_IFACE:
            raise InvalidArgsException()

        return self.get_properties()[GATT_CHRC_IFACE]

    @dbus.service.signal(DBUS_PROP_IFACE,
                         signature='sa{sv}as')
    def PropertiesChanged(self, interface, changed, invalidated):
        print("PropertiesChanged() for " + self.description + ": " + self.uuid)
        pass