def sum_digits(n: int) -> int:
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result

N = int(input())

result = N
count = 0
while True:
    count += 1
    result = (result % 10 * 10) + sum_digits(result) % 10
    if result == N:
        print(count)
        break