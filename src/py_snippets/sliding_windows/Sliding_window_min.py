from collections import deque

class MinQueue:
    def __init__(self, arr):
        self.q = deque()
        self.nums = arr

    def push_back(self, ind):
        """Adds element at `ind` into the queue."""
        q, nums = self.q, self.nums
        cur = nums[ind]
        while q and nums[q[-1]] >= cur:
            q.pop()
        q.append(ind)

    def pop_front(self, ind):
        """ 
        Removes all elements in the current window which come before `ind`.
        Also, removes `ind`.
        """
        q = self.q
        while q and q[0] <= ind:
            q.popleft()

    def get_min(self):
        """ Returns the min element in the current window"""
        return self.nums[self.q[0]]


nums = [15, 5, 10, 17, 20, 100, 17, 2, 8, 16]
n = len(nums)
k = min(n, 3)


if __name__ == '__main__':
    mnq = MinQueue(nums)

    # ans[i] stores min element in the window nums[i:i+k]
    ans = [] 
    for i in range(k):
        mnq.push_back(i)

    ans.append(mnq.get_min())

    for i in range(k, n):
        mnq.pop_front(i - k)
        mnq.push_back(i)

        ans.append(mnq.get_min())

    print(*ans)
