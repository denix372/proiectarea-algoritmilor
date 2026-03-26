
def is_sum_string(s):
    
    def back(i, sol):
        if i == len(s):
            # A valid sum-string must have at least 3 parts (num1 + num2 = num3)
            return len(sol) >= 3

        for j in range(i, len(s)):
            current_str = s[i:j + 1]

            # Rule: No leading zeroes allowed
            if len(current_str) > 1 and current_str[0] == '0':
                # If it starts with '0', making it longer will also start with '0'
                break 

            num = int(current_str)
            
            # If we already have 2 or more numbers, we must validate the sum
            if len(sol) >= 2:
                expected_sum = sol[-1] + sol[-2]
                
                if num > expected_sum:
                    # Pruning: The number is already too big. 
                    # Adding more digits will only make it bigger, so stop trying.
                    break 
                elif num < expected_sum:
                    # The number is too small. Continue the loop to add more digits.
                    continue 

            sol.append(num)
            
            if back(j + 1, sol):
                return True
    
            sol.pop()
            
        return False

    return back(0, [])

# optimized approach 
def solve2(s):
    n = len(s)

    # Helper function to check if the rest of the string follows the sum rule
    def check_sequence(remaining_str, num1, num2):
        # Base case: if we have successfully consumed the whole string
        if not remaining_str:
            return True
            
        # Calculate the next expected number
        num3 = num1 + num2
        str3 = str(num3)
        
        # If the remaining string starts with the expected sum
        if remaining_str.startswith(str3):
            # Recursively check the rest of the string
            return check_sequence(remaining_str[len(str3):], num2, num3)
            
        # If it doesn't match, this sequence is invalid
        return False

    # i represents the length of the first number
    for i in range(1, n):
        # j represents the end index of the second number
        for j in range(i + 1, n):
            
            str1 = s[0:i]
            str2 = s[i:j]
            
            # The prompt notes no leading zeroes. 
            # If a segment is longer than 1 character and starts with '0', skip it.
            if (len(str1) > 1 and str1[0] == '0') or (len(str2) > 1 and str2[0] == '0'):
                continue
                
            num1 = int(str1)
            num2 = int(str2)
            
            # Start validating from index j onwards
            if check_sequence(s[j:], num1, num2):
                return True
                
    return False

print(is_sum_string("12243660"))    # Output: True
print(is_sum_string("1111112223"))  # Output: True
print(is_sum_string("123456"))      # Output: False