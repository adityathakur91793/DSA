from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        arr = []

        for i in range(n):
            arr.append((score[i], i))
        arr.sort(reverse=True)

        ans = [""] * n

        for rank in range(n):
            original_index = arr[rank][1]

            if rank == 0:
                ans[original_index] = "Gold Medal"
            elif rank == 1:
                ans[original_index] = "Silver Medal"
            elif rank == 2:
                ans[original_index] = "Bronze Medal"
            else:
                ans[original_index] = str(rank + 1)

        return ans