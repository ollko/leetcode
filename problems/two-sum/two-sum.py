# Time complexity : O(n**2)
# Space complexity : O(1)

def twoSum(nums: List[int], target: int) -> List[int]:
    i = 0
    j = 1
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]