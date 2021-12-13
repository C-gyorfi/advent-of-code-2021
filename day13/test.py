import unittest
from readFile import readFile

def foldUp(grid, foldingLine):
    newGrid = {}
    for point in grid:
        if point[1] < foldingLine: newGrid[point] = grid[point]
        if point[1] == foldingLine: continue
        if point[1] > foldingLine:
            y = foldingLine - (point[1] - foldingLine)
            newGrid[(point[0], y)] = grid[point]

    return newGrid

def foldLeft(grid, foldingLine):
    newGrid = {}
    for point in grid:
        if point[0] < foldingLine: newGrid[point] = grid[point]
        if point[0] == foldingLine: continue
        if point[0] > foldingLine:
            x = foldingLine - (point[0] - foldingLine)
            newGrid[(x, point[1])] = grid[point]

    return newGrid

def mapDataToGrid(data):
    grid = {}
    for line in data:
        x, y = line.split(',')
        grid[(int(x), int(y))] = '#'
    return grid

def foldGrid(grid, foldingInst):
    for inst in foldingInst:
        if inst[0] == 'y': grid = foldUp(grid, inst[1])
        if inst[0] == 'x': grid = foldLeft(grid, inst[1])
    return grid

def drawGrid(grid):
    print('\n')
    for y in range(0, max(grid.keys(), key=lambda x: x[1])[1] + 1):
        for x in range(0, max(grid.keys(), key=lambda x: x[0])[0] + 1):
            if (x, y) in grid: print(grid[(x, y)], end='')
            else: print(' ', end='')
        print()
    print('\n')


class Test(unittest.TestCase):
    def testFoldUp(self):
        grid = { (1,0):'#', (0,3):'#', (1, 4): '#'}
        self.assertEqual(foldUp(grid, 2), {(1,0):'#', (0,1):'#'})

    def testMapDataToGrid(self):
        data = readFile('test_data')
        grid = mapDataToGrid(data)
        self.assertEqual(len(grid), 18)
        self.assertEqual(grid[(6,10)], '#')

    def testRun(self):
        data = readFile('test_data')
        grid = mapDataToGrid(data)
        self.assertEqual(len(foldUp(grid, 7)), 17)

        foldingInst = readFile('foldings')
        foldingInst = [(x.split('=')[0][-1], int(x.split('=')[1])) for x in foldingInst]
        data = readFile('data')
        grid = mapDataToGrid(data)
        self.assertEqual(len(foldLeft(grid, 655)), 708)

        foldingInst =  [
            "fold along y=7",
            "fold along x=5"
        ]
        foldingInst = [(x.split('=')[0][-1], int(x.split('=')[1])) for x in foldingInst]
        data = readFile('test_data')
        grid = mapDataToGrid(data)
        grid = foldGrid(grid, foldingInst)
        drawGrid(grid)

        foldingInst = readFile('foldings')
        foldingInst = [(x.split('=')[0][-1], int(x.split('=')[1])) for x in foldingInst]
        data = readFile('data')
        grid = mapDataToGrid(data)
        grid = foldGrid(grid, foldingInst)
        drawGrid(grid)

if __name__ == '__main__':
    unittest.main()