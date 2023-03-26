# 최대 입력 크기: 10^7, 시간 복잡도 상한: O(N), 공간 복잡도 상한: O(NlogN)

def get_pos(n: int) -> int:
    row_idx = 0
    sums = 0
    while n > sums:
        row_idx += 1
        sums += row_idx
    col_idx = row_idx - (sums - n) # [1 ~ row_idx]
    
    return row_idx, col_idx

X = int(input())
row, col = get_pos(X)

if row % 2 == 0:
    print(f"{col}/{row - col + 1}")
else:
    print(f"{row - col + 1}/{col}")