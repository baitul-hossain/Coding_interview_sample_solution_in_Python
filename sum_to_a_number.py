#
# PROBLEM: From an given array return two
# positions of number that sums up to a
# target number.
# array = [ 2, 5, 5, 7, 3 ], target = 10

# SOLUTION:

data = [ 2, 5, 5, 7, 3 ]
target = 10

def problem_solution(data, target):
    num_dict = {}
    data_length = len(data)
    for i in range(0, data_length):
        other_num = target - data[i]
        if(other_num in num_dict):
            return [num_dict[other_num], i]
        num_dict[data[i]] = i

print(problem_solution(data, target))

# Time Complexity: O(N)

# Space Complexity: O(N)