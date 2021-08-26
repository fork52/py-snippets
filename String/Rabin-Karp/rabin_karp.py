from functools import cache

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

MUL = 31         # 31 or 37 are recommended
P = 10 ** 9 + 7  # Very Large Prime Number
class RabinKarp:
    def __init__(self):
        self.l = 0
        self.h = 0

    def push_back(self, c):
        val = ord(c) - 96
        self.l += 1
        self.h = (self.h * MUL) % P
        self.h = (self.h + val) % P

    def pop_front(self, c):
        val = ord(c) - 96
        subtract = (val * get_power(self.l - 1)) % P
        self.h = (self.h - subtract) % P
        self.l -= 1