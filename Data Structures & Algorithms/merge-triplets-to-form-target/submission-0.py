class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        curTriplet = None
        # for every triplet
        for triplet in triplets:
            
            # check if it is valid (no elements greater than target)
            valid = True
            for i in range(len(triplet)):
                if triplet[i] > target[i]:
                    valid = False
                    break

            # update our curTriplet if valid
            if valid and curTriplet == None:
                curTriplet = triplet
            elif valid:
                curTriplet = [max(curTriplet[0], triplet[0]),
                              max(curTriplet[1], triplet[1]), 
                              max(curTriplet[2], triplet[2])]
            
            # if we find it, True
            if curTriplet == target:
                return True
        
        # if we cant reach it, False
        return False


