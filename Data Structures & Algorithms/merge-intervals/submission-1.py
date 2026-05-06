#first thoughts, if intervals are sorted by start then we know they're overlapping if i end is > i+1start
#merge by making new interval with i start and i+1 end
#should be able to do in O(n) time since we only need one iteration
#it should be possible to do all in place but the implementation is going to be a bit tricky when merging so going to first
#do with a new list
#issues with ^ when merging, thinking a 2 pointer/sliding window will be better

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        ret = [intervals[0]]

        for start, end in intervals:
            lastEnd = ret[-1][1]

            if start <= lastEnd:
                ret[-1][1] = max(lastEnd, end)
            else:
                ret.append([start, end])


        return ret