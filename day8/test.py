# unittest
from typing import NoReturn
import unittest
from readFile import readFile

NUMBERS = {
    0: 'abcefg',
    9: 'abcdfg',
    6: 'abdefg',
    1: 'cf',
    3: 'acdfg',
    2: 'acdeg',
    5: 'abdfg',
    4: 'bcdf',
    7: 'acf',
    8: 'abcdefg',
}

def getValues(raw_data):
    result = []
    for line in raw_data:
        input_output = line.split('|')
        input = sorted(input_output[0].split())
        output = input_output[1].split() 
        this_record = {}
        this_record['input'] = sorted(input, key=len)
        this_record['output'] = output
        result.append(this_record)  

    return result

def findEasyNumbers(values):
    result = 0
    for record in values:
        for n in record['output']:
            if len(n) == 2: result += 1
            if len(n) == 4: result += 1
            if len(n) == 3: result += 1
            if len(n) == 7: result += 1
    return result

def sortString(string):
    array = list(string)
    array.sort()
    return ''.join(array)

def decodeLine(line):
    result = ''
    numbers = {}
    difficult_numbers = []
    five_and_two = []
    for n in line['input']:
        sorted_n = sortString(n)
        if len(n) == 2: 
            numbers[1] = sorted_n
        elif len(n) == 3: 
            numbers[7] = sorted_n
        elif len(n) == 4: 
            numbers[4] = sorted_n
        elif len(n) == 7: 
            numbers[8] = sorted_n
        else:
            difficult_numbers.append(sorted_n)
    for dn in difficult_numbers:
        if len(dn) == 5:
            if numbers[7][0] in dn and numbers[7][1] in dn and numbers[7][2] in dn:
                numbers[3] = dn
            else:
                five_and_two.append(dn)
        elif len(dn) == 6:
            if (numbers[1][0] in dn and numbers[1][1] not in dn) or (numbers[1][1] in dn and numbers[1][0] not in dn):
                numbers[6] = dn
            elif numbers[4][0] in dn and numbers[4][1] in dn and numbers[4][2] in dn and numbers[4][3] in dn:
                numbers[9] = dn
            else:
                numbers[0] = dn
    for f in five_and_two:
        if len(set(f+numbers[6])) == 6:
            numbers[5] = f
        else:
            numbers[2] = f
    inv_map = {v: k for k, v in numbers.items()}
    for o in line['output']:
        o = sortString(o)
        result+=f'{inv_map[o]}'
    return int(result)

def sumAllNumbers(values):
    result = 0
    for record in values:
        result += decodeLine(record)
    return result

class Test(unittest.TestCase):
    def testGetValues(self):
        values = getValues(readFile('test_data'))
        self.assertEqual(values[0]['input'], ['be', 'edb', 'cgeb', 'fabcd', 'fdcge', 'fecdb', 'agebfd', 'cbdgef', 'fgaecd', 'cfbegad'])
        self.assertEqual(values[0]['output'], ['fdgacbe', 'cefdb', 'cefbgd', 'gcbe'])
        self.assertEqual(values[-1]['input'], ['gf', 'gcf', 'gaef', 'ecagb', 'fdbac', 'gcafb', 'abcdeg', 'cafbge', 'fegbdc', 'dcaebfg'])
        self.assertEqual(values[-1]['output'], ['fgae', 'cfgab', 'fg', 'bagce'])

    def testFindEasyNumbers(self):
        values = getValues(readFile('data'))
        self.assertEqual(findEasyNumbers(values), 488)

    def testDecodeLine(self):
        values = getValues(["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"])[0]
        self.assertEqual(decodeLine(values), 5353)

    def testSumAllNumbers(self):
        values = getValues(readFile('test_data'))
        self.assertEqual(sumAllNumbers(values), 61229)

        values = getValues(readFile('data'))
        self.assertEqual(sumAllNumbers(values), 1040429)

if __name__ == '__main__':
    unittest.main()