def threeNumberSum1(array, targetSum):
    # Sort the array in ascending order
    array.sort()

    # Create an empty list to store the triplets
    triplets = []

    # Iterate through the array until the third last element
    for i in range(len(array) - 2):
        # Initialize two pointers: 'left' starting from the next element and 'right' from the last element
        left = i + 1
        right = len(array) - 1

        # Continue until the left pointer is less than the right pointer
        while left < right:
            # Calculate the current sum of the values at i, left and right
            currentSum = array[i] + array[left] + array[right]

            # If the current sum equals the target sum, we've found a triplet
            if currentSum == targetSum:
                # Add the triplet to the list of triplets
                triplets.append([array[i], array[left], array[right]])
                # Move the left pointer one step to the right
                left +=1
                # Move the right pointer one step to the left
                right -= 1
            # If the current sum is less than the target sum, move the left pointer one step to the right to increase the sum
            elif currentSum < targetSum:
                left += 1
            # If the current sum is greater than the target sum, move the right pointer one step to the left to decrease the sum
            elif currentSum > targetSum:
                right -= 1      
    # Return the list of triplets
    return triplets




