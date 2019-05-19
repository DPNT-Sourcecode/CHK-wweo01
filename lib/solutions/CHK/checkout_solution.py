# -*- encoding: utf-8 -*-
from collections import defaultdict


price_data = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}
special_price = {
    'A': (3, 130),
    'B': (2, 45),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skus = skus.strip()
    total = 0

    counter = defaultdict(int)
    for c in skus:
        if c not in price_data:
            return -1
        counter[c] += 1

    for c in skus:
        if c not in price_data:
            return -1
        total += price_data[c]
    return total


assert checkout("A") == 50
assert checkout("AB") == 50+30
assert checkout("ABE") == -1
assert checkout("£$%") == -1
assert checkout("AAA") == 130
assert checkout("AAAA") == 130+50
assert checkout("AAAABBD") == 130+50+45+15
assert checkout("AABBDAA") == 130+50+45+15



