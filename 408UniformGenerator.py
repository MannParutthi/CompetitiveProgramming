# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=349

while True:
    try:
        step, mod = [int(x) for x in input().split(' ')]
        listOfPossibleOutcomes = []
        seed = 0
        for i in range(mod):
            if i != 0:
                seed = listOfPossibleOutcomes[i-1]
            listOfPossibleOutcomes.append((seed+step) % mod)
        if 0 in listOfPossibleOutcomes and mod-1 in listOfPossibleOutcomes:
            print(str(step).rjust(10), str(mod).rjust(9), '   ', 'Good Choice')
        else:
            print(str(step).rjust(10), str(mod).rjust(9), '   ', 'Bad Choice')
    except:
        break
