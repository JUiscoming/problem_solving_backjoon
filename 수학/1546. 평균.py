N = int(input())

scores = list(map(int, input().split()))
scores_updated = [score/max(scores)*100 for score in scores]

print(sum(scores_updated)/N)