import unittest
from readFile import readFile

def mapDataToGrid(data):
    grid = []
    for line in data:
        ls = list(line)
        int_array = [int(x) for x in ls]
        grid.append(int_array)
    return grid      

def mapDataToLocationDict(data):
    locationDict = {}
    for y, row in enumerate(data):
        for x, value in enumerate(row):
            locationDict[(y,x)] = int(value)
    return locationDict

def findCheapestRoute(locationDict, currentRoute, checkedRoutes, cheapestRoute, y, x, costOfRoute=0):
    if currentRoute == '(0, 0),(1, 0),(1, 1),(0, 1)':
        breakpoint()
    result = {'currentRoute': currentRoute, 'checkedRoutes': checkedRoutes, 'cheapestRoute': cheapestRoute, 'costOfRoute': costOfRoute}
    allKeys = list(locationDict.keys())
    if (y,x) == allKeys[-1] and result['currentRoute'] not in result['checkedRoutes']:
        result['checkedRoutes'].append(result['currentRoute'])
        if result['costOfRoute'] < result['cheapestRoute']:
            result['cheapestRoute'] = result['costOfRoute']
    if currentRoute == '(0, 0),(1, 0),(1, 1),(0, 1)':
        breakpoint()
    if (y,x) != allKeys[-1]:
        for location in [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]:
            if str(location) in result['currentRoute']: 
                continue
            if location in locationDict:
                newY = location[0]
                newX = location[1]
                newCostOfRoute = result['costOfRoute'] + locationDict[(newY, newX)]
                newCurrentRoute = result['currentRoute'] + ',' + f'{(newY, newX)}'
                result = findCheapestRoute(locationDict, newCurrentRoute, result['checkedRoutes'], result['cheapestRoute'], newY, newX, newCostOfRoute)
    return result

def findAllRoutes(locationDict, y, x, currentRoute=[(0,0)], routes=[]):
    routes = routes
    currentRoute = currentRoute
    allKeys = list(locationDict.keys())
    if (y,x) == allKeys[-1]:
        routes.append(currentRoute)
    if (y,x) != allKeys[-1]:
        for location in [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]:
            if location in currentRoute: 
                continue
            if location in locationDict:
                newY = location[0]
                newX = location[1]
                newRoute = [x for x in currentRoute]
                newRoute.append((newY, newX))
                routes = findAllRoutes(locationDict, newY, newX, newRoute, routes)
    return routes

def findCheapestRoute(possibleRoutes, locationDict):
    cheapestRoute = float('inf')
    for route in possibleRoutes:
        thisRouteCost = 0
        route.pop(0)
        for l in route:
                thisRouteCost += locationDict[l]
        if thisRouteCost < cheapestRoute:
            cheapestRoute = thisRouteCost
    return cheapestRoute

class Test(unittest.TestCase):
    def testMapDataToGrid(self):
        data = readFile('test_data')
        grid = mapDataToGrid(data)
        self.assertEqual(grid[0][0], 1)

    def testMapDataToLocationDict(self):
        data = [
            '116',
            '213',
            '112'
        ]
        locationDict = mapDataToLocationDict(data)
        self.assertEqual(locationDict[(0,0)], 1)
    
    def testFindCheapestRoute(self):
        data = [
            '11',
            '23',
        ]
        locationDict = mapDataToLocationDict(data)
        possibleRoutes = findAllRoutes(locationDict, 0, 0)
        self.assertEqual(
            possibleRoutes,
            [
                [(0, 0), (1, 0), (1, 1)],
                [(0, 0), (0, 1), (1, 1)]
            ]
        )
        self.assertEqual(findCheapestRoute(possibleRoutes, locationDict), 4)
        
    def testFindCheapestRouteExampleTwo(self):  
        data = [
            '116',
            '213',
            '112'
        ]
        locationDict = mapDataToLocationDict(data)
        possibleRoutes = findAllRoutes(locationDict, 0, 0)
        self.assertEqual(
            possibleRoutes,
            [
                [(0, 0), (1, 0), (1, 1)],
                [(0, 0), (0, 1), (1, 1)]
            ]
        )
        self.assertEqual(findCheapestRoute(possibleRoutes, locationDict), 5)

if __name__ == '__main__':
    unittest.main()