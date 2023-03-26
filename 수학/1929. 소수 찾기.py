# 최대 입력 크기: 10^6, 시간 복잡도 상한: O(NlogN), 공간 복잡도 상한: O(NlogN)

def get_primes(st: int, end: int):
    is_prime = [True] * (end + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(end ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(2*i, end + 1, i):
            is_prime[j] = False
    
    primes = [i for i in range(st, end + 1) if is_prime[i]]
    return primes

M, N = map(int, input().split())

primes = get_primes(M, N)

for p in primes:
    print(p)