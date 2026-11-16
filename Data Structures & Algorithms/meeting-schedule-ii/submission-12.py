"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from bisect import bisect_left, bisect_right
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        starts = []
        ends = []

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()
        print(str(starts))
        print(str(ends))
        startptr = 0
        endptr = 0
        rooms = 0
        maxRooms = 0
        while startptr < len(starts):
            if starts[startptr] < ends[endptr]:
                rooms += 1
                maxRooms = max(maxRooms, rooms)
                startptr += 1
            else:
                endptr += 1
                rooms -= 1


            
        
        return maxRooms