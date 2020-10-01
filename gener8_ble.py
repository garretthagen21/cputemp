#!/usr/bin/python3
#
# @file    gener8_ble.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-24 
#


from gatt.application import Application
from gatt.advertisement import Advertisement

from ble_profile.measurement import G8MeasurementService

from ble_profile.identifiers import *


class G8Advertisement(Advertisement):

    def __init__(self, index=0, register=True):
        Advertisement.__init__(self, index, "peripheral")

        # Configure advertising data
        self.add_local_name(LOCAL_NAME)
        self.include_tx_power = True
        self.add_manufacturer_data(0xffff, [0x47, 0x65, 0x6e, 0x65])

        # Advertise our available services
        self.add_service_uuid(INFORMATION_SVC_UUID.shortened_string())
        self.add_service_uuid(MEASUREMENT_SVC_UUID.shortened_string())
        self.add_service_uuid(MACHINE_SVC_UUID.shortened_string())
        self.add_service_uuid(CALIBRATION_SVC_UUID.shortened_string())

        # Register if specified
        if register:
            self.register()


class G8BLEApplication(Application):
    def __init__(self, register=True):
        Application.__init__(self)

        # Add our services
        self.add_service(G8MeasurementService())

        if register:
            self.register()


g8_app = G8BLEApplication()
g8_adv = G8Advertisement()

try:
    g8_app.run()
except KeyboardInterrupt:
    g8_app.quit()
