"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #if overlap imediatly return false
        #sort based on start time, walk list if overlap immediatly return
        intervals.sort(key=lambda x: x.start) #default sorts tuples based on first element, in this case start time

        for i in range(len(intervals) - 1):
            #if start2 < end1 
            if intervals[i+1].start < intervals[i].end:
                return False
        
        return True