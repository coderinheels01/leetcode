"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequentCounter(self, nums: List[int], k: int) -> List[int]:
        return [num for num, count in Counter(nums).most_common(k)]
    
    def topKFrequentHeapQ(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return heapq.nlargest(k, count, key=count.get)
    
    def topKFrequentMinHeapSort(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num ))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]
    
    def topKFrequentMaxHeapSort(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))
        
        return [ heapq.heappop(heap)[1] for _ in range(k)]

    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) +1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        result = []

        for i in range(len(bucket)-1 , 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        
if __name__ == "__main__":
    s = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(f"top k - {k} frequent elementsfor nums {nums} using Counter are {s.topKFrequentCounter(nums, k)}")
    print(f"top k - {k} frequent elements for nums {nums} using heapq are {s.topKFrequentHeapQ(nums, k)}")
    print(f"top k - {k} frequent elements for nums {nums} using min heap sort are {s.topKFrequentMinHeapSort(nums, k)}")
    print(f"top k - {k} frequent elements for nums {nums} using min heap sort are {s.topKFrequentMaxHeapSort(nums, k)}")
    print(f"top k - {k} frequent elements for nums {nums} using min heap sort are {s.topKFrequentBucketSort(nums, k)}")


