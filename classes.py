# drones (drone types)

# items (item types)

# demand

ENERGY_COST = 0 

class Item:
    item_id = 0
    weight = 0
    l = 0
    b = 0
    h = 0

class Demand:
    demand_id = 0
    WH_id = 0
    item_id = 0
    day = 0
    x = 0
    y = 0
    z = 0
    del_start = ""
    del_end = ""

class DroneType:
    battery_cap = 0
    base_weight = 0
    payload_cap = 0
    max_slots = 0
    max_speed = 0
    count = 0
    fixed_cost = 0
    var_cost = 0
    P = 0
    Q = 0
    A = 0
    B = 0
    C = 0

class Drone:
    drone_id = 0
    battery_cap = 0
    base_weight = 0
    payload_cap = 0
    max_slots = 0
    max_speed = 0
    count = 0
    fixed_cost = 0
    var_cost = 0
    P = 0
    Q = 0
    A = 0
    B = 0
    C = 0
    flight_time = {
        "Day1":0,
        "Day2":0,
        "Day3":0,
    }
    rest_time = {
        "Day1":0,
        "Day2":0,
        "Day3":0,

    }
    charging_time = {
        "Day1":0,
        "Day2":0,
        "Day3":0,
    }
    maint_cost = {
        "Day1":0,
        "Day2":0,
        "Day3":0,
    }
    energy_cost = {
        "Day1":0,
        "Day2":0,
        "Day3":0,
    }

class Recharge:
    x = 0
    y = 0
    z = 0
    capacity = 0
    current = 0

#TODO: ask query about recharge cap and current not present in input
#TODO: ask query about output for every second
#TODO: ask query about start and end of working day

class Warehouse (Recharge):
    pass
