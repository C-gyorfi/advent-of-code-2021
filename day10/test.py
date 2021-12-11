import unittest
from readFile import readFile

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completionScores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
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

def getIncompleteLines(lines):
    incompleteLines = []
    for line in lines:
        while '()' in line or '[]' in line or '{}' in line or '<>' in line:
            for bp in ['()', '[]', '{}', '<>']:
                line = line.replace(bp, '')

        indexesOfBadChars = [line.find(')'), line.find(']'), line.find('}'), line.find('>')]
        indexesOfBadChars = [x for x in indexesOfBadChars if x != -1]
        if indexesOfBadChars: continue

        incompleteLines.append(line)

    return incompleteLines

def scoreCompletedLines(lines):
    sum = []
    for line in lines:
        line_sum = 0
        for c in reversed(line):
            line_sum = line_sum * 5 + completionScores[c]
        sum.append(line_sum)
    sum.sort()
    return sum[int(len(sum) / 2)]


class Test(unittest.TestCase):
    def testFindCorruptedLines(self):
        data = readFile("test_data")
        self.assertEqual(sumCorruptedLines(data), 26397)

    def testGetIncompleteLines(self):
        data = readFile("test_data")
        self.assertEqual(getIncompleteLines(data), ['[({([[{{', '({[<{(', '((((<{<{{', '<{[{[{{[[', '<{(['])

    def testSumCompletedLines(self):
        incompleteLines = getIncompleteLines(readFile("test_data"))
        self.assertEqual(scoreCompletedLines(incompleteLines), 288957)

    def testRun(self):
        data = readFile("data")
        self.assertEqual(sumCorruptedLines(data), 339477)

        incompleteLines = getIncompleteLines(readFile("data"))
        self.assertEqual(scoreCompletedLines(incompleteLines), 3049320156)


if __name__ == '__main__':
    unittest.main()