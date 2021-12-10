# unittest
import unittest
from readFile import readFile

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def sumCorruptedLines(lines):
    sum = 0
    for line in lines:
        while '()' in line or '[]' in line or '{}' in line or '<>' in line:
            for bp in ['()', '[]', '{}', '<>']:
                line = line.replace(bp, '')

        indexesOfBadChars = [line.find(')'), line.find(']'), line.find('}'), line.find('>')]
        indexesOfBadChars = [x for x in indexesOfBadChars if x != -1]
        if not indexesOfBadChars: continue

        indexesOfBadChars.sort()
        sum += scores[line[indexesOfBadChars[0]]]

    return sum

class Test(unittest.TestCase):
    def testFindCorruptedLines(self):
        data = readFile("test_data")
        self.assertEqual(sumCorruptedLines(data), 26397)

    def testRun(self):
        data = readFile("data")
        self.assertEqual(sumCorruptedLines(data), 339477)


if __name__ == '__main__':
    unittest.main()