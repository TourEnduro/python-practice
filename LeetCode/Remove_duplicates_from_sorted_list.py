nums = [int(x) for x in input().split()]

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            else:
                pass
        return i + 1

remDup = Solution()   
k = remDup.removeDuplicates(nums)
print(nums[0: k])