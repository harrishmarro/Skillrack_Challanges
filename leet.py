class Solution:
        def check(i,target,nums):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]==target:
                    l2.append(i)
                    l2.append(j)
                    return l2
        def twoSum(self, nums: list[int], target: int) -> list[int]:
                def __init__(self):
                    print(nums,target)
                    for i in range(len(nums)-1):
                        check(i,target,nums)
                        break
p=Solution([2,7,11,15],9)
print(p)

