# http://codeforces.com/contest/427/problem/A

noOfEvents = input()
listOfEvents = [int(x) for x in input().split(' ')]

noOfCrimesUntreated = 0
noOfPolicesFree = 0

for event in listOfEvents:
    if event == -1:
        if noOfPolicesFree <= 0:
            noOfCrimesUntreated += 1
        else:
            noOfPolicesFree -= 1
    else:
        noOfPolicesFree += event

print(noOfCrimesUntreated)
