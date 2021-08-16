#
# PROBLEM: From an array find if the array
# has any duplicate elements and return in
# boolean
# array = [ 2, 2, 3, 4 ,5 ]

# SOLUTION:

data = [ 2, 2, 3, 4 ,5 ]

def problem_solution(data):
    num_dict = {}
    for element in data:
        if(element in num_dict):
            return True
        num_dict[element] = True
    return False

print(problem_solution(data))

# Time Complexity: O(N)

# Space Complexity: O(N)