def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    #[1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
    #[10, 12, 13, 14, 17, 18, 26, 30, 31, 32]

    idx1 = 0
    idx2 = 0

    small = float('inf')
    curr =  float('inf')
    smpair = []

    while idx1 < len(arrayOne) and idx2 < len(arrayTwo):
         num1 = arrayOne[idx1]
         num2 = arrayTwo[idx2]

            if num1 < num2:
                curr = num2 - num1
                idx1 += 1
            elif num2 < num1:
                curr = num1 - num2
                idx2 += 1
            else:
                return [num1, num2]

            if small > curr:
                small = curr
                smpair = [num1, num2]

    return smpair

# Time: O(nlog(n) + mlog(m)) | Space: O(1)

