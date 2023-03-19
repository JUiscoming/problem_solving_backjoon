year = int(input())

condition = 0
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    condition = 1
print(condition)
