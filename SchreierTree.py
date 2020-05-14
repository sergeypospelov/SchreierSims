from collections import deque
from Perm import Perm, id_perm


class SchreierTree:
    def build(self, generator_set):
        gs = [(~g, g) for g in generator_set]
        elems = list(self.orbit.keys())

        for elem in elems:
            for inv_g, g in gs:
                next_elem = inv_g[elem]
                if next_elem not in self.orbit:
                    self.orbit[next_elem] = self.orbit[elem] * g
                    elems.append(next_elem)

    def __init__(self, generator_set, b: int, n: int):
        self.orbit = {b: id_perm(n)}

        self.build(generator_set)

    def __getitem__(self, index):
        return self.orbit.get(index)

    def get_orbit(self):
        return self.orbit.keys()
