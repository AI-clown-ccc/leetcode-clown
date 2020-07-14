class Solution:
    '''
    先对两个数组进行排序，分别同时遍历两个数组进行比较大小。
    '''
    """
Given two arrays, write a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1, length2 = len(nums1), len(nums2)

        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums2[index2] < nums1[index1]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1
        return intersection
