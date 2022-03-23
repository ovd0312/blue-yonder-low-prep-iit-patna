import csv
from classes import *
import pandas as pd
def store_path_cost(drones, wh, rec, cost_file):
  keys = ["DroneID", "Day", "Resting Time (s)","Charging Time (s)","Maintainence Cost ($)", "Energy Cost ($)"]
  
  with open(cost_file) as cost_f:
    cwr = csv.DictWriter(cost_f, fieldnames = keys)
    cwr.writeheader()
    for drone in drones:
      energy = [0,0,0]
      flight_time = [0,0,0]
      resting_time = [0,0,0]
      charging_time = [0,0,0]
      energy_cost = [0,0,0]
      m_var_cost = [0,0,0]
      for work in drone.works:
        if(work.status == 'T-L'):
          disp = [work.end_pos[i] - work.start_pos[i] for i in range(3)]
          time = work.end_time - work.start_time
          speed = ((disp[0]**2 + disp[1]**2 + disp[2]**2)**0.5) / time  
          asc_vel = disp[2] / time
          energy[work.day - 1] += (work.weight + drone.base_weight)*(drone.A + drone.B * speed + drone.C * (asc_vel if asc_vel>0 else 0))
          flight_time[work.day - 1] += time
        elif(work.status == 'T-E'):
          time = work.end_time - work.start_time
          speed = ((disp[0]**2 + disp[1]**2 + disp[2]**2)**0.5) / time  
          asc_vel = disp[2] / time
          energy[work.day - 1] += (drone.base_weight)*(drone.A + drone.B * speed + drone.C * (asc_vel if asc_vel > 0 else 0))
          flight_time[work.day - 1] += time
        elif(work.status[0] == 'C'):
          time = work.end_time - work.start_time
          charging_time[work.day - 1] += time
          if(work.status[2] == 'W'):
            X = int(work.status[4])
            energy_cost[work.day - 1] += wh[X - 1].current * time
          else:
            X = ord(work.status[4]) - ord('A') + 1
            energy_cost[work.day - 1] += rec[X - 1].current * time
            
        else:
          resting_time[work.day - 1] += work.end_time - work.start_time
      m_var_cost = [((flight_time[i])/3600)*drone.var_cost + drone.fixed_cost for i in range(3)]
      energy_cost = [consumed * ENERGY_COST for consumed in energy_cost]
      cwr.writerow({"DroneID":drone.drone_id,"Day":work.day,"Resting Time (s)":resting_time,"Charging Time (s)":charging_time,"Maintainence Cost ($)":m_var_cost, "Energy Cost ($)":energy_cost})
      