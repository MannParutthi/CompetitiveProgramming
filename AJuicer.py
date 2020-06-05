# https://codeforces.com/contest/709/problem/A

noOfOranges, maxSizeOfOrangeJuicerCanAccept, wasteToBeEmptiedAtTotalOrangeSize = [int(x) for x in input().split(' ')]
sizeListOfOranges = [int(x) for x in input().split(' ')]

noOfTimesJuicerWasteHasToBeEmptied = 0
totalSizeOfOranges = 0

for orangeSize in sizeListOfOranges:
    if orangeSize <= maxSizeOfOrangeJuicerCanAccept:
        totalSizeOfOranges += orangeSize
        if totalSizeOfOranges > wasteToBeEmptiedAtTotalOrangeSize:
            noOfTimesJuicerWasteHasToBeEmptied += 1
            totalSizeOfOranges = 0

print(noOfTimesJuicerWasteHasToBeEmptied)
