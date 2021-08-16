#
# PROBLEM: Find the length of the longest
# substring, note: no repeating characters
# string = abcaabcdaabcef

# SOLUTION:

data = "abcaabcdaabcef"

def problem_solution(data):
    char_dict = {}
    left_point = 0
    right_point = 0
    substring_length = 0
    datastring_length = len(data)

    while(left_point < datastring_length and right_point < datastring_length):
        element = data[right_point]
        if(element in char_dict):
            left_point = max(left_point, char_dict[element]+1)
        char_dict[element] = right_point
        substring_length = max(substring_length, right_point - left_point + 1)
        right_point += 1

    return substring_length

print(problem_solution(data))


# Time Complexity: O(N)

# Space Complexity: O(N)