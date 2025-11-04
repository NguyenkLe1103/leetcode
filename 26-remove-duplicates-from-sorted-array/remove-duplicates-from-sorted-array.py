class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  #check for empty array
            return 0
        j = 0  #pointer for unique element 

        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j +=1
                nums[j]= nums[i]
        return j + 1