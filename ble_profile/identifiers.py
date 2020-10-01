#!/usr/bin/python3
#
# @file    identifiers.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-30 
#
from gatt.uuid import UUID

# Advertisement data
LOCAL_NAME = "Gener-8"
MANUFACTUER_DATA = [0x47, 0x65, 0x6e, 0x65, 0x72, 0x2d, 0x38, 0x20, 0x49, 0x6e, 0x63, 0x2e]

# Universal descriptor UUID
DESCRIPTOR_UUID = UUID("2901")

# Information Service
INFORMATION_SVC_UUID = UUID("0010")
VERSION_CHARACTERISTIC_UUID = UUID("0011")
WIFICRED_CHARACTERISTIC_UUID = UUID("0012")
WIFICONNECTION_CHARACTERISTIC_UUID = UUID("0013")

# Measurement Service
MEASUREMENT_SVC_UUID = UUID("0020")
INC_CHARACTERISTIC_UUID = UUID("0021")
PROPRIO_CHARACTERISTIC_UUID = UUID("0022")
LIMITSTATE_CHARACTERISTIC_UUID = UUID("0023")  # TODO: Move to machine service

# Machine Service
MACHINE_SVC_UUID = UUID("0030")
MACHINESTATE_CHARACTERISTIC_UUID = UUID("0031")
HARDSTOPSTATE_CHARACTERISTIC_UUID = UUID("0032")

# Calibration Service
CALIBRATION_SVC_UUID = UUID("0040")
CALSTATUS_CHARACTERISTIC_UUID = UUID("0041")  # PROG:<number>, FAIL:<reason>, SUCCESS:<reason>, IDLE:<null>
ACCELOFFSET_CHARACTERISTIC_UUID = UUID("0042")
GYROOFFSET_CHARACTERISTIC_UUID = UUID("0043")
LASTCALTIME_CHARACTERISTIC_UUID = UUID("0044")
