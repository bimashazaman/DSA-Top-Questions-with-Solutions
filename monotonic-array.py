def isMonotonic(array):
    # If the array has less than 2 elements, it's already monotonic
    # because a single number or no numbers at all can't violate the rule.
    if len(array) < 2:
        return True

    # Determine the initial direction by subtracting the first element from the second.
    # We subtract the first element from the second to handle the equal case.
    direction = array[1] - array[0]
    if direction > 0:  # non-decreasing, array is going up or flat
        direction = 1
    elif direction < 0:  # non-increasing, array is going down or flat
        direction = -1

    # Start iterating from the second index
    for i in range(2, len(array)):
        # If direction is still unknown, try to determine direction
        # from the current pair of elements
        if direction == 0:
            direction = array[i] - array[i - 1]
            if direction > 0:  # non-decreasing
                direction = 1
            elif direction < 0:  # non-increasing
                direction = -1

        # If the direction is known, check every pair of elements
        # for compliance with the determined direction
        else:
            # If the direction is non-decreasing (going up or flat)
            # and the next element is less than the current one,
            # it violates the monotonic property, so we return False
            if direction == 1 and array[i] < array[i - 1]:  # Violates non-decreasing
                return False

            # If the direction is non-increasing (going down or flat)
            # and the next element is greater than the current one,
            # it violates the monotonic property, so we return False
            elif direction == -1 and array[i] > array[i - 1]:  # Violates non-increasing
                return False

    # If we have gone through the entire array without returning False,
    # that means the array is monotonic, and we return True
    return True



def isMonotonic2(array):
    isNonI = True
    isNonD = True

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonD = False
        if array[i] > array[i - 1]:
            isNonI = False  

    return isNonD or isNonI

