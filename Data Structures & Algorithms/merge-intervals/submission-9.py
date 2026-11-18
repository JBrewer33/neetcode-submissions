class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda pair: pair[0])
        ret = [intervals[0]]

        for start, end in intervals:
            lastEnd = ret[-1][1] #largest end in ret list

            if start <= lastEnd:
                ret[-1][1] = max(lastEnd, end) #if start is before or equal to current largest (mergable) update largest end if end is larger
            else:
                ret.append([start, end]) #else add new interval

        return ret