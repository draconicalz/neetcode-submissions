class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        all = set()
        srcs = set()
        for src, dest in paths:
            all.add(src)
            all.add(dest)
            srcs.add(src)
        
        for city in all:
            if city not in srcs: return city
