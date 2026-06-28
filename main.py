from environment import DisasterGrid
from ai_engine import a_star_search

def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return None 
    
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# 1. Initialize
world = DisasterGrid()
print("Initial Disaster Grid Map:")
world.display()

# 2. Run initial A*
path_data = a_star_search(world.grid, world.start, world.goal)
path = reconstruct_path(path_data, world.start, world.goal)
print(f"\nInitial Path: {path}")

# 3. DYNAMIC UPDATE: Simulate uncertainty
# Let's say an obstacle appears at (0, 5) while the drone is working
print("\n--- SENSOR UPDATE: New obstacle detected at (0, 5)! Re-planning... ---")
world.add_obstacle(0, 5) 
world.display()

# 4. Re-calculate path from the current position (e.g., assuming drone is at 0, 4)
new_start = (0, 4) 
new_path_data = a_star_search(world.grid, new_start, world.goal)
new_path = reconstruct_path(new_path_data, new_start, world.goal)

if new_path:
    print(f"New Path found: {new_path}")
else:
    print("No path found: The goal is unreachable!")