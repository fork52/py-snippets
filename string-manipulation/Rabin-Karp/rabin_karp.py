from functools import cache
from dataclasses import dataclass

@cache
def get_power(exp):
    ans = 1
    cur_power = MUL
    while exp:
        if exp & 1:
            ans = (ans * cur_power) % P
        cur_power = (cur_power * cur_power) % P
        exp = exp >> 1
    return ans


MUL = 31  # 31 or 37 are recommended
P = 10**9 + 7  # Very Large Prime Number

@dataclass(slots = True)
class RabinKarp:
    length: int = 0
    hash: int = 0

    def push_back(self, c):
        val = ord(c) - 96
        self.length += 1
        self.hash = (self.hash * MUL) % P
        self.hash = (self.hash + val) % P

    def pop_front(self, c):
        val = ord(c) - 96
        subtract = (val * get_power(self.length - 1)) % P
        self.hash = (self.hash - subtract) % P
        self.length -= 1
