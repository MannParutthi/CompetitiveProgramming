# http://codeforces.com/contest/474/problem/A

shiftDirection = input()
charsEnteredByMode = input()

if shiftDirection == 'L':
    valueAdjustment = 1
elif shiftDirection == 'R':
    valueAdjustment = -1
keySeq = 'qwertyuiopasdfghjkl;zxcvbnm,./'
actualMsg = ''

for char in charsEnteredByMode:
    actualMsg += keySeq[keySeq.find(char) + valueAdjustment]

print(actualMsg)
