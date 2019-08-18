# Time complexity : O(n**2)
# Space complexity : O(1)
import time
def twoSum(nums, target):
    t0 = time.clock()
    i = 0
    j = 1
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                t1 = time.clock()
                print('twoSum', t1-t0)
                return [i, j]


def twoSum2(nums, target):
    t0 = time.clock()
    h_table = { nums[i] : i for i in range(len(nums)) }
    for i in range(len(nums)):
        complement = target - nums[i]
        if h_table.get(complement) and h_table[complement] != i:
            t1 = time.clock()
            print('twoSum1', t1-t0)
            return [i, h_table[complement]]

def test():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert twoSum2([2, 7, 11, 15], 9) == [0, 1]
    return ("test pass")

print(test())