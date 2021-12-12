import unittest
from readFile import readFile

def mapRoutes(data):
    routes = {}
    for line in data:
        line = line.split('-')
        if line[0] in routes: routes[line[0]].add(line[1])
        else: routes[line[0]] = set([line[1]])
        if line[1] in routes: routes[line[1]].add(line[0])
        else: routes[line[1]] = set([line[0]])
    return routes

def canContinue1(currentRoute):
    route = currentRoute.split(',')
    location = route.pop()
    if location == "end": return False
    return not (location.islower() and location in route)

def canContinue2(currentRoute):
    route = currentRoute.split(',')
    location = route[-1]
    if location == "start" and not len(route) == 1: return False
    if location == "end": return False
    if location.islower():
        if route.count(location) > 2: return False
        if route.count(location) > 1:
            lowers = [l for l in route if l.islower()]
            return len(lowers) == len(set(lowers))+1       
    return True

def findDistinctRoutes(routesMap, distinctRoutes, currentRoute, canContinue):
    currentLocation = currentRoute.split(',')[-1]
    if not canContinue(currentRoute):
        if currentLocation == "end": distinctRoutes.append(currentRoute)
        return distinctRoutes

    for dest in routesMap[currentLocation]:
        distinctRoutes = findDistinctRoutes(routesMap, distinctRoutes, currentRoute + "," + dest, canContinue)
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

    def testCanContinue(self):
        self.assertFalse(canContinue1('start,A,b,end'))
        self.assertTrue(canContinue1('start,A,b,c'))

        self.assertTrue(canContinue2('start,A,b,c,b'))
        self.assertTrue(canContinue2('start,A,c,A,c,A,b'))

        self.assertFalse(canContinue2('start,A,b,end'))
        self.assertFalse(canContinue2('start,A,b,c,b,c'))
        self.assertFalse(canContinue2('start,A,b,c,b,c,b'))
        self.assertFalse(canContinue2('start,b,c,b,c,start'))
        self.assertFalse(canContinue2('start,A,b,A,b,A,b'))

    def testFindDistinctRoutes(self):
        data = ['start-A', 'A-b', 'b-end', 'A-end']
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start', canContinue1)
        self.assertEquals(set(distinctRoutes), {'start,A,end', 'start,A,b,end', 'start,A,b,A,end'})

        data = readFile('test_data')
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start', canContinue1)
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

    def testFindDistinctRoutesPart2(self):
        data = ['start-A', 'A-b', 'b-end', 'A-end']
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start', canContinue2)
        self.assertEquals(set(distinctRoutes), {'start,A,end', 'start,A,b,end', 'start,A,b,A,end', 'start,A,b,A,b,end', 'start,A,b,A,b,A,end'})

        data = readFile('test_data')
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start', canContinue2)
        expectedRoutes = readFile('expectedPart2')
        self.assertEquals(
            set(distinctRoutes), 
            set(expectedRoutes)
        )
        self.assertEquals(len(distinctRoutes), 36)


    def testRun(self):
        data = readFile('data')
        routesMap = mapRoutes(data)
        distinctRoutes = findDistinctRoutes(routesMap, [], 'start', canContinue1)
        self.assertEquals(len(distinctRoutes), 5874)

        data = readFile('data')
        routesMap = mapRoutes(data)
        distinctRoutesPart2 = findDistinctRoutes(routesMap, [], 'start', canContinue2)
        self.assertEquals(len(distinctRoutesPart2), 153592)

if __name__ == '__main__':
    unittest.main()