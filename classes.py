# drones (drone types)

# items (item types)

# demand

ENERGY_COST = 0
MAX_SPEED = 0


class Item:
    def __init__(self):
        self.item_id = 0
        self.weight = 0
        self.l = 0
        self.b = 0
        self.h = 0


class Demand:
    def __init__(self):
        self.demand_id = 0
        self.WH_id = 0
        self.item_id = 0
        self.day = 0
        self.x = 0
        self.y = 0
        self.z = 0
        self.del_start = 0
        self.del_end = 0


class Work:
    def __init__(self, demand_id, day, start_pos, end_pos, start_time, end_time, status, speed, energy_consumed, energy_cost, total_weight):
        self.demand_id = demand_id
        self.day = day
        self.start_pos = start_pos  # [x, y, z]
        self.end_pos = end_pos  # [x, y, z]
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.speed = speed
        self.energy_consumed = energy_consumed  # energy consumed per second
        self.energy_cost = energy_cost  # per second
        self.total_weight = total_weight


class DroneType:
    def __init__(self):
        self.battery_cap = 0
        self.base_weight = 0
        self.payload_weight_cap = 0
        self.payload_volume_cap = 0
        self.max_slots = 0
        self.max_speed = 0
        self.count = 0
        self.fixed_cost = 0
        self.var_cost = 0
        self.P = 0
        self.Q = 0
        self.A = 0
        self.B = 0
        self.C = 0


class Drone:
    def __init__(self):
        self.drone_id = ''
        self.battery_cap = 0
        self.base_weight = 0
        self.payload_weight_cap = 0
        self.payload_volume_cap = 0
        self.max_slots = 0
        self.max_speed = 0
        self.count = 0
        self.fixed_cost = 0
        self.var_cost = 0
        self.P = 0
        self.Q = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.instruction_set = []   # will contain work objects
        self.flight_time = {
            "Day1": 0,
            "Day2": 0,
            "Day3": 0,
        }
        self.rest_time = {
            "Day1": 0,
            "Day2": 0,
            "Day3": 0,

        }
        self.charging_time = {
            "Day1": 0,
            "Day2": 0,
            "Day3": 0,
        }
        self.maint_cost = {
            "Day1": 0,
            "Day2": 0,
            "Day3": 0,
        }
        self.energy_cost = {
            "Day1": 0,
            "Day2": 0,
            "Day3": 0,
        }


class Zone:
    def __init__(self):
        self.X = [0] * 8
        self.Y = [0] * 8
        self.Z = [0] * 8


class Recharge:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.capacity = 0
        self.current = 0


# TODO: ask query about recharge cap and current not present in input
# TODO: ask query about output for every second
# TODO: ask query about start and end of working day

class Warehouse(Recharge):
    pass
