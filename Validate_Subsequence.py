# Validate Subsequence • ~

# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] , and so do the numbers [2, 4]. Note that a single number in an array and the array itself are both valid subsequences of the array.


#by while loop

def isValidSubsequence1(array, sequence):
    arrIdx = 0
    seqIdx = 0

    # The code is using a while loop to iterate through both the `array` and `sequence`
    # simultaneously. It checks if the element at the current index of `sequence` is equal to the
    # element at the current index of `array`. If they are equal, it increments `seqIdx` to move to
    # the next element in `sequence`. Regardless of whether the elements are equal or not, it always
    # increments `arrIdx` to move to the next element in `array`.
    while arrIdx < len(array) and seqIdx < len(sequence):
        if seqIdx[seqIdx] == array[arrIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)  

    
    
        
