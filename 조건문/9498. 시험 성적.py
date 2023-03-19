x = int(input())

score2credit = {90: 'A', 80: 'B', 70: 'C', 60: 'D', 0: 'F'}

for score in score2credit:
    if x >= score:
        print(score2credit[score])
        break
