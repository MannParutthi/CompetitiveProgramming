# https://codeforces.com/contest/9/problem/A

points = [int(x) for x in input().split(' ')]

minPointDotNeedsToWin = max(points[0], points[1])
dictOfDiceProbability = {1: '1/1', 2: '5/6', 3: '2/3', 4: '1/2', 5: '1/3', 6: '1/6'}

probabilityOfDotToWin = dictOfDiceProbability[minPointDotNeedsToWin]

print(probabilityOfDotToWin)
