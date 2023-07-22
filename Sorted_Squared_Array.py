# Sorted Squared Array • I

# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order.


def sorted_squared_array(array):
    squared = [number ** 2 for number in array]
    squared.sort()
    return squared



#brutforce solution

#O(nlogn) time | O(N) space

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()   
    return sortedSquares



#thirtd solution
def sortedSquaredArray3(array):
    sortedSquares = [0 for _ in array] #initializing with all 0
    smallValueIdx = 0 # first element
    largeValueIdx = len(array) - 1 #last element

    for idx in reversed(range(len(array))):
        smallValue = array[smallValueIdx] #assigining to the first element of the array
        largeValue = array[largeValueIdx] # ASSIGN The last one

        if abs(smallValue) > abs(largeValue):
            sortedSquares[idx] = smallValue * smallValue
            smallValueIdx += 1
        else:
            sortedSquares[idx] = largeValue * largeValue
            largeValueIdx -= 1

    return sortedSquares     