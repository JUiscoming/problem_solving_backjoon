import sys

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    print(sum(map(int, line.split())))