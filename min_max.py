
def find_min(nums):
    temp_min = nums[0]
    for num in nums:
        if num < temp_min:
            temp_min, num = num, temp_min
    return temp_min


def find_max(nums):
    temp_max = nums[0]
    for num in nums:
        if num > temp_max:
            temp_max, num = num, temp_max
    return temp_max


my_list = [4, 2, 4, 0, 2, 4, 5, 7, 8, 9, 23, 8, 5, 4, 2, 2, 34, 4, 45]
min_value = find_min(my_list)
max_value = find_max(my_list)

print("Min & max value in the given list are {:d} & {:d} respectively.".format(min_value, max_value))
