#!/usr/bin/python3
#
# @file    advertising.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-30 
#

from gatt.advertisement import Advertisement
from ble_profile.identifiers import *
from ble_profile.measurement import MeasurementService

class G8Advertisement(Advertisement):
    #MANUFACTURER_NAME = "Gener-8 Inc."

    def __init__(self, index=0):
        Advertisement.__init__(self, index, "peripheral")

        # Configure advertising data
        self.add_local_name(LOCAL_NAME)
        self.include_tx_power = True
        # self.add_manufacturer_data(0xFFFF, "Gener-8 Inc.")
        print("Manufacturer Data")
        print(MANUFACTUER_DATA)
        #print(UUID('1234').full_string())

        # Add our services
        self.add_service_uuid(MeasurementService)

        # Advertise our available services
        self.add_service_uuid(INFORMATION_SVC_UUID.shortened_string())
        self.add_service_uuid(MEASUREMENT_SVC_UUID.shortened_string())
        self.add_service_uuid(MACHINE_SVC_UUID.shortened_string())
        self.add_service_uuid(CALIBRATION_SVC_UUID.shortened_string())



        #self.add_manufacturer_data(0xFFFF, self.MANUFACTURER_NAME.encode('utf-8'))
        #self.add_service_data('9999', [0x00, 0x01, 0x02, 0x03, 0x04])
