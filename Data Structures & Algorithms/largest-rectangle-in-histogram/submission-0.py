class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][0]:
                height, idx = stack.pop()
                res = max(res, height * (i - idx)) 
                start = idx
            
            stack.append([heights[i], start])
        
        for height, idx in stack:
            res = max(res, height * (len(heights) - idx))

        return res