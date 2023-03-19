T = int(input())

operands = []
for test_idx in range(T):
    operands.append(map(int, input().split()))

for (op1, op2) in operands:
    print(op1 + op2)