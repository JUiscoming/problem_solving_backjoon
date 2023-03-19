from collections import Counter

nums = map(int, input().split())

counts = Counter(nums)

counts = sorted(counts.items(), key = lambda x: (-x[1], -x[0]))

eye, count = counts[0]

if count == 3:
    money = 10000 + eye * 1000
elif count == 2:
    money = 1000 + eye * 100
else:
    money = eye * 100
print(money)

