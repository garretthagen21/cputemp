#!/usr/bin/python3
#
# @file    machine.py
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


class G8MachineService(Service):

    def __init__(self, index=0):
        Service.__init__(self, index=index, uuid=MACHINE_SVC_UUID.full_string(), primary=True)

        # Add characteristics
        self.machine_state_characteristic = G8MachineStateCharacteristic(self)
        self.limit_state_characteristic = G8LimitStateCharacteristic(self)
        self.hardstop_state_characteristic = G8HardStopStateCharacteristic(self)

        self.add_characteristic(self.machine_state_characteristic)
        self.add_characteristic(self.limit_state_characteristic)
        self.add_characteristic(self.hardstop_state_characteristic)


class G8MachineStateCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=MACHINESTATE_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read"],
            description="Machine State Characteristic")

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Machine State"))

        self.set_value("IDLE", False)


class G8LimitStateCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=LIMITSTATE_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read"],
            description="Limit State Characteristic")

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Limit State"))

        self.set_value("NONE", False)


class G8HardStopStateCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=HARDSTOPSTATE_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read"],
            description="Hard Stop State Characteristic")

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Hard Stop State"))

        self.set_value("NONE", False)
