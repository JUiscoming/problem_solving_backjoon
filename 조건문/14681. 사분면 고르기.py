x = int(input())
y = int(input())

candidates = {1, 2, 3, 4}

if x > 0:
    candidates &= {1, 4}
else:
    candidates &= {2, 3}

if y > 0:
    candidates &= {1, 2}
else:
    candidates &= {3, 4}
print(candidates.pop())