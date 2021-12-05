import unittest
from unittest import result

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines

def getMostFrequentChar(lines, position):
  zero = 0
  one = 0
  for line in lines:
    if line[position] == "1": one += 1
    if line[position] == "0": zero += 1
  return "1" if one >= zero else "0"

def getLeastFrequentChar(lines, position):
  zero = 0
  one = 0
  for line in lines:
    if line[position] == "1": one += 1
    if line[position] == "0": zero += 1
  return "0" if zero <= one else "1"

def filterLinesByChar(lines, char, position):
  return [line.strip() for line in lines if line[position] == char]

def getArrayOfMostFrequentChars(lines):
  most_frequent_chars = []
  line_length = len(lines[0].strip())
  for i in range(line_length):
    most_frequent_chars.append(getMostFrequentChar(lines, i))
  return most_frequent_chars

def getArrayOfLeastFrequentChars(lines):
  chars = []
  line_length = len(lines[0].strip())
  for i in range(line_length):
    chars.append(getLeastFrequentChar(lines, i))
  return chars

def getNumberByMostFrequent(lines, position):
  if len(lines) == 1: return lines[0]

  most_frequent_chars = getArrayOfMostFrequentChars(lines)
  lines = filterLinesByChar(lines, most_frequent_chars[position], position)
  return getNumberByMostFrequent(lines, position+1)

def getNumberByLeastFrequent(lines, position):
  if len(lines) == 1: return lines[0]

  chars = getArrayOfLeastFrequentChars(lines)
  lines = filterLinesByChar(lines, chars[position], position)
  return getNumberByLeastFrequent(lines, position+1)

class TestDay3(unittest.TestCase): 
    def testGetMostFrequentChar(self):
      lines = [
        "00100\n",
        "11110\n",
        "10110\n",
        "10111\n",
        "10101\n",  
        "01111\n",
        "00111\n",
        "11100\n",
        "10000\n",
        "11001\n",
        "00010\n",
        "01010\n",
      ]
      assert getMostFrequentChar(lines, 0) == "1"
      assert getMostFrequentChar(lines, 1) == "0"
      assert getMostFrequentChar(lines, 2) == "1"

    def testFilterLinesStartWithChar(self):
      lines = [
        "00100\n",
        "11110\n",
        "10110\n",
        "10111\n",
        "10101\n",  
        "01111\n",
        "00111\n",
        "11100\n",
        "10000\n",
        "11001\n",
        "00010\n",
        "01010\n",
      ]
      filtered_first = filterLinesByChar(lines, "1", 0)
      assert len(filtered_first) == 7
      assert len(filterLinesByChar(filtered_first, "0", 1)) == 4

    def testGetArrayOfMostFrequentChars(self):
      lines = [
        "0010\n",
        "1110\n",
        "1011\n",
        "1011\n",
      ]
      assert getArrayOfMostFrequentChars(lines) == ["1", "0", "1", "1"]

    def testGetNumberByMostFrequent(self):
      lines = [
        "00100\n",
        "11110\n",
        "10110\n",
        "10111\n",
        "10101\n",  
        "01111\n",
        "00111\n",
        "11100\n",
        "10000\n",
        "11001\n",
        "00010\n",
        "01010\n",
      ]
      number = getNumberByMostFrequent(lines, 0)
      assert number == '10111'
      assert int(number, 2) == 23

    def testGetNumberByLestFrequent(self):
      lines = [
        "00100\n",
        "11110\n",
        "10110\n",
        "10111\n",
        "10101\n",  
        "01111\n",
        "00111\n",
        "11100\n",
        "10000\n",
        "11001\n",
        "00010\n",
        "01010\n",
      ]
      number = getNumberByLeastFrequent(lines, 0)
      assert number == '01010'
      assert int(number, 2) == 10

    def testFinal(self):
      lines = read_file('data')
      most_frequent_number = getNumberByMostFrequent(lines, 0)
      least_frequent_number = getNumberByLeastFrequent(lines, 0)
      print(int(most_frequent_number, 2) * int(least_frequent_number, 2))
      assert 1 == 1

if __name__ == '__main__':
    unittest.main()