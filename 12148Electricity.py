# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3300

from datetime import date

day = 0
month = 1
year = 2
consumption = 3

while True:
    noOfReadings = int(input())
    if noOfReadings == 0:
        break
    else:
        listOfEntries = []
        countOfPreciseReading = 0
        consumptionOfPreciseReading = 0
        for i in range(noOfReadings):
            listOfEntries.append([int(x) for x in input().split(' ')])
            if i != 0:
                previousDate = date(listOfEntries[i-1][year], listOfEntries[i-1][month], listOfEntries[i-1][day]).toordinal()
                todaysDate = date(listOfEntries[i][year], listOfEntries[i][month], listOfEntries[i][day]).toordinal()
                if todaysDate - previousDate == 1:
                    consumptionOfPreciseReading += (listOfEntries[i][consumption] - listOfEntries[i - 1][consumption])
                    countOfPreciseReading += 1
        print(countOfPreciseReading, consumptionOfPreciseReading)
