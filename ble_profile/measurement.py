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

MEASUREMENT_SVC_UUID = "00000001-710e-4a5b-8d75-3e5b444bc3cf"
INC_CHARACTERISTIC_UUID = "00000002-710e-4a5b-8d75-3e5b444bc3cf"
PROPRIO_CHARACTERISTIC_UUID = "00000003-710e-4a5b-8d75-3e5b444bc3cf"
LIMITSTATE_CHARACTERISTIC_UUID = "00000004-710e-4a5b-8d75-3e5b444bc3cf"
DESCRIPTOR_UUID="2901"


def write_inc_callback_1(value):
    print("Write value callback 1: "+value)
def write_inc_callback_2(value):
    print("Write value callback 2: "+value)


def read_prop_callback():
    return 2.5

def read_limit_callback():
    return "NONE"


class MeasurementService(Service):

    def __init__(self, index=0):

        Service.__init__(self, index, MEASUREMENT_SVC_UUID, True)

        # Add characteristics
        self.add_characteristic(InclincationCharacteristic(self))
        self.add_characteristic(ProprioCharacteristic(self))
        self.add_characteristic(LimitStateCharacteristic(self))



class InclincationCharacteristic(Characteristic):
    def __init__(self, service):

        Characteristic.__init__(
            self, service=service, uuid=INC_CHARACTERISTIC_UUID, flags=["notify", "read","write"],
            description="Inclination Angle Characteristic", notify_timeout=Characteristic.DEFAULT_NOTIFY_TIMEOUT,
            on_write_callbacks=[lambda value: write_inc_callback_1(value),lambda value: write_inc_callback_2(value)])

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID,
                                       flags=["read"], description="Inclination Angle"))
        self.set_value(0,False)


class ProprioCharacteristic(Characteristic):
    def __init__(self, service):

        Characteristic.__init__(
            self, service=service, uuid=PROPRIO_CHARACTERISTIC_UUID, flags=["notify", "read"],
            description="Proprio Angle Characteristic", notify_timeout=Characteristic.DEFAULT_NOTIFY_TIMEOUT,
            on_write_callbacks=[lambda value: write_inc_callback_1(value)])

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID,
                                       flags=["read"], description="Proprio Angle"))

        self.set_value(0,False)


class LimitStateCharacteristic(Characteristic):
    def __init__(self, service):

        Characteristic.__init__(
            self, service=service, uuid=LIMITSTATE_CHARACTERISTIC_UUID, flags=["notify", "read"],
            description="Limit State Characteristic", notify_timeout=Characteristic.DEFAULT_NOTIFY_TIMEOUT,
            on_write_callbacks=[lambda value: write_inc_callback_1(value)])

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID,
                                       flags=["read"], description="Limit State"))

        self.set_value("NONE",False)