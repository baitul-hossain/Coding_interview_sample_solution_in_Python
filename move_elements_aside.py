#
# QUESTION:
# Given an array of integers, write a function to
# move all 0´s to the end while maintaining the
# relative order of the other elements
# [ 0, 1, 0, 3, 2, 5 ]

# SOLUTION:

data = [ 0, 1, 0, 3, 2, 5 ]

def problem_solution(array):

    i = 0
    j = len(array)
    for element in array:
        if(element != 0):
            array[i] = element
            i += 1
    for k in range(i, j):
        array[k] = 0

    return array

print(problem_solution(data))


# Time Complexity = O(N)

# Space Complexity = O(1)

