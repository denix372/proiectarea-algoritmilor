import math
import random

def get_total_distance(route: list[int], cities: list[tuple[float, float]]) -> float:
    dist = 0.0
    n = len(route)
    for i in range(n):
        x1, y1 = cities[route[i]]
        x2, y2 = cities[route[(i + 1) % n]] # Wrap around to the start
        dist += math.hypot(x1 - x2, y1 - y2)
    return dist

def simulated_annealing_tsp(cities: list[tuple[float, float]], 
                            temp: float = 1000.0, 
                            cooling_rate: float = 0.995, 
                            iterations: int = 2000) -> float:
    n = len(cities)
    
    # Start with a random route
    current_route = list(range(n))
    random.shuffle(current_route)
    current_dist = get_total_distance(current_route, cities)
    
    best_dist = current_dist
    
    for _ in range(iterations):
        # Generate a neighbor by swapping two random cities
        neighbor = current_route[:]
        i, j = random.sample(range(n), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        
        neighbor_dist = get_total_distance(neighbor, cities)
        
        # 1. If it's a better route, ALWAYS accept it (Hill Climbing logic)
        if neighbor_dist < current_dist:
            current_route = neighbor
            current_dist = neighbor_dist
            best_dist = min(best_dist, current_dist)
        
        # 2. If it's a WORSE route, accept it probabilistically (Simulated Annealing magic)
        else:
            acceptance_probability = math.exp((current_dist - neighbor_dist) / temp)
            if random.random() < acceptance_probability:
                current_route = neighbor
                current_dist = neighbor_dist
                
        # Cool down the system
        temp *= cooling_rate
        
    return best_dist


random.seed(42)
# Generate 20 random (x, y) coordinates representing cities
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(20)]

print(f"Optimized TSP Distance: {simulated_annealing_tsp(cities):.2f}")

'''
HEURISTIC SEARCH ANALYSIS & PROOF (Simulated Annealing)

A) Core Mathematical Idea (Thermodynamics in Algorithms):
   Hill Climbing fails in highly complex spaces because it gets permanently trapped 
   in "Local Minima" (a valley that looks like the lowest point locally, but isn't 
   the global lowest point).
   Simulated Annealing introduces a "Temperature" (T) variable. When evaluating a 
   worse state, it calculates an acceptance probability using the Boltzmann distribution:
   P = e^(-ΔE / T), where ΔE is the degradation in the cost function.

B) The Cooling Schedule:
   - High Temperature (Start of search): T is large, making ΔE / T close to 0, 
     and e^0 = 1. The algorithm accepts almost any worse move. It behaves like a 
     completely random walk, escaping any local minima easily.
   - Low Temperature (End of search): T approaches 0, making the exponent a large 
     negative number, meaning P approaches 0. The algorithm stops accepting worse 
     moves and behaves exactly like pure Hill Climbing, settling into the true 
     optimum of the valley it discovered.

C) Complexity (Metaheuristics):
   - Time Complexity: O(I), where I is the number of iterations. Since TSP is 
     NP-Hard (O(N!)), calculating exact paths for N=20 is impossible in real-time. 
     SA finds a near-optimal solution in constant time relative to the iteration limit.
   - Space Complexity: O(N) to store the route and neighbor states.
'''