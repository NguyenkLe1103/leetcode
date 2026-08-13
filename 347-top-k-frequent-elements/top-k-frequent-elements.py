class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums: 
            counts[num]= counts.get(num,0) + 1

        sort_counts = sorted(counts.items(), key= lambda x:x[1], reverse= True)
        
        top_k=  sort_counts[:k]
        

        result= []
        for key, num in top_k:
            result.append(key)
        return result