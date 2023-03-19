a, b = map(int, input().split())
results = [a+b, a-b, a*b, a//b, a%b]

for result in results:
    print(result)