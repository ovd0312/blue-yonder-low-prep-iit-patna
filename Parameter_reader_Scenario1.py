import pandas as pd

# drones (drone types)

# items (item types)

# demand

ENERGY_COST = 0
MAX_SPEED = 0


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
    payload_weight_cap = 0
    payload_volume_cap = 0
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
        "Day1": 0,
        "Day2": 0,
        "Day3": 0,
    }
    rest_time = {
        "Day1": 0,
        "Day2": 0,
        "Day3": 0,

    }
    charging_time = {
        "Day1": 0,
        "Day2": 0,
        "Day3": 0,
    }
    maint_cost = {
        "Day1": 0,
        "Day2": 0,
        "Day3": 0,
    }
    energy_cost = {
        "Day1": 0,
        "Day2": 0,
        "Day3": 0,
    }


class Recharge:
    x = 0
    y = 0
    z = 0
    capacity = 0
    current = 0


class Warehouse(Recharge):
    pass


def parameter_extractor(path):  # returns (list of drone type objects), WareHouse object, Max Speed, Energy Cost

    data = pd.read_csv(path)

    drones = []
    WH = Warehouse()

    MS = 0
    EC = 0

    num_drones = 0

    for ind in data.index:
        tp = data['Type'][ind]
        if ind > 1 and tp[0] == 'D':
            num_drones = max(num_drones, ord(tp[5]) - 48)

    for _ in range(num_drones):
        drones.append(DroneType())

    for ind in data.index:
        par = data['Parameter_ID'][ind]
        val = data['Value'][ind]
        unit = data['Unit'][ind]
        tp = data['Type'][ind]

        if par == 'MaxSpeed (M)':
            MS = val

        elif par == 'Cost(C)':
            EC = val

        else:
            if tp[0] == 'W':
                if par[3] == 'X':
                    WH.x = val
                elif par[3] == 'Y':
                    WH.y = val
                else:
                    WH.z = val

            else:
                t = ord(tp[5]) - 48 - 1
                pf = par[0]

                if pf == 'P':
                    drones[t].P = val
                elif pf == 'Q':
                    drones[t].Q = val
                elif pf == 'A':
                    drones[t].A = val
                elif pf == 'B':
                    drones[t].B = val
                elif pf == 'C':
                    drones[t].C = val
                elif pf == 'D':
                    drones[t].count = val

    return drones, WH, MS, EC
