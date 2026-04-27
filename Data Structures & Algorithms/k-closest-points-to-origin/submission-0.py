class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use max heap with k elements to get k closest elements
        distances = []

        for point in points:
            heapq.heappush(distances, (-1 * math.sqrt(point[0]**2 + point[1]**2), point))
            k -= 1
            if k < 0:
                heapq.heappop(distances)
                k += 1
        
        return [point for distance, point in distances]