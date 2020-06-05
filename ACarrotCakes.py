# https://codeforces.com/contest/799/problem/A

noOfCakesToBeMade, minsOvenReqToBakeABatchOfCakes, noOfCakesInABatch, minsReqToBuildAOven = [int(x) for x in input().split(' ')]

noOfCakesReady = 0
timer = 0

while timer <= minsReqToBuildAOven:
    noOfCakesReady += noOfCakesInABatch
    timer += minsOvenReqToBakeABatchOfCakes

if noOfCakesReady < noOfCakesToBeMade:
    print('YES')
else:
    print('NO')
