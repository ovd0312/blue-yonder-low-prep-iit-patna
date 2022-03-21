import pandas as pd
import classes as cl


def parameter_extractor(path):  # returns (list of drone type objects), WareHouse object, Max Speed, Energy Cost

    data = pd.read_csv(path)

    drones = []
    WH = cl.Warehouse()

    MS = 0
    EC = 0

    num_drones = 0

    for ind in data.index:
        tp = data['Type'][ind]
        if ind > 1 and tp[0] == 'D':
            num_drones = max(num_drones, ord(tp[5]) - 48)

    for _ in range(num_drones):
        drones.append(cl.DroneType())

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
