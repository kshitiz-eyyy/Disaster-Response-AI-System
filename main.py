import time
from environment import DisasterGrid
from ai_engine import a_star_search
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
print("Initial Disaster Grid Map:")
world.display()

start_time = time.time()
path_data = a_star_search(world.grid, world.start, world.goal)
path = reconstruct_path(path_data, world.start, world.goal)
exec_time = time.time() - start_time

if path:
    print(f"\nInitial Path: {path}")
    log_path("Static Test", len(path), f"{exec_time:.4f}")

# Dynamic Update
print("\n--- SENSOR UPDATE: New obstacle detected at (0, 5)! ---")
world.add_obstacle(0, 5)
world.display()

start_time = time.time()
new_path_data = a_star_search(world.grid, (0, 4), world.goal)
new_path = reconstruct_path(new_path_data, (0, 4), world.goal)
exec_time = time.time() - start_time

if new_path:
    print(f"New Path: {new_path}")
    log_path("Dynamic Test", len(new_path), f"{exec_time:.4f}")