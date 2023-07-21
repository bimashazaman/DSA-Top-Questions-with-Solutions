// Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.

// Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.

// You can assume that there will be at most one pair of numbers summing up to the target sum.

// first solution

function twoNumberSum(array, targetSum) {
  let nums = {} // Initialize empty object

  for (let num of array) {
    let potentialMatch = targetSum - num
    if (nums[potentialMatch] !== undefined) {
      return [potentialMatch, num] // Return the two numbers
    } else {
      nums[num] = true // Add the current number to the object
    }
  }

  return [] // If no pair is found, return an empty array
}
