import numpy as np
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ms=np.array(matrix)
        msx=ms.flatten()
        msx.sort()
        return msx[k-1]