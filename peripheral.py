#!/usr/bin/python3
#
# @file    peripheral.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-24 
#


from gatt.application import Application
from gatt.advertisement import Advertisement
from ble_profile.identifiers import *
from ble_profile.measurement import G8MeasurementService
# from ble_profile.information import G8InformationService
from ble_profile.machine import G8MachineService


class G8Advertisement(Advertisement):

    def __init__(self, index=0, register=True):
        Advertisement.__init__(self, index, "peripheral")

        # Configure advertising data
        self.add_local_name(LOCAL_NAME)
        self.add_manufacturer_data(0xFFFF, MANUFACTUER_DATA)
        self.include_tx_power = True

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
        self.measurement_service = G8MeasurementService()
        # self.information_service = G8InformationService()
        self.machine_service = G8MachineService()
        # self.calibration_service = G8CalibrationService()

        # self.add_service(self.information_service)
        self.add_service(self.measurement_service)
        self.add_service(self.machine_service)
        # self.add_service(self.calibration_service)

        if register:
            self.register()

# g8_app = G8BLEApplication()
# g8_adv = G8Advertisement()

# try:
#    g8_app.run()
# except KeyboardInterrupt:
#    g8_app.quit()
