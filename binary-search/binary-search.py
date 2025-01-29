class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ## recursive method
        ## O(1) memory if list is called by reference, O(nlogn) if called by value
        ## O(log n) time
        # l = len(nums)

        # if l == 0 or target < nums[0] or target > nums[-1]:
        #     return -1
        
        # if l == 1 and target in nums:
        #     return 0
        
        # mid = l // 2

        # i = self.search(nums[:mid], target)

        # if i != -1:
        #     return i
        
        # i = self.search(nums[mid:], target)
        # if i != -1:
        #     return mid + i
        
        # return -1
        

        ## iterative method
        ## O(1) memory
        ## O(log n) time
        queue = [(0, len(nums))]
        while len(queue) > 0:
            pair = queue[0]
            queue = queue[1:]

            start = pair[0]
            end = pair[1]

            # if start == end:
            if start >= end:
                continue
            
            if end - start == 1:
                if nums[start] == target:
                    return start
                else:
                    continue
            
            ## end - start > 1
            mid = (start + end) // 2

            queue += [(start, mid), (mid, end)]
        
        return -1
