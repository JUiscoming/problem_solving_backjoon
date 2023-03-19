is_prime = [True for _ in range(1001)]
for i in (0, 1):
    is_prime[i] = False

for n in range(2, int(1001 ** 0.5)):
    if not is_prime[n]:
        continue

    for m in range(n * 2, 1001, n):
        if is_prime[m]:
            is_prime[m] = False


N = int(input())
count_prime = [n for n in map(int, input().split()) if is_prime[n]]
print(len(count_prime))
