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






class G8MeasurementService(Service):

    def __init__(self, index=0):
        Service.__init__(self, index=index, uuid=MEASUREMENT_SVC_UUID.full_string(), primary=True)

        # Add characteristics
        self.inclination_characteristic = G8InclincationCharacteristic(self)
        self.proprio_characteristic = G8ProprioCharacteristic(self)

        self.add_characteristic(self.inclination_characteristic)
        self.add_characteristic(self.proprio_characteristic)


class G8InclincationCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=INC_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read"],
            description="Inclination Angle Characteristic")

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Inclination Angle"))
        self.set_value(0, False)


class G8ProprioCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
            self, service=service, uuid=PROPRIO_CHARACTERISTIC_UUID.full_string(), flags=["notify", "read"],
            description="Proprio Angle Characteristic")

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID.shortened_string(),
                                       flags=["read"], description="Proprio Angle"))

        self.set_value(0, False)

