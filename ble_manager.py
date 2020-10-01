#!/usr/bin/python3
#
# @file    ble_manager.py
# 
# @brief       
#
# @author  Garrett Hagen <garretthagen21@gmail.com>
# 
# @date    2020-09-30 
#

from peripheral import *

ble_app = G8BLEApplication(register=False)
ble_adv = G8Advertisement(register=False)


def initialize(start_run=True):
    ble_app.register()
    ble_adv.register()

    if start_run:
        run()


def run():
    ble_app.run()


def stop():
    ble_app.quit()


def update_proprio_angle(angle):
    ble_app.measurement_service.proprio_characteristic.set_value(angle)


def update_inclination_angle(angle):
    ble_app.measurement_service.proprio_characteristic.set_value(angle)


def update_limit_state(state):
    ble_app.machine_service.limit_state_characteristic.set_value(state.upper())


def update_hardstop_state(state):
    ble_app.machine_service.hardstop_state_characteristic.set_value(state.upper())


def update_machine_state(state):
    ble_app.machine_service.machine_state_characteristic.set_value(state.upper())


def simulate():
    import random
    import time
    machine_states = ["AUTORUN", "IDLE", "MOVING", "CALIBRATING"]
    limit_states = ["LOWER", "UPPER", "NONE"]
    while True:
        update_machine_state(random.choice(machine_states))
        update_limit_state(random.choice(limit_states))
        update_hardstop_state(random.choice(limit_states))
        update_inclination_angle(random.randint)
        update_proprio_angle(random.randint)
        time.sleep(0.5)


try:
    initialize()
    simulate()
except KeyboardInterrupt:
    stop()
    exit(0)
