class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            
            for j in range(i + 1, len(nums)):
                # Check the condition:
                # If the sum of the numbers at indices 'i' and 'j' equals the target,
                # we have found our pair.
                if nums[i] + nums[j] == target:
                    
                    return [i, j]
