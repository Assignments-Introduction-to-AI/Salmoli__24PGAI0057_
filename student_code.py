from expand import expand
import heapq
from collections import deque

visted = []
queue = []


def a_star_search(dis_map, time_map, start, goal):
    if start not in dis_map or goal not in dis_map:
        return None  # Invalid start or end landmark
    
    open_list = [(0, start, [])]  # Priority queue contains tuples of (estimated total cost, current landmark, path)
    closed_set = set()

    while open_list:
        estimated_cost, current, path = heapq.heappop(open_list)
        
        if current == goal:
            return path + [current]
        
        if current not in closed_set:
            closed_set.add(current)
            for neighbor, distance in dis_map[current].items():
                if neighbor not in closed_set and distance is not None:
                    travel_time = time_map[current][neighbor]
                    if travel_time is not None:
                        new_path = path + [current]
                        heapq.heappush(open_list, (estimated_cost + distance, neighbor, new_path))

    return None  # No path found
    
pass

def depth_first_search(time_map, start, end):
    if start not in time_map or end not in time_map:
        return None  # Invalid start or end landmark
    
    stack = [(start, [])]  # Stack contains tuples of (current landmark, path)
    visited = set()

    while stack:
        current, path = stack.pop()
        
        if current == end:
            return path + [current]
        
        if current not in visited:
            visited.add(current)
            for neighbor, travel_time in time_map[current].items():
                if neighbor not in visited and travel_time is not None:
                    stack.append((neighbor, path + [current]))

    return None  # No path found

def breadth_first_search(time_map, start, end):
    
    if start not in time_map or end not in time_map:
        return None  # Invalid start or end landmark
    
    queue = [(start, [])]  # Queue contains tuples of (current landmark, path)
    visited = set()

    while queue:
        current, path = queue.pop(0)
        
        if current == end:
            return path + [current]
        
        if current not in visited:
            visited.add(current)
            for neighbor, travel_time in time_map[current].items():
                if neighbor not in visited and travel_time is not None:
                    queue.append((neighbor, path + [current]))

    return None  # No path found