class FenwickTree:
    def __init__(self, nums: List[int]):
        self.n = n = len(nums) + 1
        self.fenwick = fenwick = [0] * self.n
        for i in range(1, n):
          fenwick[i] += nums[i - 1]
          parent = i + (i & -i)
          if parent < n:
            fenwick[parent] += fenwick[i]

    def pointAdd(self, index: int, delta: int) -> None:
        fenwick, n = self.fenwick, self.n
        while index < n:
          fenwick[index] += delta
          index += index & -index
    
    def rangeSum(self, index: int) -> int:
        fenwick = self.fenwick
        total = 0
        while index > 0:
          total += fenwick[index]
          index -= index & -index
        return total
