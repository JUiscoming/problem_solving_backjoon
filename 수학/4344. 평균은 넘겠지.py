get_mean = lambda x: sum(x) / len(x)

C = int(input())

for _ in range(C):
    N, *scores = list(map(int, input().split()))
    mean = get_mean(scores)
    percentage = sum((1 for score in scores if score > mean)) / N * 100
    print(f"{percentage:.3f}%")