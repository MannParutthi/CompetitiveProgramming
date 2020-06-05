# https://codeforces.com/contest/686/problem/A

noOfPeopleInQueue, noOfIcecreamsTheyHave = [int(x) for x in input().split(' ')]

noOfKidsGoBackDisstressed = 0

for i in range(noOfPeopleInQueue):
    icecreamsIncomingOrOutgoing, noOfIcecreams = input().split(' ')
    if icecreamsIncomingOrOutgoing == '+':
        noOfIcecreamsTheyHave += int(noOfIcecreams)
    elif icecreamsIncomingOrOutgoing == '-':
        if noOfIcecreamsTheyHave >= int(noOfIcecreams):
            noOfIcecreamsTheyHave -= int(noOfIcecreams)
        else:
            noOfKidsGoBackDisstressed += 1

print(noOfIcecreamsTheyHave, noOfKidsGoBackDisstressed)
