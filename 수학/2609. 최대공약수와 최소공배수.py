# 최대 입력 크기: 10^4, 시간 복잡도 상한: O(NlogN), 공간 복잡도 상한: O(N^2)

def get_gcd(a: int, b: int):
    divisor, dividend = sorted((a, b))
    quotient = dividend % divisor
    while quotient != 0:
        divisor, dividend = sorted((divisor, quotient))
        quotient = dividend % divisor
    return divisor

a, b = map(int, input().split())
gcd = get_gcd(a, b)
lcm = a * b // gcd
print(gcd)
print(lcm)