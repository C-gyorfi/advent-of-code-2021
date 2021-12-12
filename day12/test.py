import unittest
from readFile import readFile

def mapRoutes(data):
    routes = {}
    for line in data:
        line = line.split('-')
        if line[0] in routes:
            routes[line[0]].add(line[1])
        else:
            routes[line[0]] = set([line[1]])
        if line[1] in routes:
            routes[line[1]].add(line[0])
        else:
            routes[line[1]] = set([line[0]])
    return routes

def canContinue(currentRoute):
    route = currentRoute.split(',')
    location = route.pop()
    if location == "end": return False
    return not (location.islower() and location in route)

def findDistinctRoutes(routesMap, distinctRoutes, currentRoute):
    currentLocation = currentRoute.split(',')[-1]
    if not canContinue(currentRoute):
        if currentLocation == "end": distinctRoutes.append(currentRoute)
        return distinctRoutes

    for dest in routesMap[currentLocation]:
        distinctRoutes = findDistinctRoutes(routesMap, distinctRoutes, currentRoute + "," + dest)
    return distinctRoutes

class Test(unittest.TestCase):
    def testMapRoutes(self):
        data = readFile('test_data')
        self.assertEquals(
            mapRoutes(data), 
            {
                'start': {'A', 'b'}, 
                'A': {'c', 'b', 'end', 'start'},
                'b': {'d', 'end', 'start', 'A'},
                'c': {'A'},
                'd': {'b'},
                'end': {'A', 'b'}
            }
        )

    def testCanVisit(self):
        self.assertFalse(canContinue('start,A,b,end'))
        self.assertTrue(canContinue('start,A,b,c'))

    def testFindDistinctRoutes(self):
        data = ['start-A', 'A-b', 'b-end', 'A-end']
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start')
        self.assertEquals(set(distinctRoutes), {'start,A,end', 'start,A,b,end', 'start,A,b,A,end'})

        data = readFile('test_data')
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start')
        self.assertEquals(
            set(distinctRoutes), 
            {
                "start,A,b,A,c,A,end",
                "start,A,b,A,end",
                "start,A,b,end",
                "start,A,c,A,b,A,end",
                "start,A,c,A,b,end",
                "start,A,c,A,end",
                "start,A,end",
                "start,b,A,c,A,end",
                "start,b,A,end",
                "start,b,end"
            }
        )

    def testRun(self):
        data = readFile('data')
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start')
        self.assertEquals(len(distinctRoutes), 5874)

if __name__ == '__main__':
    unittest.main()