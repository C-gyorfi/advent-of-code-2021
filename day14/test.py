import unittest
from readFile import readFile

def mapRules(data):
    rules = {}
    for line in data:
        line = line.split(' -> ')
        rules[line[0]] = line[1]
    return rules

def incrementValue(values, key):
    try:
        values[key] += 1
    except KeyError:
        values[key] = 1
    return values

def insertValues(rules, initialVale):
    newValue = initialVale[0]
    sumOfValues = { initialVale[0]: 1}
    chars = list(initialVale)
    for i, letter in enumerate(chars):
        try:
            pair = initialVale[i] + initialVale[i+1]
            newValue+=(rules[pair] + initialVale[i+1])
            sumOfValues = incrementValue(sumOfValues, rules[pair])
            sumOfValues = incrementValue(sumOfValues, initialVale[i+1])
        except: continue
    return {'value': newValue, 'sumOfValues': sumOfValues}

def insertValueTimes(rules, initialVale, times):
    result = { 'value': initialVale, 'sumOfValues': {} }
    for _i in range(times):
        result = insertValues(rules, result['value'])
    return result

class Test(unittest.TestCase):
    def testMapRules(self):
        data = readFile('test_data')
        data.pop(0)
        rules = mapRules(data)
        self.assertEqual(rules['CH'], 'B')

    def testInsertValues(self):
        data = readFile('test_data')
        initialValue = data.pop(0) #NNCB
        rules = mapRules(data)
        result = insertValues(rules, initialValue)
        self.assertEqual(result['value'], 'NCNBCHB')

    def testInsertValueTimes(self):
        data = readFile('test_data')
        initialValue = data.pop(0)
        rules = mapRules(data)
        result = insertValueTimes(rules, initialValue, 4)
        self.assertEqual(result['value'], 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB')

    def testSumValues(self):
        data = readFile('test_data')
        initialValue = data.pop(0) #NNCB
        rules = mapRules(data)
        result = insertValueTimes(rules, initialValue, 10)
        self.assertEqual(result['sumOfValues'], {'B': 1749, 'C': 298, 'H': 161, 'N': 865})

    def testRun(self):
        data = readFile('data')
        initialValue = data.pop(0) 
        rules = mapRules(data)
        result = insertValueTimes(rules, initialValue, 10)
        self.assertEqual(result['sumOfValues'], 
            {
                'B': 2253,'C': 3505,'F': 2454,'H': 2324,'K': 840,'N': 2885,'O': 1431,'P': 1137,'S': 530,'V': 2098
            }
        )


if __name__ == '__main__':
    unittest.main()