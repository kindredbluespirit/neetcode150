class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        
        first = nums[0]
        rest = nums[1:]

        subsets_rest = self.subsets(rest)

        subsets_rest_with_first = [[first] + subset for subset in subsets_rest]

        return subsets_rest + subsets_rest_with_first

## their solution
# def all_subsets_bitwise(lst):
#     n = len(lst)
#     return [[lst[j] for j in range(n) if (i & (1 << j))] for i in range(1 << n)]
