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
    def __init__(self, demand_id=0, day=0, start_pos=[], end_pos=[], start_time=0, end_time=0, status=0, speed=0,
                 energy_consumed=0, energy_cost=0, total_weight=0):
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
        self.drone_type = 0
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



def read_demands(path):

    df=pd.read_csv(path)
    
    demands=[]
    
    for i in df:
        demand=Demand()
    
        if i=="X":
            demand.x = df["X"]
    
        elif i=="Y":
            demand.y = df["Y"]
    
        elif i=="Z":
            demand.z = df["Z"]
    
        elif i=="DeliveryFrom":
            demand.del_start=df["DeliveryFrom"]
    
        elif i=="DeliveryTo":
            demand.del_end=df["DeliveryTo"]
    
        elif i=="DemandID":
            for j in range(len(df)):
                demand.demand_id=int(df["Demand ID"][j][1:])
    
        elif i=="WH":
            for j in range(len(df)):
                demand.WH_id=int(df["WH"][j][2:])
    
        elif i=="Item":
            for j in range(len(df)):
                demand.item_id=int(df["Item"][j][5:])
    
        elif i=="Day":
            for j in range(len(df)):
                demand.item_id=int(df["Item"][j][4:])

        demands.append(demand)
    
    return demands
