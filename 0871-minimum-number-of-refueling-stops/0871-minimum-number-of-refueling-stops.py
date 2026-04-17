import heapq

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        max_heap = []
        fuel = startFuel
        i = 0
        n = len(stations)
        stops = 0
        
        while fuel < target:
            # Add all reachable stations
            while i < n and stations[i][0] <= fuel:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            
            # If no fuel options left
            if not max_heap:
                return -1
            
            # Refuel with best option
            fuel += -heapq.heappop(max_heap)
            stops += 1
        
        return stops