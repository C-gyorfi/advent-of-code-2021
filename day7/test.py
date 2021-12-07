# unittest
import unittest
from readFile import readFile

def groupCrabs(data):
    result = {}
    for key in set(data):
        if key not in result:
            result[key] = 0
    for pos in data: result[pos] += 1
    return result


def costOfPosition(crabs, pos):
    keys = list(crabs.keys())
    cost = 0
    for key in keys:
        cost += abs(key - pos) * crabs[key]
    return cost


def findCheapestCost(crabs):
    cheapest_cost = float("inf")
    keys = list(crabs.keys())

    for i in range(keys[0],keys[-1]+1):
        cost_for_pos = costOfPosition(crabs, i)        
        if cost_for_pos < cheapest_cost:
            cheapest_cost = cost_for_pos
    return cheapest_cost


class Test(unittest.TestCase):
    def testGroupCrabs(self):
        self.assertEqual(groupCrabs([16,1,2,1]), {16: 1, 1: 2, 2: 1})
        self.assertEqual(groupCrabs([16,1,2,0,4,2,7,1,2,14]), {0: 1, 1: 2, 2: 3, 4: 1, 7: 1, 14: 1, 16: 1})

    def testCostOfPosition(self):
        crabs = groupCrabs([16,1,2,0,4,2,7,1,2,14])
        result = costOfPosition(crabs, 2)
        self.assertEqual(result, 37)

    def testFindCheapestCost(self):
        crabs = groupCrabs([16,1,2,0,4,2,7,1,2,14])
        result = findCheapestCost(crabs)
        self.assertEqual(result, 37)

    def testRun(self):
        raw_data = readFile('data')[0].split(',')
        data = [int(x) for x in raw_data]
        crabs = groupCrabs(data)
        self.assertEqual(findCheapestCost(crabs), 1)

if __name__ == '__main__':
    unittest.main()