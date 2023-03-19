C = int(input())

for c_idx in range(C):
    a, b = map(int, input().split())
    print(f"Case #{c_idx + 1}: {a} + {b} = {a + b}")