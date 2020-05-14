import Perm
from SchreierTree import SchreierTree


class Algorithm:
    class ChainSegment:
        def __init__(self, n, stab_gen, next_stab_point):
            self.n = n
            self.stab_gen = stab_gen
            self.next_stab_point = next_stab_point
            self.build_tree()

        def build_tree(self):
            self.tree = SchreierTree(self.stab_gen, self.next_stab_point, self.n)

        def get_schreier_generators(self):
            schreier_generators = []
            for o in self.tree.get_orbit():
                for gen in self.stab_gen:
                    schreier_generators.append(self.tree[gen[o]] * gen * ~self.tree[o])
            return schreier_generators

    def __init__(self, n, generator_set, base):
        self.n = n
        self.base = base
        self.stab_chain = [self.ChainSegment(n, generator_set, base[1]),
                           self.ChainSegment(n, [Perm.id_perm(n)], base[2])]

    def check_element(self, h):
        copy_h = h
        k = len(self.stab_chain)
        segment_i = 0
        while segment_i < k - 1:
            segment = self.stab_chain[segment_i]
            u = segment.tree[copy_h[self.stab_chain[segment_i].next_stab_point]]
            if u is None:
                return copy_h, segment_i
            copy_h = u * copy_h

            segment_i += 1
        return copy_h, segment_i

    def rec(self, pos):
        self.stab_chain[pos].build_tree()
        schreier_generators = self.stab_chain[pos].get_schreier_generators()

        for h in schreier_generators:
            residue, break_pos = self.check_element(h)
            if residue != Perm.id_perm(self.n):
                if break_pos == len(self.stab_chain) - 1:
                    self.stab_chain.append(
                        self.ChainSegment(self.n, [Perm.id_perm(self.n)], self.base[len(self.stab_chain) + 1]))
                for broken in range(break_pos, pos, -1):
                    self.stab_chain[broken].stab_gen.append(residue)
                    self.rec(broken)

    def run(self):
        self.rec(0)
        pass

    def get_order(self) -> int:
        res = 1
        for segment in self.stab_chain:
            res *= len(segment.tree.orbit)
        return res
