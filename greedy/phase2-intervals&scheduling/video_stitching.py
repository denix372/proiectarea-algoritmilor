from typing import List
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        curr_end = 0
        next_end = 0
        count = 0
        i = 0
        n = len(clips)

        while curr_end < time:
            while i < n and clips[i][0] <= curr_end:
                next_end = max(next_end, clips[i][1])
                i += 1
            if next_end == curr_end:
                return -1
            count += 1
            curr_end = next_end
        return count
        

clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
time = 10
print(Solution().videoStitching(clips, time))