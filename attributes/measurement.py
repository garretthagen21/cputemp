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

from service import *

MEASUREMENT_SVC_UUID = "00000001-710e-4a5b-8d75-3e5b444bc3cf"
INC_CHARACTERISTIC_UUID = "00000002-710e-4a5b-8d75-3e5b444bc3cf"
PROPRIO_CHARACTERISTIC_UUID = "00000003-710e-4a5b-8d75-3e5b444bc3cf"
LIMIT_CHARACTERISTIC_UUID = "00000004-710e-4a5b-8d75-3e5b444bc3cf"
DESCRIPTOR_UUID="2901"


def read_inc_callback():
    return 1.5

def read_prop_callback():
    return 2.5

def read_limit_callback():
    return "NONE"


class MeasurementService(Service):

    def __init__(self, index=0):
        self.active_limit = "NONE"  # LOWER, MIDDLE, NONE
        self.proprio = 0.0
        self.inclination = 0.0

        Service.__init__(self, index, MEASUREMENT_SVC_UUID, True)

        # Add characteristics
        self.add_characteristic(InclincationCharacteristic(self))
        self.add_characteristic(ProprioCharacteristic(self))

    def is_in_motion(self):
        return self.state != "IDLE" and self.state != "CALIBRATION"

    def set_proprio(self, proprio):
        self.proprio = proprio

    def set_inclination(self, inclination):
        self.inclination = inclination

    def set_state(self, state):
        self.state = state


class InclincationCharacteristic(Characteristic):
    def __init__(self, service):

        Characteristic.__init__(
            self, service=service, uuid=INC_CHARACTERISTIC_UUID, flags=["notify", "read"],
            description="Inclination Angle Characteristic", notify_timeout=DEFAULT_NOTIFY_TIMEOUT,
            read_value_callback=lambda: read_inc_callback())

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID,
                                       flags=["read"], description="Inclination Angle"))


class ProprioCharacteristic(Characteristic):
    def __init__(self, service):

        Characteristic.__init__(
            self, service=service, uuid=PROPRIO_CHARACTERISTIC_UUID, flags=["notify", "read"],
            description="Proprio Angle Characteristic", notify_timeout=DEFAULT_NOTIFY_TIMEOUT,
            read_value_callback=lambda: read_prop_callback())

        self.add_descriptor(Descriptor(characteristic=self, uuid=DESCRIPTOR_UUID,
                                       flags=["read"], description="Proprio Angle"))
