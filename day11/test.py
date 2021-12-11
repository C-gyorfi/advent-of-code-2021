import unittest
from readFile import readFile
import numpy as np

def mapDataToGrid(data):
    grid = []
    for line in data:
        ls = list(line)
        int_array = [int(x) for x in ls]
        grid.append(int_array)
    return grid

def safeAccess(grid, x, y):
    if x < 0 or y < 0: return None
    try:
        return grid[y][x]
    except IndexError: return None

def checkAround(x, y, grid, flashed, count):
    result = { 'x': x, 'y': y, 'grid': grid, 'flashed': flashed, 'count': count }
    point = safeAccess(result['grid'], x, y)
    if (x, y) in flashed: return result
    if point == 9:
        result['grid'][y][x] = 0
        result['count']+=1
        result['flashed'].append((x, y))
        result = checkAround(x-1, y, result['grid'], result['flashed'], result['count'])
        result = checkAround(x+1, y, result['grid'], result['flashed'], result['count'])
        result = checkAround(x, y+1, result['grid'], result['flashed'], result['count'])
        result = checkAround(x, y-1, result['grid'], result['flashed'], result['count'])
        result = checkAround(x-1, y+1, result['grid'], result['flashed'], result['count'])
        result = checkAround(x+1, y+1, result['grid'], result['flashed'], result['count'])
        result = checkAround(x-1, y-1, result['grid'], result['flashed'], result['count'])
        result = checkAround(x+1, y-1, result['grid'], result['flashed'], result['count'])
    elif not point == None:
        result['grid'][y][x] = point+1
    return result

def isAllFlashed(grid):
    return set(np.array(grid).flatten()) == {0}

def checkFlashes(grid, numberOfSteps=100, findStepWhenInSync=False):
    count = 0
    current_grid = grid
    if findStepWhenInSync: numberOfSteps = 999999999999999999
    for step in range(numberOfSteps):
        if isAllFlashed(current_grid) and findStepWhenInSync:
            return step

        flashed = []
        for y, row in enumerate(grid):
            for x, _value in enumerate(row):
                thisCheck = checkAround(x, y, current_grid, flashed, count)
                flashed = thisCheck['flashed']
                count = thisCheck['count']
                current_grid = thisCheck['grid']
    return count

class Test(unittest.TestCase):
    def testCheckFlashes(self):
        data = readFile('test_data')
        grid = mapDataToGrid(data)
        findStepWhenInSync = False
        self.assertEqual(checkFlashes(grid), 1656)

    def testIsAllFlashed(self):
        data = ['000', '000', '000']
        grid = mapDataToGrid(data)
        self.assertTrue(isAllFlashed(grid))

        data = ['004', '000', '000']
        grid = mapDataToGrid(data)
        self.assertFalse(isAllFlashed(grid))

    def testRun(self):
        data = readFile('data')
        grid = mapDataToGrid(data)
        self.assertEqual(checkFlashes(grid), 1615)
        
        data = readFile('data')
        grid = mapDataToGrid(data)
        self.assertEqual(checkFlashes(grid, findStepWhenInSync=True), 249)

if __name__ == '__main__':
    unittest.main()