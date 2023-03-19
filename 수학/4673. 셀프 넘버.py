def sum_digits(n: int) -> int:
    result = 0
    while n > 0:
        result += (n % 10)
        n //= 10
    return result

self_numbers = [True for _ in range(10001)]
self_numbers[0] = False

for n in range(1, 10001):
    if not self_numbers[n]:
        continue
    d_n = n
    while True:
        d_n += sum_digits(d_n)
        if not self_numbers[n] or d_n > 10000:
            break
        self_numbers[d_n] = False

for num, bool_value in enumerate(self_numbers):
    if bool_value:
        print(num)