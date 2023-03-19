def count_digit(n: int) -> list:
    counts = [0 for _ in range(10)]

    while n > 0:
        counts[n % 10] += 1
        n //= 10
    return counts

a = int(input())
b = int(input())
c = int(input())

result = count_digit(a * b * c)
for count in result:
    print(count)
