class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(chunk):
            if len(chunk) > 1:
                mid = len(chunk) // 2
                firstHalf = mergeSort(chunk[:mid])
                secondHalf = mergeSort(chunk[mid:])
            else:
                firstHalf = chunk
                secondHalf = []

            combined = []
            i, j = 0, 0
            while i < len(firstHalf) and j < len(secondHalf):
                if firstHalf[i] <= secondHalf[j]:
                    combined.append(firstHalf[i])
                    i+= 1
                else:
                    combined.append(secondHalf[j])
                    j += 1
            
            combined.extend(firstHalf[i:])
            combined.extend(secondHalf[j:])

            return combined
        
        return mergeSort(nums)


