# http://codeforces.com/contest/381/problem/A

noOfCards = input()
listOfCards = [int(x) for x in input().split(' ')]

serejasScore = 0
dimasScore = 0
turnNo = 0

while len(listOfCards) > 0:
    highNumberCard = 0
    turnNo += 1

    if listOfCards[0] > listOfCards[-1]:
        highNumberCard = listOfCards[0]
        listOfCards.remove(listOfCards[0])
    else:
        highNumberCard = listOfCards[-1]
        listOfCards.remove(listOfCards[-1])

    if turnNo % 2 != 0:
        serejasScore += highNumberCard
    else:
        dimasScore += highNumberCard

print(serejasScore, dimasScore)
