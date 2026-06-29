import time
from environment import DisasterGrid
from ai_engine import a_star_search, dijkstra_search # Import both
from logger import log_path

def reconstruct_path(came_from, start, goal):
    if goal not in came_from: return None
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# Run System
world = DisasterGrid()

# --- 1. Run A* (Your Main Model) ---
start_time = time.time()
path_data_a = a_star_search(world.grid, world.start, world.goal)
exec_time_a = time.time() - start_time
path_a = reconstruct_path(path_data_a, world.start, world.goal)
if path_a:
    log_path("A-Star Search", len(path_a), f"{exec_time_a:.6f}")

# --- 2. Run Dijkstra (Baseline Model) ---
start_time = time.time()
path_data_d = dijkstra_search(world.grid, world.start, world.goal)
exec_time_d = time.time() - start_time
path_d = reconstruct_path(path_data_d, world.start, world.goal)
if path_d:
    log_path("Dijkstra Baseline", len(path_d), f"{exec_time_d:.6f}")

print("Tests complete. Check performance_log.csv for data.")