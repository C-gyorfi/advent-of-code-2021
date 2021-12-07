# unittest
import unittest
from readFile import readFile

def processInput(input):
    newFishes = []
    result = []
    for i in input:
        i = int(i)
        if i == 0:
            newFishes.append(8)
            result.append(6)
        else:
            result.append(i-1)
    result.extend(newFishes)
    return result

def runForDays(days, input):
    for i in range(days):
        input = processInput(input)
    return input

def processInputFast(days, input):
    fishes = getFishDictionary()
    for f in input:
        fishes[int(f)] += 1
    for _ in range(days):
        updatedFishes = getFishDictionary()
        for i in range(9):
            if i == 0:
                updatedFishes[i] = fishes[i+1]
                updatedFishes[8] += fishes[0]
                fishes[7] += fishes[0]
            elif i < 8:
                updatedFishes[i] = fishes[i+1]
        fishes = updatedFishes
    return fishes

def getFishDictionary():
    fishes = dict()
    for i in range(9):
        fishes[i] = 0
    return fishes


class Test(unittest.TestCase):
    def testDecreaseInput(self):
        result = processInput([3,4,3,1,2])
        self.assertEqual(result, [2,3,2,0,1])

    def testGenerateNewFish(self):
        result = processInput([2,3,2,0,1])
        self.assertEqual(result, [1,2,1,6,0,8])

    def testRun(self):
        data = readFile('data')[0].split(',')
        days = 256
        fast_result = processInputFast(days, data)
        # slow_result = runForDays(days, data)
        self.assertEqual(1595330616005, sum(fast_result.values()))

if __name__ == '__main__':
    unittest.main()