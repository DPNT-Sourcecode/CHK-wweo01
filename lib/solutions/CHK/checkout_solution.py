# -*- encoding: utf-8 -*-
from collections import defaultdict
import math


price_data = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
}

special_price = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)],
    'H': [(10, 80), (5, 45)],
    'K': [(2, 150)],
    'P': [(5, 200)],
    'Q': [(3, 80)],
    'V': [(3, 130), (2, 90)],
}


def trim_and_count(skus):
    skus = skus.strip()
    counter = defaultdict(int)
    for c in skus:
        if c not in price_data:
            raise Exception()
        counter[c] += 1
    return counter


def apply_special_discounts(counter):
    #  2E get one B free
    # strip out the Bs if we have sufficient Es exist here:
    number_of_es = counter.get('E', 0)
    counter['B'] = max(0, counter['B'] - (number_of_es//2))

    # strip out the Fs if we have sufficient Fs exist here:
    # 2F get one F free
    counter['F'] = max(0, int(math.ceil(counter['F']*2.0/3.0)))

    #  3N get one M free
    number_of_ns = counter.get('N', 0)
    counter['M'] = max(0, counter['M'] - (number_of_ns//3))

    #  3R get one Q free
    number_of_rs = counter.get('R', 0)
    counter['Q'] = max(0, counter['Q'] - (number_of_rs//3))

    # 3U get one U free
    counter['U'] = max(0, int(math.ceil(counter['U']*3.0/4.0)))


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        counter = trim_and_count(skus)
    except Exception:
        return -1

    apply_special_discounts(counter)

    total = 0

    for k,v in counter.items():
        discount_list = special_price.get(k, [])
        if discount_list:
            # This wont work if our discounts get weird
            for the_discount in discount_list:
                while v >= the_discount[0]:
                    total += the_discount[1]
                    v -= the_discount[0]
        if v > 0:
            total += price_data[k] * v
    return total


assert checkout('F') == 10
assert checkout('FF') == 20
assert checkout('FFF') == 20
assert checkout('FFFF') == 30
assert checkout('FFFFFF') == 40
assert checkout('FFEFFFF') == 40+40

assert checkout('BEEBE') == 80+40+30
assert checkout("A") == 50
assert checkout("AB") == 50+30
assert checkout("AB0") == -1
assert checkout("£$%") == -1
assert checkout("AAA") == 130
assert checkout("AAAA") == 130+50
assert checkout("AAAABBD") == 130+50+45+15
assert checkout("AABBDAA") == 130+50+45+15

assert checkout("AAAAA") == 200
assert checkout("AAAAAA") == 250
assert checkout("AAAAAAA") == 300
assert checkout("AAAAAAAAA") == 380

assert checkout('E') == 40
assert checkout('EEB') == 80
assert checkout('EEBEEEE') == 80*3
assert checkout('BEEBEE') == 80*2
assert checkout('BEEBE') == 80+40+30
assert checkout('UUVV') == 40*2 + 90
assert checkout('UUVVUU') == 40*3 + 90
assert checkout('P') == 50
assert checkout('PPPPPP') == 50+200
assert checkout('UUU') == 120

