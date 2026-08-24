class CountSquares:

    def __init__(self):
        self.squareMap = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.squareMap[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        total = 0
        px, py = point
        for x, y in self.squareMap:
            dist1, dist2 = abs(px - x), abs(py - y)
            if dist1 == 0 or dist2 == 0: continue
            elif dist1 == dist2:
                if (px, y) in self.squareMap and (x, py) in self.squareMap:
                    total += (self.squareMap[(px,y)] * self.squareMap[(x, py)] * self.squareMap[(x, y)])
        return total
