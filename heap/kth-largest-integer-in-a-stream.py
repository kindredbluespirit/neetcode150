## introducing heapq.minheap

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = nums
        heapq.heapify(self.q)

        ## max size k to hold k largest numbers
        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)

        while len(self.q) > self.k:
            heapq.heappop(self.q)
        
        return self.q[0]


## time limit exceeded for this solution for some reason

# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.nums = nums

#         self.q = []
#         for num in nums:
#             self.silentAdd(num)

#     def silentAdd(self, val: int) -> None:

#         if self.q == []:
#             self.q = [val]
#             return

#         start = 0
#         end = len(self.q)-1
#         mid = (start + end) // 2

#         if self.q[end] > val:
#             return
        
#         if val > self.q[start]:
#             self.q = [val] + self.q[:-1]
#             return

#         while True:
#             if start + 1 == end and self.q[start] >= val and val >= self.q[end]:
#                 self.q = q[:start+1] + [val] + self.q[end:-1]
#                 break

#             if self.q[start] > val and val > self.q[mid]:
#                 end = mid
#                 mid = (start + end)/2
#                 continue
            
#             if self.q[mid] > val and val > self.q[end]:
#                 start = mid
#                 mid = (start + end)/2
#                 continue

#     def add(self, val: int) -> int:
#         self.silentAdd(val)
#         return self.q[k-1]


## default
## initially n > k elements
## m elements added later
## sort first O(nlogn) time
## as m elements are added
## O(nlogn) time for each element
## O(m * nlogn) in total


