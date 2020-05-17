# https://codeforces.com/contest/344/problem/A

noOfMagnets = int(input())

listOfMagnets = []
noOfGroupOfMagnets = 1

for i in range(noOfMagnets):
    listOfMagnets.append(input())

for i in range(1, len(listOfMagnets)):
    if listOfMagnets[i] != listOfMagnets[i-1]:
        noOfGroupOfMagnets += 1

print(noOfGroupOfMagnets)
