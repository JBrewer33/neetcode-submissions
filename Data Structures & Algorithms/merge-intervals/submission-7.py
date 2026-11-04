class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals based on start time

        intervals.sort() #default is sort by first element

        ret = [] #new list for return

        #walk list with 2 pointers merging by adding to new list
        first = 0
        second = 1
        maxEnd = intervals[0][1]
        while second < len(intervals):
            #to determin if overlap, need: first end, second start
            #to create new interval if overlap need first start final end
            firstEnd = intervals[first][1]
            maxEnd = max(maxEnd, firstEnd)
            secondStart = intervals[second][0]
            
            #if current intervals dont overlap, add all previously overlaping intervals as new single interval, move pointers
            if maxEnd < secondStart:
                ret.append([intervals[first][0], maxEnd])
                first = second
            maxEnd = max(maxEnd, intervals[second][1])
            second += 1
        if first < len(intervals):
            ret.append([intervals[first][0], maxEnd])

        return ret