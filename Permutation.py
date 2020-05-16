from typing import Iterable


class Perm:
    perm = []

    def __init__(self, lst: list) -> None:
        self.perm = lst

    def __str__(self):
        return self.perm.__str__()

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.perm)

    def __getitem__(self, item):
        return self.perm[item - 1]

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("different lengths")
        res = [0] * len(self)
        for i in range(len(self)):
            res[i] = self[other[i + 1]]
        return Perm(res)

    def __imul__(self, other):
        self = self * other
        return self

    def __invert__(self):
        res = [0] * len(self)
        for i in range(len(self)):
            res[self[i + 1] - 1] = i + 1
        return Perm(res)

    def __eq__(self, other):
        return self.perm == other.perm

    def as_cycles(self):
        res = []
        used = [False] * len(self)
        for i in range(len(self)):
            j = i
            cur = []
            while not used[j]:
                used[j] = True
                cur.append(j + 1)
                j = self[j + 1] - 1
            if cur:
                res.append(tuple(cur))
        return res


def identity(n: int):
    return Perm([i + 1 for i in range(n)])


def from_cycles(n, cycles: Iterable[Iterable[int]]):
    res = [i + 1 for i in range(n)]
    for cycle in cycles:
        for pos, elem in enumerate(cycle):
            res[cycle[pos - 1] - 1] = elem
    return Perm(res)
