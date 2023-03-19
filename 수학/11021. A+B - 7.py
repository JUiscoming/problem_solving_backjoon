T = int(input())

results = []
for _ in range(T):
    a, b = map(int, input().split())
    results.append(a + b)

for case_idx, result in enumerate(results):
    print(f"Case #{case_idx + 1}: {result}")