import sys
import math
import heapq
from collections import Counter


def findPath(start_idx, end_idx, cannons):
    points = [start_idx, end_idx] + cannons

    graph = [[] for _ in range(len(points))]

    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                dist = getDist(points[i], points[j])
                if i >= 2:
                    time = getCannonTime(dist)
                else:
                    time = getRunningTime(dist)

                graph[i].append((j, time))

    min_time = [float('inf')] * len(points)
    min_time[0] = 0
    priority_queue = [(0, 0)]

    while priority_queue:
        current_time, start_idx = heapq.heappop(priority_queue)

        if start_idx == 1:
            return current_time

        if current_time > min_time[start_idx]:
            continue

        for end_idx, travel_time in graph[start_idx]:
            new_time = current_time + travel_time
            if new_time < min_time[end_idx]:
                min_time[end_idx] = new_time
                heapq.heappush(priority_queue, (new_time, end_idx))

    return min_time[1]


def getDist(start, end):
    return math.sqrt(math.pow(start[0] - end[0], 2) + math.pow(start[1] - end[1], 2))


def getRunningTime(distance):
    return distance / 5


def getCannonTime(distance):
    if distance >= 50:
        return 2 + getRunningTime(distance - 50)
    elif distance >= 30:
        return 2 + getRunningTime(50 - distance)
    else:
        return getRunningTime(distance)


start = (25.0, 100.0)
end = (190.0, 57.5)
cannons = [
    (125.0, 67.5),
    (75.0, 125.0),
    (45.0, 72.5),
    (185.0, 102.5)
]

result = findPath(start, end, cannons)
print(result)

# lines = [line for line in sys.stdin]

# start, end = [float(val) for val in lines[0].split()], [float(
#     val) for val in lines[1].split()]
# cannons = []
# for i in range(int(lines[2])):
#     cannons.append([float(val) for val in lines[3 + i].split()])

# result = findPath(start, end, cannons)
# print(result)
