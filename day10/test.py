# unittest
import unittest
from readFile import readFile

def containsChar(char, string):
    try: return string.index(char)
    except ValueError:
        return None

def sumCorruptedLines(lines):
    sum = 0
    for line in lines:
        while '()' in line or '[]' in line or '{}' in line or '<>' in line:
            line = line.replace('()', '')
            line = line.replace('[]', '')
            line = line.replace('<>', '')
            line = line.replace('{}', '')

        badChars = [line.find(')'), line.find(']'), line.find('}'), line.find('>')]
        badChars = [x for x in badChars if x != -1]
        if len(badChars) == 0: continue
        badChars.sort()
        if line[badChars[0]] == ')': sum += 3
        elif line[badChars[0]] == ']': sum += 57
        elif line[badChars[0]] == '}': sum += 1197
        elif line[badChars[0]] == '>': sum += 25137  
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