import math

def heuristic(a, b):
    
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Test the function: 
# Distance from (0,0) to (9,9) should be 18
print(f"Heuristic cost from (0,0) to (9,9) is: {heuristic((0,0), (9,9))}")