# http://codeforces.com/contest/266/problem/A

noOfStones = input()
listOfStones = list(input())

noOfStonesToRemove = 0

if listOfStones.count(listOfStones[0]) == len(listOfStones):
    noOfStonesToRemove = len(listOfStones) - 1
else:
    for i in range(0, len(listOfStones) - 1):
        if listOfStones[i] == listOfStones[i + 1]:
            noOfStonesToRemove += 1

print(noOfStonesToRemove)
