# https://codeforces.com/contest/228/problem/A

colorsOfHorseshoesValeraHas = [int(x) for x in input().split(' ')]

noOfShoesValeraNeedsToBuy = 0
dictOfShoes = {}

for val in colorsOfHorseshoesValeraHas:
    dictOfShoes[val] = colorsOfHorseshoesValeraHas.count(val)

for color, noOfShoes in dictOfShoes.items():
    noOfShoesValeraNeedsToBuy += noOfShoes-1

print(noOfShoesValeraNeedsToBuy)
