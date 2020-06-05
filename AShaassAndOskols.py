# https://codeforces.com/contest/294/problem/A

noOfWires = int(input())
noOfBirdsOnEachWires = [int(x) for x in input().split(' ')]
noOfBirdsKilled = int(input())

for i in range(noOfBirdsKilled):
    birdKilled = [int(x) for x in input().split(' ')]
    wireNo = birdKilled[0] - 1  # index
    birdNo = birdKilled[1]
    birdsOnLeft = birdNo - 1
    birdsOnRight = noOfBirdsOnEachWires[wireNo] - birdNo
    if wireNo != 0:
        noOfBirdsOnEachWires[wireNo - 1] += birdsOnLeft
    noOfBirdsOnEachWires[wireNo] = 0
    if wireNo != noOfWires-1:
        noOfBirdsOnEachWires[wireNo + 1] += birdsOnRight

print('\n'.join([str(x) for x in noOfBirdsOnEachWires]))
