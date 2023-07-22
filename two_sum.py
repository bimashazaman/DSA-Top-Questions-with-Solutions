# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

# Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

# You can assume that there will be at most one pair of numbers summing up to the target sum.

# first solution

def twoNumberSum1(array, targetSum):
    nums = {}
    # The code snippet is using a dictionary (`nums`) to keep track of the numbers that have been
    # encountered so far in the array.
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num, num]
        else:
            nums [num] = True
    return []



# // another way in python

 def twoNumberSum2(array, targetSum):
    # The code snippet is using a nested loop to iterate through the array and check if any two
    # numbers in the array sum up to the target sum.
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]

    return []

# another one

def twoNumberSum3(array, targetSum):
    array.sort()
    
    left = 0
    right = len(array) - 1

  # The code snippet is implementing a two-pointer approach to find a pair of numbers in the array
  # that sum up to the target sum.
    
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]] 
        elif currentSum < targetSum:
            left += 1 
        elif currentSum > targetSum:
            right -= 1
    
    return []  # Return empty list when no pair is found

