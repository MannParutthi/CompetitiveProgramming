# http://codeforces.com/problemset/problem/767/A

totalNoOfSnacks = int(input())
snacksSizeListOnIthDay = [int(x) for x in input().split(' ')]

dictOfPossibleNumbersReceivedStatus = {x: False for x in snacksSizeListOnIthDay}
currentMaxSnackSize = totalNoOfSnacks

for i in range(totalNoOfSnacks):
    dictOfPossibleNumbersReceivedStatus[snacksSizeListOnIthDay[i]] = True
    while currentMaxSnackSize > 0 and dictOfPossibleNumbersReceivedStatus[currentMaxSnackSize]:
        print(currentMaxSnackSize, end=' ')
        currentMaxSnackSize -= 1
    print()
