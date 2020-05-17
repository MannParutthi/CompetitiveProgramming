# https://codeforces.com/contest/731/problem/A

wordToPrint = input()

charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
noOfRotations = 0

for index, val in enumerate(wordToPrint):
    if index != 0:
        previousChar = wordToPrint[index-1]
    else:
        previousChar = charList[0]
    diff = abs(charList.index(previousChar) - charList.index(val))
    noOfRotations += min(diff, 26-diff)

print(noOfRotations)
