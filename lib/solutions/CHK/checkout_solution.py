# -*- encoding: utf-8 -*-
from collections import defaultdict


price_data = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
}
special_price = {
    'A': (3, 130),
    'B': (2, 45),
}
other_specials = {
    '2E': 'B'
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

    # strip out the Bs if we have sufficient Es exist here:
    number_of_es = counter.get('E', 0)
    counter['B'] = max(0, counter['B'] - (number_of_es//2))

    for k,v in counter.items():
        discount = special_price.get(k, None)
        if discount:
            while v >= discount[0]:
                total += discount[1]
                v -= discount[0]
        if v > 0:
            total += price_data[k] * v
    return total


assert checkout("A") == 50
assert checkout("AB") == 50+30
assert checkout("ABZ") == -1
assert checkout("£$%") == -1
assert checkout("AAA") == 130
assert checkout("AAAA") == 130+50
assert checkout("AAAABBD") == 130+50+45+15
assert checkout("AABBDAA") == 130+50+45+15

assert checkout('E') == 40
assert checkout('EEB') == 80
assert checkout('EEBEEEE') == 80*3
assert checkout('BEEBEE') == 80*2
assert checkout('BEEBE') == 80+40+30


