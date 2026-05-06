# creating a class. Why do we need a class here?
class Solution:
    # defining a function to search through the given List
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating a Dictionary to store already checked values
        hashmap = {}
        # making a searching loop in a range of given indexes in on a list
        for i in range(len(nums)):
            # creating a variable for defining a commplementary value to our current number
            complement = target - nums[i]
            # if there is one -> we write down its index as a second one into the dictinary, that would be our solution
            if complement in hashmap:
                return [i, hashmap[complement]]
            # writing down a Key and a Value into the Dictinary, to be sure, which values we already checked
            hashmap[nums[i]] = i
        # Return an empty list if no solution is found
        return []