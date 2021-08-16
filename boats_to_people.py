#
# PROBLEM: Given an array of people weight and
# and integer as limit capacity of each boat,
# return the minimum number of boats to carry
# all people.
# Weight = [ 2, 1, 3, 2], limit = 2

# SOLUTION:

data = [ 2, 1, 3, 2]
limit = 2

def problem_solution(data, limit):
    data.sort()
    left_point = 0
    right_point = len(data) - 1
    boat_need = 0

    while(left_point <= right_point):
        if(left_point == right_point):
            boat_need += 1
            break
        if(data[left_point] + data[right_point] <= limit):
            left_point += 1
        right_point -= 1

    return boat_need

print(problem_solution(data, limit))

# Time Complexity: O( N Log(N) )

# Space Complexity: O(N)