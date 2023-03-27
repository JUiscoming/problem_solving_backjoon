# 최대 입력 크기: 10^4, 시간 복잡도 상한: O(NlogN), 공간 복잡도 상한: O(N^2)

def get_primes(st: int, end: int):
    is_prime = [True] * (end + 1)
    for i in range(2):
        is_prime[i] = False
    for i in range(2, int(end ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(2 * i, end + 1, i):
            is_prime[j] = False
    primes = []
    for i in range(st, end + 1):
        if is_prime[i]:
            primes.append(i)
    return primes

M = int(input())
N = int(input())
primes = get_primes(M, N)

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)