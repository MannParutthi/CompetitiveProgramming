# http://codeforces.com/contest/567/problem/A

noOfCities = int(input())
coOrdinatesOfCities = [int(x) for x in input().split(' ')]

for index, currentCityCoOrdinate in enumerate(coOrdinatesOfCities):
    if index == 0:
        minDistance = abs(coOrdinatesOfCities[index + 1] - currentCityCoOrdinate)
        maxDistance = abs(coOrdinatesOfCities[noOfCities-1]-currentCityCoOrdinate)
    elif index == noOfCities-1:
        minDistance = abs(coOrdinatesOfCities[index - 1] - currentCityCoOrdinate)
        maxDistance = abs(coOrdinatesOfCities[0] - currentCityCoOrdinate)
    else:
        minDistance = min(abs(coOrdinatesOfCities[index - 1] - currentCityCoOrdinate),
                          abs(coOrdinatesOfCities[index + 1] - currentCityCoOrdinate))
        maxDistance = max(abs(coOrdinatesOfCities[0] - currentCityCoOrdinate),
                          abs(coOrdinatesOfCities[noOfCities - 1] - currentCityCoOrdinate))

    print(minDistance, maxDistance)
