#!/usr/bin/python3
#
# @file    uuid.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-30 
#


class UUID(object):
    EXTENDED_FILLER = '0000-1000-8000'

    def __init__(self, attribute_uid: str, device_uid: str = '0808', company_uid: str = '1421',
                 ble_sig_uid: str = '00805F9B'):
        self.attribute_uid = attribute_uid
        self.device_uid = device_uid
        self.company_uid = company_uid
        self.ble_sig_uid = ble_sig_uid

        if len(attribute_uid) != 4: raise Exception("attribute_id must be a hex value of length 4")
        if len(device_uid) != 4: raise Exception("device_uid must be a hex value of length 4")
        if len(company_uid) != 4: raise Exception("company_uid must be a hex value of length 4")
        if len(ble_sig_uid) != 8: raise Exception("ble_sig_id must be a hex value of length 8")

    def full_string(self):
        return self.device_uid + self.attribute_uid + '-' + self.EXTENDED_FILLER + "-" + self.ble_sig_uid + self.company_uid

    def shortened_string(self):
        return self.attribute_uid

