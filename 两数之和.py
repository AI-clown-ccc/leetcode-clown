class Solution:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind,num in enumerate(nums)://把nums录入哈希表,用哈希算法节省时间
            hashmap[num] = ind  //哈希[value] = key
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)//哈希.get获得key
            if j is not None and j!=i:
                return [i,j]
            

