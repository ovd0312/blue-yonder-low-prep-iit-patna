import pandas as pd
import classes as cl


# returns list of drone type objects, list of WareHouse objects, list of recharge objects, list of zone objects, Max Speed, Energy Cost

def parameter_extractor(path):
    data = pd.read_csv(path)

    drones = []
    wh = []
    recs = []
    zones = []

    MS = 0
    EC = 0

    num_drones = 0
    num_wh = 0
    num_recs = 0
    num_zones = 0

    for ind in data.index:
        tp = data['Type'][ind]
        par = data['Parameter_ID'][ind]
        if ind < 2:
            continue

        if tp[0] == 'D':
            num_drones = max(num_drones, ord(tp[5]) - 48)

        if tp[0] == 'N':
            num_zones = max(num_zones, ord(par[1]) - 48)

        if tp[0] == 'R':
            num_recs = max(num_recs, ord(par[0]) - 64)

        if tp[0] == 'W':
            num_wh = max(num_wh, ord(par[2]) - 48)

    # print(num_recs)

    for _ in range(num_drones):
        drones.append(cl.DroneType())

    for _ in range(num_zones):
        zones.append(cl.Zone())

    for _ in range(num_recs):
        recs.append(cl.Recharge())

    for _ in range(num_wh):
        wh.append(cl.Warehouse())

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

            if tp[0] == 'N':
                t = ord(par[1]) - 48 - 1
                v = ord(par[2]) - 48 - 1
                pf = par[0]

                if pf == 'X':
                    zones[t].X[v] = val
                elif pf == 'Y':
                    zones[t].Y[v] = val
                else:
                    zones[t].Z[v] = val

            elif tp[0] == 'W':
                t = ord(par[2]) - 48 - 1
                if par[3] == 'X':
                    wh[t].x = val
                elif par[3] == 'Y':
                    wh[t].y = val
                else:
                    wh[t].z = val

            elif tp[0] == 'R':
                t = ord(par[0]) - 65
                if par[1] == 'X':
                    recs[t].x = val
                elif par[1] == 'Y':
                    recs[t].y = val
                else:
                    recs[t].z = val

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
                else:
                    drones[t].count = val

    return drones, wh, recs, zones, MS, EC
