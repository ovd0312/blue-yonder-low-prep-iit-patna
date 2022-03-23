import pandas as pd
import classes as cl


def drone_path_output(drones):  # drones is a list of Drone objects

    total_output = []

    for drone in drones:
        drone_id = 'D' + str(drone.drone_type) + drone.drone_id

        i = 0
        sz = len(drone.instruction_set)  # drone.instruction_set is a list of Work objects

        while i < sz:

            instruction = drone.instruction_set[i]

            start = instruction.start_time
            end = instruction.end_time

            if start == end:
                total_time = 1
            else:
                total_time = end - start

            j = start
            while j <= end:
                output = []
                output.append(instruction.demand_id)
                output.append(drone_id)
                output.append('Day ' + str(instruction.day))
                output.append(j + 1)
                x = instruction.start_pos[0] + ((j - start) / total_time) * (
                        instruction.end_pos[0] - instruction.start_pos[0])
                y = instruction.start_pos[1] + ((j - start) / total_time) * (
                        instruction.end_pos[1] - instruction.start_pos[1])
                z = instruction.start_pos[2] + ((j - start) / total_time) * (
                        instruction.end_pos[2] - instruction.start_pos[2])
                output.append(x)
                output.append(y)
                output.append(z)
                output.append(instruction.status)
                output.append(instruction.speed)
                output.append(instruction.energy_consumed)
                output.append(instruction.energy_cost)
                output.append(instruction.total_weight)
                total_output.append(output)

                j += 1

            i += 1

    headers = ['Demand ID', 'DroneID', 'Day', 'Time (in seconds)', 'X', 'Y', 'Z', 'Activity', 'Speed (m/s)',
               'mAH Consumed', 'Energy Cost (c X mA)', 'Total Weight (kgs)']

    data = pd.DataFrame(total_output, columns=headers)
    data.to_csv('DronePath_Output.csv', index=False)
