from queue import PriorityQueue
import random
import math
import bisect
from line_plane_isect import isect_line_plane
from classes import Drone, DroneType, Zone

def process_zones(zones):
    global nfzs
    nfzs = []
    for zone in zones:
        nfz = ((zone.X[0],zone.Y[0],zone.Z[0]),(zone.X[7],zone.Y[7],zone.Z[7]))
        assert zone.X[0]<zone.X[7] and zone.Y[0]<zone.Y[7] and zone.Y[0]<zone.Y[7]
        nfzs.append(nfz)
        print(nfz)

    global nfzs_set
    nfzs_set = set(nfzs)
    global nfzs_bottom_left
    nfzs_bottom_left = [[],[],[]]
    global nfzs_top_right
    nfzs_top_right = [[],[],[]]
    for nfz in nfzs:
        for i in range(3):
            nfzs_bottom_left[i].append(nfz[0][i])
            nfzs_top_right[i].append(nfz[1][i])

    for i in range(3):
        nfzs_bottom_left[i] = sorted(nfzs_bottom_left[i])
        nfzs_top_right[i] = sorted(nfzs_top_right[i])

def get_dis(curr_point, end_point):
    return math.sqrt(abs(curr_point[0]-end_point[0])**2 + abs(curr_point[1]-end_point[1])**2 + abs(curr_point[2]-end_point[2])**2)

def get_h(curr_point, end_point):
    return 2*math.sqrt(abs(curr_point[0]-end_point[0])**2 + abs(curr_point[1]-end_point[1])**2 + abs(curr_point[2]-end_point[2])**2)

def isValid(point):
    global nfzs, nfzs_set, nfzs_bottom_left, nfzs_top_right
    bl_pos = [-1,-1,-1]
    tr_pos = [-1,-1,-1]
    for i in range(3):
        bl_pos[i] = bisect.bisect_right(nfzs_bottom_left[i], point[i])-1
        tr_pos[i] = bisect.bisect_left(nfzs_top_right[i], point[i])

    # print(f"{point} {bl_pos}")
    if -1 in bl_pos or -1 in tr_pos or len(nfzs_bottom_left[0]) in bl_pos or len(nfzs_top_right[0]) in tr_pos:
        return True

    nfz = ((nfzs_bottom_left[0][bl_pos[0]],nfzs_bottom_left[1][bl_pos[1]],nfzs_bottom_left[2][bl_pos[2]]), (nfzs_top_right[0][tr_pos[0]],nfzs_top_right[1][tr_pos[1]],nfzs_top_right[2][tr_pos[2]]))
    # print("NFZ - ", nfz)
    if nfz in nfzs_set:
        # print(point)
        return False

    return True

def is_between(point1, isect_point, point2):
    if abs(get_dis(point1,isect_point)+get_dis(point2,isect_point)-get_dis(point1,point2))<1e-6:
        # print(point1,isect_point,point2)
        return True
    return False

def is_inside(nfz, point):
    for i in range(3):
        if point[i]<nfz[0][i]:
            return False

    for i in range(3):
        if point[i]>nfz[1][i]:
            return False
    # print(point, nfz)
    return True

def check_los(point1, point2):
    global nfzs, nfzs_set, nfzs_bottom_left, nfzs_top_right
    dirs = [
        (1,0,0),
        (0,1,0),
        (0,0,1)
    ]
    for nfz in nfzs:
        for point in nfz:
            for dire in dirs:
                isect_point = isect_line_plane(point1, point2, point,dire)
                if isect_point is not None and is_inside(nfz,isect_point) and is_between(point1, isect_point, point2):
                    # print(isect_point)
                    # print(point1, point2)
                    return False

    return True

def get_path(start, end, want_path=False):
    global nfzs, nfzs_set, nfzs_bottom_left, nfzs_top_right
    pq = PriorityQueue()
    pq.put((get_dis(start,end), 0, start))

    dirs = []
    for i in (1,0,-1):
        for j in (1,0,-1):
            for k in (1,0,-1):
                if i != 0 or j != 0 or k != 0:
                    dirs.append((i,j,k))
    num_dir = len(dirs)
    dis = dict()
    dis[start] = 0
    parent = dict()
    parent[start] = start
    iterations = 0

    while pq.qsize()>0:
        iterations+=1
        if iterations>1000000:
            print("Too many iterations in theta* pathfinding.")
            break
        curr_point_info = pq.get()
        curr_point = curr_point_info[2]

        # print(f'{curr_point} {curr_point_info[0]}')
        # if dis[curr_point]<curr_point_info[1]:
        #     print("Skipping",curr_point)
        #     continue 
        if curr_point == end:
            break
        
        if check_los(curr_point, end):
            dis[end] = dis[curr_point]+get_dis(curr_point,end)
            parent[end] = curr_point
            break

        for i in range(num_dir):
            jumpx = 1
            jumpy = 1
            jumpz = 1
            # jumpx = max(1,abs(curr_point[0]-end[0])//10)
            # jumpy = max(1,abs(curr_point[1]-end[1])//10)
            # jumpz = max(1,abs(curr_point[2]-end[2])//10)

            new_point = (curr_point[0]+dirs[i][0]*jumpx,curr_point[1]+dirs[i][1]*jumpy,curr_point[2]+dirs[i][2]*jumpz)
            if isValid(new_point):
                if new_point not in dis:
                    if check_los(new_point, parent[curr_point]):
                    # if False:
                        parent[new_point] = parent[curr_point]
                        dis[new_point] = dis[parent[curr_point]] + get_dis(new_point,parent[curr_point])
                        pq.put((get_h(new_point,end)+dis[new_point],-dis[new_point],new_point))
                        # pq.put((get_dis(new_point,end)+dis[new_point],0,new_point))
                    else:
                        dis[new_point] = dis[curr_point] + get_dis(new_point,curr_point)
                        pq.put((get_h(new_point,end)+dis[new_point],-dis[new_point],new_point))
                        # pq.put((get_dis(new_point,end)+dis[new_point],0,new_point))
                        parent[new_point] = curr_point

    if not want_path:
        return dis[end]

    node = end
    path = []
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    return dis[end], path

def get_min_time_helper(start, end, drone, weight):
    total_weight = drone.base_weight+weight
    f = weight/drone.payload_weight_cap
    xy_speed = drone.max_speed - drone.P*f
    z_up_speed = drone.max_speed - drone.Q*f
    z_down_speed = drone.max_speed + drone.Q*f
    xy_dis = get_dis((start[0],start[1],0),(end[0],end[1],0))
    z_dis = abs(start[2]-end[2])
    z_speed = z_up_speed
    if z_dis<0:
        z_speed = z_down_speed
    req_time = max(z_dis/z_speed, xy_dis/xy_speed)
    return req_time

def get_min_time(start, end,drone, weight):
    if check_los(start,end):
        return get_min_time_helper(start, end, drone, weight)
    req_time = 0
    path = get_path(start, end, )

if __name__ == "__main__":
    start = (0,0,0)
    end = (2068,1149,56)

    zz = [
        ((1,1,1),(1000,1000,1000))
        ]

    zones = []
    for z in zz:
        zone = Zone()
        zone.X[0]=z[0][0]
        zone.Y[0]=z[0][1]
        zone.Z[0]=z[0][2]
        zone.X[7]=z[1][0]
        zone.Y[7]=z[1][1]
        zone.Z[7]=z[1][2]
        zones.append(zone)

    process_zones(zones)

    dis, path = get_path(start, end, True)
    print(dis)
    print(path)