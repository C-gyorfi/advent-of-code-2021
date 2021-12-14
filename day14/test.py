import unittest
from readFile import readFile
import copy

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

def incrementValueBy(values, key, count):
    try:
        values[key] += count
    except KeyError:
        values[key] = count
    return values

def mapValues(initialVale):
    result = { 'values': {}, 'sumOfChars': {} }
    chars = list(initialVale)
    for i, char in enumerate(chars):
        try:
            result['sumOfChars'] = incrementValue(result['sumOfChars'], char)
            result['values'] = incrementValue(result['values'], initialVale[i] + initialVale[i+1])
        except IndexError:
            continue
    return result

def insertValues(rules, valueMap):
    oldValues = copy.copy(valueMap['values'])
    values = valueMap['values']
    sumOfChars = valueMap['sumOfChars']
    for rule in rules:
        if rule in oldValues:
            count = oldValues[rule]
            values = incrementValueBy(values, rule[0]+rules[rule], count)
            values = incrementValueBy(values, rules[rule]+rule[1], count)
            values[rule] -= count
            sumOfChars = incrementValueBy(sumOfChars, rules[rule], count)
            if values[rule] == 0: del values[rule]
    
    return valueMap

def insertValueTimes(rules, valueMap, times):
    for _i in range(times):
        result = insertValues(rules, valueMap)
    return result

class Test(unittest.TestCase):
    def testMapRules(self):
        data = readFile('test_data')
        data.pop(0)
        rules = mapRules(data)
        self.assertEqual(rules['CH'], 'B')

    def testMapValues(self):
        initialValue = 'ABABC'
        self.assertEqual(mapValues(initialValue)['values'], {'AB': 2, 'BA': 1, 'BC': 1})
        self.assertEqual(mapValues(initialValue)['sumOfChars'], {'A': 2, 'B': 2, 'C': 1})

    def testInsertValues(self):
        data = readFile('test_data')
        initialValue = data.pop(0) #NNCB
        valueMap = mapValues(initialValue)
        self.assertEqual(valueMap['values'], {'CB': 1, 'NC': 1, 'NN': 1})
        self.assertEqual(valueMap['sumOfChars'], {'B': 1, 'C': 1, 'N': 2})
        rules = mapRules(data)
        result = insertValues(rules, valueMap)
        self.assertEqual(result['values'], { 'NC': 1, 'CN': 1, 'NB': 1, 'BC': 1, 'CH': 1, 'HB': 1 })
        self.assertEqual(result['sumOfChars'], { 'N': 2, 'C': 2, 'B': 2, 'H': 1 })

    def testInsertValueTimes(self):
        data = readFile('test_data')
        initialValue = data.pop(0)
        valueMap = mapValues(initialValue)
        rules = mapRules(data)
        result = insertValueTimes(rules, valueMap, 10)
        self.assertEqual(result['sumOfChars'], {'B': 1749, 'C': 298, 'H': 161, 'N': 865})

    def testRun(self):
        data = readFile('data')
        initialValue = data.pop(0) 
        valueMap = mapValues(initialValue)
        rules = mapRules(data)
        result = insertValueTimes(rules, valueMap, 10)
        self.assertEqual(result['sumOfChars'], 
            {
                'B': 2253,'C': 3505,'F': 2454,'H': 2324,'K': 840,'N': 2885,'O': 1431,'P': 1137,'S': 530,'V': 2098
            }
        )

        data = readFile('data')
        initialValue = data.pop(0) 
        valueMap = mapValues(initialValue)
        rules = mapRules(data)
        result = insertValueTimes(rules, valueMap, 40)
        self.assertEqual(result['sumOfChars'], 
            {
                'B': 2327102224376,
                'C': 3609835890592,
                'F': 2438207863681,
                'H': 2449422046565,
                'K': 931567796274,
                'N': 3026949313902,
                'O': 1815342753281,
                'P': 1111290252186,
                'S': 594452039903,
                'V': 2586550746985
            }
        )


if __name__ == '__main__':
    unittest.main()