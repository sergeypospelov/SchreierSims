from collections import deque
from Perm import Perm


class ShreierAlgorithm:
    S = []

    def __init__(self, S):
        self.S = S


def build_tree(n, generator_set, b):
    ext_gs = [(s, ~s) for s in generator_set]
    vector = [None] * n
    q = deque()
    q.append(b)
    vector[b - 1] = -1
    while q:
        x = q.popleft()
        for (s, inv_s) in ext_gs:
            if vector[inv_s[x] - 1] is None:
                vector[inv_s[x] - 1] = s
                q.append(inv_s[x])

    return vector
