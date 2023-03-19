"""
https://www.acmicpc.net/board/view/109747
수학적으로 재미있는 풀이
"""

N = int(input())

count_min = -1
for count_3 in range(N // 3 + 1):
    count_5 = N - 3 * count_3
    count_5, remainder = divmod(count_5, 5)
    count = count_3 + count_5
    if not remainder:
        if count_min == -1 or count < count_min:
            count_min = count

print(count_min)