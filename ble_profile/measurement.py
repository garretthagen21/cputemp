#!/usr/bin/python3
#
# @file    measurement.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-24 
#

from gatt.service import Service
from gatt.characteristic import Characteristic
from gatt.descriptor import Descriptor
from ble_profile.identifiers import *




def write_inc_callback_1(value):
    print("Write value callback 1: " + value)


def write_inc_callback_2(value):
    print("Write value callback 2: " + value)


def read_prop_callback():
    return 2.5


def read_limit_callback():
    return "NONE"


class G8MeasurementService(Service):

    def __init__(self, index=0):
        Service.__init__(self, index=index, uuid=MEASUREMENT_SVC_UUID.full_string(), primary=True)

        # Add characteristics
        self.add_characteristic(G8InclincationCharacteristic(self))
        self.add_characteristic(G8ProprioCharacteristic(self))
        self.add_characteristic(G8LimitStateCharacteristic(self))


class G8InclincationCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=INC_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read", "write"],
            description="Inclination Angle Characteristic", notify_timeout=Characteristic.DEFAULT_NOTIFY_TIMEOUT,
            on_write_callbacks=[lambda value: write_inc_callback_1(value), lambda value: write_inc_callback_2(value)])

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Inclination Angle"))
        self.set_value(0, False)


class G8ProprioCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=PROPRIO_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read"],
            description="Proprio Angle Characteristic", notify_timeout=Characteristic.DEFAULT_NOTIFY_TIMEOUT,
            on_write_callbacks=[lambda value: write_inc_callback_1(value)])

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Proprio Angle"))

        self.set_value(0, False)


class G8LimitStateCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=LIMITSTATE_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read"],
            description="Limit State Characteristic", notify_timeout=Characteristic.DEFAULT_NOTIFY_TIMEOUT,
            on_write_callbacks=[lambda value: write_inc_callback_1(value)])

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Limit State"))

        self.set_value("NONE", False)
