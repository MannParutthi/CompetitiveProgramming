# http://codeforces.com/contest/431/problem/A

listOfCalories = [int(x) for x in input().split(' ')]
gameProcessStrips = [int(x) for x in list(input())]

noOfCaloriesWasted = 0

for index, wasteOfCalorie in enumerate(listOfCalories):
    noOfCaloriesWasted += (gameProcessStrips.count(index+1) * wasteOfCalorie)

print(noOfCaloriesWasted)
