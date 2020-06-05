# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3104

noOfTests = int(input())

for i in range(noOfTests):
    gridSize = int(input())
    matrix = []
    noOfShipsAlive = 0
    for r in range(gridSize):
        matrix.append(input())
        # noOfShipsAlive += matrix[r].count('x')



    print('Case', str(i+1) + ':', noOfShipsAlive)
