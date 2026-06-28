Disaster-Response-AI-System: Dynamic Disaster Coordination

## Project Overview
This project implements an AI-driven disaster response system designed to coordinate drone navigation in high-stakes, volatile disaster environments. The core of the system utilizes the **A* (A-Star) search algorithm** to find optimal paths from rescue depots to victim locations.

## Technical Approach: Informed Search
The project focuses on **Informed Search** techniques to solve the pathfinding problem. By using a heuristic-based approach, the A* algorithm evaluates the cost to reach a destination while navigating obstacles and dynamic environmental variables.

## Key Features
- **Informed Pathfinding:** Implements A* search with a custom heuristic to ensure efficient traversal through disaster zones.
- **Dynamic Re-planning:** Extends standard A* logic to handle real-time updates when paths become blocked (Reasoning under uncertainty).
- **Principled Design:** Modular architecture featuring a custom grid-based state representation for the disaster environment.
- **Experimental Evaluation:** Compares performance across various disaster intensity levels.

## Implementation Structure
- `environment.py`: Grid-based map representation with dynamic obstacle generation.
- `ai_engine.py`: A* search implementation (heuristic-based decision making).
- `interface.py`: Visualization tool to monitor drone pathfinding in real-time.
