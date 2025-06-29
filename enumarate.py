def twoSum(nums, target):
    
    num_map = {}  #to store number

    for i, num in enumerate(nums):

        print("Index:", i, "Value:", num)

        complement = target - num
        # calculate what number would complete the pair

        if complement in num_map:
        # if that number has already been seen(stored in num_map)
        # return is index and the current index 

            return [num_map[complement], i]
        
        num_map[num] = i



nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))


#  enumerate adds a counter(index) to an iterable like list
# so you get both the index and the items at the same time in a loop