class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, height in enumerate(heights):
            while stack and height >= stack[-1][0]: stack.pop()
            stack.append([height, i])
        
        res = []
        for height, i in stack:
            res.append(i)
        return res
        