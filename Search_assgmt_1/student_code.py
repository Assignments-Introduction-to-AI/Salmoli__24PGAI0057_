##   Using Heapify

# from expand import expand
# import heapq
# from collections import deque

# visted = []
# queue = []


# def a_star_search(dis_map, time_map, start, goal):
#     if start not in dis_map or goal not in dis_map:
#         return None  # Invalid start or end landmark
    
#     open_list = [(0, start, [])]  # Priority queue contains tuples of (estimated total cost, current landmark, path)
#     closed_set = set()

#     while open_list:
#         estimated_cost, current, path = heapq.heappop(open_list)
        
#         if current == goal:
#             return path + [current]
        
#         if current not in closed_set:
#             closed_set.add(current)
#             for neighbor, distance in dis_map[current].items():
#                 if neighbor not in closed_set and distance is not None:
#                     travel_time = time_map[current][neighbor]
#                     if travel_time is not None:
#                         new_path = path + [current]
#                         heapq.heappush(open_list, (estimated_cost + distance, neighbor, new_path))

#     return None  # No path found
    
# pass

# def depth_first_search(time_map, start, end):
#     if start not in time_map or end not in time_map:
#         return None  # Invalid start or end landmark
    
#     stack = [(start, [])]  # Stack contains tuples of (current landmark, path)
#     visited = set()

#     while stack:
#         current, path = stack.pop()
        
#         if current == end:
#             return path + [current]
        
#         if current not in visited:
#             visited.add(current)
#             for neighbor, travel_time in time_map[current].items():
#                 if neighbor not in visited and travel_time is not None:
#                     stack.append((neighbor, path + [current]))

#     return None  # No path found

# def breadth_first_search(time_map, start, end):
    
#     if start not in time_map or end not in time_map:
#         return None  # Invalid start or end landmark
    
#     queue = [(start, [])]  # Queue contains tuples of (current landmark, path)
#     visited = set()

#     while queue:
#         current, path = queue.pop(0)
        
#         if current == end:
#             return path + [current]
        
#         if current not in visited:
#             visited.add(current)
#             for neighbor, travel_time in time_map[current].items():
#                 if neighbor not in visited and travel_time is not None:
#                     queue.append((neighbor, path + [current]))

#     return None  # No path found




##Using Priority Queue

from expand import expand
from queue import PriorityQueue

def a_star_search(dis_map, time_map, start, end):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    count = 1
    while not frontier.empty():
        current = frontier.get()[1]
        if end == current:
            break
        counter = False
        children = expand(current, time_map)
        for next in children:
            new_cost = cost_so_far[current] + time_map[current][next]
            if (next not in cost_so_far or new_cost < cost_so_far[next]): # or (new_cost == cost_so_far[next] and dis_map[next][end] < hn):
                cost_so_far[next] = new_cost
                priority = new_cost + dis_map[next][end]
                frontier.put((priority, next))
                came_from[next] = current


    path = []
    node = end
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()
    # print(path)
    return path


# Right to Left Path
def depth_first_search(time_map, start, end):
    found = False
    stack = [start]
    parents = {}
    
    while stack:
        node = stack.pop()
        if node == end:
            found = True
            break
        
        children = expand(node, time_map)
            
        for child in reversed(children):
            stack.append(child)
            parents[child] = node
    
    path = [end]
    
    if found:
        # Traverse back through the parent nodes for the path
        while node != start:
            path.insert(0, parents[node])
            node = parents[node]

    return path    


def breadth_first_search(time_map, start, end):
	found = False
	visited = []
	queue = [start]
	parents = {}
	while queue:
		node = queue.pop(0)
		if node == end:
			found = True
			break
		if node not in visited:
			visited.append(node)
			children = expand(node, time_map)
			for child in children:
				if child not in visited:
					queue.append(child)
					parents[child] = node
	path = [end]
	if found == True:
		node = end
		# Traverse back through the parent nodes for the path
		while (node != start):
			path.insert(0, parents[node])
			node = parents[node]
	return path