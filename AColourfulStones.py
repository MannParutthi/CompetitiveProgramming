# https://codeforces.com/contest/265/problem/A

listOfStones = list(input())
listOfInstructions = list(input())

positionOfLiss = 1

for instruction in listOfInstructions:
    if instruction == listOfStones[positionOfLiss-1]:
        positionOfLiss += 1

print(positionOfLiss)
