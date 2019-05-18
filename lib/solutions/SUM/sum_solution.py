# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    return x + y


assert compute(0, 0) == 0
assert compute(20, 0) == 20
assert compute(0, 20) == 20
assert compute(90, 20) == 110

