import Permutation
import Schreier


# example
# order of Rubik's cube group
def rubik():
    n = 48
    base = Permutation.identity(n)

    L = [(1, 3, 8, 6), (2, 5, 7, 4), (33, 9, 41, 32), (36, 12, 44, 29), (38, 14, 46, 27)]
    F = [(9, 11, 16, 14), (10, 13, 15, 12), (38, 17, 43, 8), (39, 20, 42, 5), (40, 22, 41, 3)]
    R = [(17, 19, 24, 22), (18, 21, 23, 20), (48, 16, 40, 25), (45, 13, 37, 28), (43, 11, 35, 30)]
    B = [(25, 27, 32, 30), (26, 29, 31, 28), (19, 33, 6, 48), (21, 34, 4, 47), (24, 35, 1, 46)]
    U = [(33, 35, 40, 38), (34, 37, 39, 36), (25, 17, 9, 1), (26, 18, 10, 2), (27, 19, 11, 3)]
    D = [(41, 43, 48, 46), (42, 45, 47, 44), (6, 14, 22, 30), (7, 15, 23, 31), (8, 16, 24, 32)]

    generator_set = [L, F, R, B, U, D]
    generator_set = [Permutation.from_cycles(n, move) for move in generator_set]

    example = Schreier.Algorithm(n, generator_set, base)
    example.run()

    print(example.get_order())


# my project task
# works about 15 seconds
def task():
    n = 56
    rows = 7
    cols = 8

    swap_rows_cols = []
    for i in range(rows):
        for j in range(cols):
            swap_rows_cols.append(j * rows + i + 1)
    swap_rows_cols = Permutation.Perm(swap_rows_cols)
    print(swap_rows_cols.as_cycles())  # first generator

    swap_halves = Permutation.Perm([(n // 2 + i) % n + 1 for i in range(n)])
    print(swap_halves.as_cycles())  # second generator

    generator_set = [swap_rows_cols, swap_halves]

    # top cards in right order
    print("Enter top cards order")
    print("example: 1 3 2 4 will check deck with these cards on the top")
    order = list(map(int, input().split()))
    base = order.copy()
    for i in range(1, n + 1):
        if i not in base:
            base.append(i)
    base = Permutation.Perm(base)
    print(order)

    cards = Schreier.Algorithm(n, generator_set, base)
    cards.run()

    print(cards.get_order())  # order of group
    print(cards.stab_chain[1].stab_gen)  # generators of stabilizer of point 1

    residue, level = cards.check_element(base)
    print(residue, level)
    if level >= len(order):
        print("Possible")
    else:
        print("Impossible")

task()
