# unittest
import unittest
from unittest import result
from bresenham import bresenham

def readFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def formatInput(lines):
    result = []
    remove_arrow = [tuple(line.split(' -> ')) for line in lines]
    for line in remove_arrow:
        result.append(tuple([line[0].split(','), line[1].split(',')]))
    return result

def filterHorizontalAndVerticalLines(data):
    result = []
    for line in data:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            result.append(line)
    return result

def getSortedRange(n1, n2):
    sorted_range = sorted([int(n1), int(n2)])
    sorted_range[-1] = sorted_range[-1]+1
    return range(sorted_range[0], sorted_range[-1])

def generatePointsOnHorizontalOrVerticalLineLine(data):
    points_to_draw = []
    for line in data:
        if line[0][1] == line[1][1]:
            for i in getSortedRange(line[0][0], line[1][0]):
                points_to_draw.append(f'{i}, {line[0][1]}')
        elif line[0][0] == line[1][0]:
            for i in getSortedRange(line[0][1], line[1][1]):
                points_to_draw.append(f'{line[0][0]}, {i}')

    return points_to_draw

def generatePointsWithBresenham(data):
    points_to_draw = []
    for line in data:
        coordinates = list(bresenham(int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])))
        coordinates = [f'{c[0]}, {c[1]}' for c in coordinates]
        points_to_draw.extend(coordinates)
    return points_to_draw

def countOverlap(points):
    grid = {}
    result = 0
    for point in points:
        if point in grid:
            grid[point] += 1
        else:
            grid[point] = 1
    
    for c in grid:
        if grid[c] > 1:
            result += 1
    return result

class Test(unittest.TestCase):
    def testFormatInput(self):
      self.assertEqual(formatInput(readFile('test_data'))[0], (['0', '9'], ['5', '9']))
      self.assertEqual(formatInput(readFile('test_data'))[9], (['5', '5'], ['8', '2']))

    def testGenerateCoordinates(self):
        data = formatInput(readFile('test_data'))
        self.assertEqual(generatePointsOnHorizontalOrVerticalLineLine(data)[0], '0, 9')
        self.assertEqual(generatePointsOnHorizontalOrVerticalLineLine(data)[1], '1, 9')
        self.assertEqual(generatePointsOnHorizontalOrVerticalLineLine(data)[2], '2, 9')
        self.assertEqual(generatePointsOnHorizontalOrVerticalLineLine(data)[-3], '1, 4')
        self.assertEqual(generatePointsOnHorizontalOrVerticalLineLine(data)[-2], '2, 4')
        self.assertEqual(generatePointsOnHorizontalOrVerticalLineLine(data)[-1], '3, 4')

    def testGenerateCoordinatesWithBresenham(self):
        data = filterHorizontalAndVerticalLines(formatInput(readFile('test_data')))
        self.assertEqual(generatePointsWithBresenham(data)[0], '0, 9')
        self.assertEqual(generatePointsWithBresenham(data)[1], '1, 9')
        self.assertEqual(generatePointsWithBresenham(data)[2], '2, 9')
        self.assertEqual(generatePointsWithBresenham(data)[-3], '3, 4')
        self.assertEqual(generatePointsWithBresenham(data)[-2], '2, 4')
        self.assertEqual(generatePointsWithBresenham(data)[-1], '1, 4')

    def testCountDuplicate(self):
        lines = [
            "0,2 -> 0,2",
            "0,2 -> 0,2",
            "0,2 -> 0,2",
            "0,2 -> 3,2",
        ]
        data = formatInput(lines)
        points = generatePointsOnHorizontalOrVerticalLineLine(data)
        result = countOverlap(points)
        self.assertEqual(result, 1)

    def testRun(self):
        data = formatInput(readFile('data'))

        points = generatePointsOnHorizontalOrVerticalLineLine(data)
        result = countOverlap(points)
        self.assertEqual(result, 4826)

        points = generatePointsWithBresenham(data)
        result = countOverlap(points)
        self.assertEqual(result, 16793)

if __name__ == '__main__':
    unittest.main()