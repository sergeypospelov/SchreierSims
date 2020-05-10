class Perm:
    perm = []

    def __init__(self):
        self.perm = [1]

    def __init__(self, n):
        self.perm = list(range(1, n + 1))

    def __init__(self, lst):
        self.perm = lst

    def __str__(self):
        return self.perm.__str__()

    def __len__(self):
        return len(self.perm)

    def __getitem__(self, item):
        return self.perm[item]

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("different lengths")
        res = [0] * len(self)
        for i in range(len(self)):
            res[i] = other[self[i] - 1]
        return Perm(res)

    def __imul__(self, other):
        self = self * other
        return self

    def __invert__(self):
        res = [0] * len(self)
        for i in range(len(self)):
            res[self[i] - 1] = i + 1
        return Perm(res)

    def as_cycles(self):
        res = []
        used = [False] * len(self)
        for i in range(len(self)):
            j = i
            cur = []
            while not used[j]:
                used[j] = True
                cur.append(j + 1)
                j = self[j] - 1
            if cur:
                res.append(cur)
        return res

    @staticmethod
    def e(n):
        return Perm(n)
