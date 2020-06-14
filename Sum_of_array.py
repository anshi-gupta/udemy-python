### Return the sum of the numbers of the array, except ignore sections of numbers starting with a 6 and 
### extending to a next 9(every 6 will be followed by atleast one 9). Return 0 for no numbers.

# summer_69(1,3,5) -- 9
# summer_69(4, 5, 6, 7, 6, 7, 9, 8, 9, 4, 5, 7, 6, 1, 9, 1) -- 9
# summer_69(2,7,9,6,11) -- 14

def pattern_finder(nums):
    pattern_start = 6
    pattern_end = 9
    length_of_nums = len(nums)
    pattern_indices = list()

    i = 0
    while i < length_of_nums:
        num = nums[i]
        if num == 6:
            start_index = i
            index_to_start_from = start_index + 1
            for position in range(index_to_start_from, length_of_nums):
                current_num = nums[position]
                if current_num == 9:
                    end_index = position
                    pattern_indices.append((start_index, end_index))
                    i = end_index
                    break
        i += 1
    return pattern_indices

def sum_excluding_pattern(nums, pattern_positions):
    special_sum = 0
    for index in range(len(nums)):
        add_or_not = True
        for pattern_position in pattern_positions:
            pattern_position_start = pattern_position[0]
            pattern_position_end = pattern_position[1]
            if index >= pattern_position_start and index <= pattern_position_end:
                add_or_not = False
                break
        if add_or_not:
            special_sum += nums[index]


nums = [2,7,9,6,11, 9, 4, 5, 1, 6, 7, 1, 11, 9]
pattern_indices = pattern_finder(nums)
sum = sum_excluding_pattern(nums, pattern_indices)
print()