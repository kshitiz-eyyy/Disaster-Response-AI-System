import heapq

def heuristic(a, b):
    # Manhattan distance for A*
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            return came_from
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_node = (current[0] + dx, current[1] + dy)
            if 0 <= next_node[0] < 10 and 0 <= next_node[1] < 10:
                if grid[next_node[1]][next_node[0]] != 1:
                    new_cost = cost_so_far[current] + 1
                    if next_node not in cost_so_far or new_cost < cost_so_far.get(next_node, float('inf')):
                        cost_so_far[next_node] = new_cost
                        # A* uses heuristic to guide the search
                        priority = new_cost + heuristic(next_node, goal)
                        heapq.heappush(open_list, (priority, next_node))
                        came_from[next_node] = current
    return came_from

def dijkstra_search(grid, start, goal):
    """Baseline: Search without a heuristic (Blind Search)"""
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            return came_from
            
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_node = (current[0] + dx, current[1] + dy)
            if 0 <= next_node[0] < 10 and 0 <= next_node[1] < 10:
                if grid[next_node[1]][next_node[0]] != 1:
                    new_cost = cost_so_far[current] + 1
                    if next_node not in cost_so_far or new_cost < cost_so_far.get(next_node, float('inf')):
                        cost_so_far[next_node] = new_cost
                        # Dijkstra uses ONLY cost (no heuristic)
                        priority = new_cost
                        heapq.heappush(open_list, (priority, next_node))
                        came_from[next_node] = current
    return came_from