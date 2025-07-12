import math

def solution(numer1, denom1, numer2, denom2):
    num = denom1 * denom2 // math.gcd(denom1, denom2)
    numer1 = numer1 * (num // denom1)
    numer2 = numer2 * (num // denom2)
    sum = numer1 + numer2
    gcd = math.gcd(sum, num)
    return [sum // gcd, num // gcd]