a, b, c = map(int, input().split())
results = [(a+b)%c, ((a%c)+(b%c))%c, (a*b)%c, ((a%c)*(b%c))%c]

for result in results:
    print(result)