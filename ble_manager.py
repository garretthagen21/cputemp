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
    update_num = 0

    while DO_CONTINUE:
        time.sleep(5.0)
        print("Simulated Update Round: " + str(update_num))
        update_num += 1
        #update_machine_state(random.choice(machine_states))
        #update_limit_state(random.choice(limit_states))
        #update_hardstop_state(random.choice(limit_states))
        update_inclination_angle(random.randint(0, 100))
        update_proprio_angle(random.randint(0, 100))


DO_CONTINUE = True
import threading


try:
    initialize()

    # Create a Thread with a function without any argumen
    sim_thread = threading.Thread(target=simulate())
    sim_thread.start()

except KeyboardInterrupt:
    global DO_CONTINUE
    DO_CONTINUE = False
    #sim_thread.join()
    stop()
    exit(0)
