# https://codeforces.com/contest/732/problem/A

priceAndDenomination = input().split(' ')

priceOfOneShovel = int(priceAndDenomination[0])
denominationOfCoinInPocket = int(priceAndDenomination[1])

noOfShovelsToBuyWithoutChange = 0

while True:
    noOfShovelsToBuyWithoutChange += 1
    if (noOfShovelsToBuyWithoutChange * priceOfOneShovel) % 10 in [0, denominationOfCoinInPocket]:
        break

print(noOfShovelsToBuyWithoutChange)
