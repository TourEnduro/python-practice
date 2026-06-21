nums = [int(x) for x in input().split()]
val = int(input())

class Solution:
    def removeElement(self, nums):
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == val:
                nums.pop(j)
            else:
                pass
        return len(nums)
    

remEl = Solution()   
k = remEl.removeElement(nums)
print(nums[0: k])