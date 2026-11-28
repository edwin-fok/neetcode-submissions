class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        ordered_nums = [item[0] for item in sorted(freq.items(), 
                            key = lambda item: item[1], reverse = True)]
        
        while (k > 0):
            res.append(ordered_nums[0])
            ordered_nums = ordered_nums[1:]
            k -= 1
        
        return res
