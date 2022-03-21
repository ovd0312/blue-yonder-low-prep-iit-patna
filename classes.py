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
