x = int(input())
y = input()

for digit_char in y[::-1]:
    print(x * int(digit_char))
print(x * int(y))