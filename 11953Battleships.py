# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3104


def connectedComponents(rowno, colno, gridsize):
    if 0 <= rowno < gridsize and 0 <= colno < gridsize and not visited[rowno][colno] and matrix[rowno][colno] != '.':
        visited[rowno][colno] = True
        connectedComponents(rowno - 1, colno, gridsize)  # check up
        connectedComponents(rowno + 1, colno, gridsize)  # check down
        connectedComponents(rowno, colno - 1, gridsize)  # check left
        connectedComponents(rowno, colno + 1, gridsize)  # check right
    else:
        return


noOfTests = int(input())

for i in range(noOfTests):
    gridSize = int(input())
    matrix = []
    visited = []
    noOfShipsAlive = 0
    for r in range(gridSize):
        rowData = list(input())
        matrix.append(rowData)
        visited.append([False for x in rowData])

    for rowNo in range(gridSize):
        for colNo in range(gridSize):
            if not visited[rowNo][colNo] and matrix[rowNo][colNo] == 'x':
                connectedComponents(rowNo, colNo, gridSize)
                noOfShipsAlive += 1
    print('Case', str(i+1)+':', noOfShipsAlive)
