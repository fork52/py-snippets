class MaxSegmentTree:
    identity: int = -(10**15)

    __slots__ = ('leftInd', 'rightInd', 'arr', 'nodeMax', 'left', 'right')

    def __init__(self, leftInd: int, rightInd: int, arr: int):
        self.leftInd = leftInd
        self.rightInd = rightInd
        self.arr = arr

        if self._isLeaf():
            self.nodeMax = arr[leftInd]
        else:
            mid = (leftInd + rightInd) >> 1
            self.left = MaxSegmentTree(leftInd, mid, arr)
            self.right = MaxSegmentTree(mid + 1, rightInd, arr)
            self._recalculate()

    def _isLeaf(self):
        return self.leftInd == self.rightInd

    def _recalculate(self):
        if self._isLeaf():
            return
        self.nodeMax = max(self.left.nodeMax, self.right.nodeMax)

    def pointUpdate(self, value, index):
        if self._isLeaf():
            self.nodeMax = value
            return

        if index <= self.left.rightInd:
            self.left.pointUpdate(value, index)
        else:
            self.right.pointUpdate(value, index)
        self._recalculate()

    def rangeQuery(self, l, r):
        if l <= self.leftInd <= self.rightInd <= r:
            return self.nodeMax
        elif r < self.leftInd or self.rightInd < l:
            return MaxSegmentTree.identity
        else:
            return max(self.left.rangeQuery(l, r), self.right.rangeQuery(l, r))
