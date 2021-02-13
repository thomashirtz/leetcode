class Solution:
    def merge(self, intervals):
        merged_intervals = []
        for interval in sorted(intervals, key=lambda x: x[0]):
            if merged_intervals and interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)
        return merged_intervals
