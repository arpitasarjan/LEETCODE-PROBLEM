class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])
        shift = k % n
        if shift == 0:
            return True
        
        for row in mat:
            for j in range(n):
                if row[j] != row[(j + shift) % n]:
                    return False
        
        return True