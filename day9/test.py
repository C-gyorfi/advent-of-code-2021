# unittest
import unittest
from unittest.case import skip
from readFile import readFile

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

def anyInArrayIsLower(array, num):
    for x in array:
        if x == None: continue
        if x <= num: return True
    return False

def sumLowestPoints(grid):
    low_points = []
    sum = 0
    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            adjacent = [
                safeAccess(grid, x-1, y), 
                safeAccess(grid, x+1, y), 
                safeAccess(grid, x, y-1), 
                safeAccess(grid, x, y+1)
            ] 
            if not anyInArrayIsLower(adjacent, point):
                low_points.append(point)
                sum += point+1
    return { 'sum': sum, 'low_points': low_points }

def isBoundary(location):
    return (location == 9 or location == None)

def sumAdjacent(grid, current_sum, checked_locations, x, y):
    if (x,y) in checked_locations or isBoundary(safeAccess(grid, x, y)): return { 'sum': current_sum, 'checked': checked_locations }
    checked_locations.append((x,y))
    current_sum += 1

    for direction in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
        sm  = sumAdjacent(grid, current_sum, checked_locations, direction[0], direction[1])
        current_sum = sm['sum']
        checked_locations = sm['checked']

    return { 'sum': current_sum, 'checked': checked_locations }

def sumLargesBasins(grid):
    checked_locations = []
    sum_of_basins = []

    for y, row in enumerate(grid):
        for x, point in enumerate(row):
            if point == 9 or (x,y) in checked_locations: continue
            current_sum = 0

            sumOfAdj = sumAdjacent(grid, current_sum, checked_locations, x, y)
            current_sum = sumOfAdj['sum']
            checked_locations = sumOfAdj['checked']

            sum_of_basins.append(current_sum)
    sum_of_basins.sort()
    return sum_of_basins[-1] * sum_of_basins[-2] * sum_of_basins[-3]

class Test(unittest.TestCase):
    def testMapDataToGrid(self):
        data  = readFile('test_data')
        grid = mapDataToGrid(data)
        self.assertEqual(grid[0][0], 2)
        self.assertEqual(grid[4][9], 8)

    def testSumLowestPoints(self):
        data  = readFile('test_data')
        grid = mapDataToGrid(data)
        self.assertEqual(sumLowestPoints(grid)['sum'], 15)

    def testSumLargestBasins(self):
        data  = readFile('test_data')
        grid = mapDataToGrid(data)
        self.assertEqual(sumLargesBasins(grid), 1134)

    def testRun(self):
        data  = readFile('data')
        grid = mapDataToGrid(data)
        self.assertEqual(sumLowestPoints(grid)['sum'], 603)
        self.assertEqual(sumLargesBasins(grid), 786780)

if __name__ == '__main__':
    unittest.main()