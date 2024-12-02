class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_present = set()
        for num in nums:
            if num in nums_present:
                return True
            nums_present.add(num)
        return False
