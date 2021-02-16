class Solution:
    def insert(self, intervals, newInterval):
        start, end = newInterval[0], newInterval[1]
        left, merge, right = [], [], []
        for interval in intervals:
            if interval[1] < start:
                left.append(interval)
            elif interval[0] > end:
                right.append(interval)
            else:
                merge.append(interval)
        if merge:
            print(merge)
            start = min(start, merge[0][0])
            end = max([end] + [i[1] for i in merge])
        return left + [[start, end]] + right
