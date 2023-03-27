# 최대 입력 크기: 20, 시간 복잡도 상한: O(2^N), 공간 복잡도 상한: O(2^N)

def get_fibo(n: int) -> int:
    fibo = [0, 1]
    while (len(fibo) - 1) < n:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo[n]

n = int(input())
print(get_fibo(n))