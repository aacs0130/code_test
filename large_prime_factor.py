#!/usr/bin/env python 

def large_prime_factor(num):
    half = int(num ** 0.5)
    factor = [num]

    while len(factor) != 0:
        now_f = factor.pop()
        for i in range(half, 2):
            if now_f % i == 0:
                if test_if_prime(i):
                    return i
                factor.append(i)
                factor.append(now_f / i)
                factor = sort(factor)

    return num


def test_if_prime(num):
    half = num ** 0.5
    for i in range(2, half+1):
        if num % i == 0:
            return False
    
    return True


print large_prime_factor(600851475143)

