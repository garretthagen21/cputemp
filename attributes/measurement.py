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

NOTIFY_TIMEOUT = 5000
MEASUREMENT_SVC_UUID = "00000001-710e-4a5b-8d75-3e5b444bc3cf"
INC_CHARACTERISTIC_UUID = "00000002-710e-4a5b-8d75-3e5b444bc3cf"
PROPRIO_CHARACTERISTIC_UUID = "00000003-710e-4a5b-8d75-3e5b444bc3cf"
LIMIT_CHARACTERISTIC_UUID = "00000004-710e-4a5b-8d75-3e5b444bc3cf"
INC_DESCRIPTOR_UUID = "2901"
PROPRIO_DESCRIPTOR_UUID = "2902"
LIMIT_DESCRIPTOR_UUID = "2903"


def read_value_callback():
    return 1.5


class MeasurementService(Service):

    def __init__(self, index=0):
        self.active_limit = "NONE"  # LOWER, MIDDLE, NONE
        self.proprio = 0.0
        self.inclination = 0.0

        Service.__init__(self, index, MEASUREMENT_SVC_UUID, True)

        # Add to inclination characteristic
        self.add_characteristic(InclincationCharacteristic(self))

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
        self.notifying = False

        Characteristic.__init__(
            self, service=service, uuid=INC_CHARACTERISTIC_UUID, flags=["notify", "read"],
            description="Inclination Angle Characteristic", notify_timeout=DEFAULT_NOTIFY_TIMEOUT,
            read_value_callback=lambda: read_value_callback())

        self.add_descriptor(Descriptor(characteristic=self, uuid=INC_DESCRIPTOR_UUID,
                                        flags=["read"], description="Inclination Angle"))


