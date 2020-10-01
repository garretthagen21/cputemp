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

# !/usr/bin/python3

"""Copyright (c) 2019, Douglas Otwell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from gatt.advertisement import Advertisement
from gatt.application import Application
from gatt.uuid import UUID
from ble_profile.measurement import MeasurementService



class G8Advertisement(Advertisement):
    MANUFACTURER_NAME = "Gener-8 Inc."

    def __init__(self, index=0):
        Advertisement.__init__(self, index, "peripheral")
        self.add_local_name("Gener-8")

        print("Manufacturer Name: "+self.MANUFACTURER_NAME+" as bytes: "+str(self.MANUFACTURER_NAME.encode('utf-8')))
        uuid = UUID(0x1234)
        uuid.as_string()

        # self.add_manufacturer_data(0xFFFF, "Gener-8 Inc.")
        # self.add_service_uuid(MEASUREMENT_SVC_UUID)
        self.include_tx_power = True
        self.add_service_uuid('180D')
        self.add_service_uuid('180F')
        self.add_manufacturer_data(0xFFFF, "Gener-8 Inc.")
        self.add_service_data('9999', [0x00, 0x01, 0x02, 0x03, 0x04])


app = Application()
app.add_service(MeasurementService())
app.register()

adv = G8Advertisement()
adv.register()

try:
    app.run()

except KeyboardInterrupt:
    app.quit()
