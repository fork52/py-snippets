class PrefixSum2D:
    """
    Data structure for querying a PrefixSums over 2d ranges.
    """
    def __init__(self, mat):
        n, m = len(mat), len(mat[0])
        self.n, self.m = n, m
        self.pre = pre = [ [0] * (m + 1) for _ in range(n + 1)]
        
        for r in range(n):
            for c in range(m):
                cur = mat[r][c]
                add1, add2 = pre[r][c + 1], pre[r + 1][c]
                sub = pre[r][c]
                pre[r + 1][c + 1] = cur + add1 + add2 - sub
        
    def query(self, r1 : int, c1 : int, r2 : int, c2 : int):
        """
        Query the sum of the 2D array in the inclusive range: (r1, c1) to (r2, c2).
        s = sum(mat[r][c] for r in range(r1, r2 + 1) for c in range(c1, c2 + 1))
        Constraints: r1 <= r2 and c1 <= c2
        """
        pre = self.pre
        add1, add2 = pre[r2 + 1][c2 + 1], pre[r1][c1]
        sub1, sub2 = pre[r2 + 1][c1], pre[r1][c2 + 1]
        return add1 + add2 - sub1 - sub2

