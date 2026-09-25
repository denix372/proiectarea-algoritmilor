def objective_function(x: float) -> float:
    # A simple parabola opening downwards: f(x) = -x^2 + 5
    # The mathematical global maximum is at x = 0, where f(0) = 5.
    return -(x ** 2) + 5

def hill_climbing_math(initial_x: float, step_size: float = 0.1, max_iterations: int = 100) -> tuple[float, float]:
    current_x = initial_x
    current_val = objective_function(current_x)
    
    for i in range(max_iterations):
        # Generate neighboring states by taking a small step left and right
        left_x = current_x - step_size
        right_x = current_x + step_size
        
        left_val = objective_function(left_x)
        right_val = objective_function(right_x)
        
        # Steepest-Ascent logic: Find the best move among neighbors
        best_next_x = current_x
        best_next_val = current_val
        
        if left_val > best_next_val:
            best_next_x = left_x
            best_next_val = left_val
            
        if right_val > best_next_val:
            best_next_x = right_x
            best_next_val = right_val
            
        # Termination condition: If neither neighbor is better, we reached the peak
        if best_next_val == current_val:
            break
            
        # Move to the better state
        current_x = best_next_x
        current_val = best_next_val
        
    # Rounding to 4 decimal places for clean output
    return round(current_x, 4), round(current_val, 4)

initial_guess = 2.0
best_x, best_value = hill_climbing_math(initial_guess)

print(f"Starting x: {initial_guess}")
print(f"Algorithm converged at: x = {best_x}, f(x) = {best_value}")

'''
HEURISTIC SEARCH ANALYSIS & PROOF (Continuous Hill Climbing)

A) Core Mathematical Idea (State Generation in Continuous Spaces):
   Unlike discrete problems (like arrays or chessboards) where neighbors are 
   obvious (index + 1), in continuous mathematical functions, there are infinitely 
   many neighbors. We discretize the space using a 'step_size' (e.g., 0.1). 
   The algorithm evaluates f(x - step_size) and f(x + step_size) and always 
   moves in the direction that increases the function's value (Steepest Ascent).

B) The Role of Step Size (Learning Rate equivalent in ML):
   - If step_size is too small: The algorithm takes too long to converge 
     and might run out of iterations.
   - If step_size is too large: The algorithm might completely step over the 
     peak and bounce back and forth without ever settling on the exact maximum.
   - Advanced algorithms (like Gradient Descent in Neural Networks) dynamically 
     reduce the step size as they get closer to the peak.

C) Landscape Limitations:
   Because f(x) = -x^2 + 5 has only one peak, Hill Climbing perfectly finds the 
   Global Maximum. However, if the function was wavy (like sin(x)), the climber 
   would stop at the first crest it finds (a Local Maximum), utterly oblivious 
   to taller peaks further away.
'''