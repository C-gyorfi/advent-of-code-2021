import unittest
from unittest import result
import numpy as np

def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines

def getDraws(lines):
    numbers = lines[0].split(',')
    return [int(i.strip()) for i in numbers]

def getBoards(lines):
    boards = []
    current_board = []
    for line in lines[1:]:
        if line.strip() == '': continue
        line = [int(i) for i in line.split()]
        current_board.append(line)
        if len(current_board) == 5:
            boards.append(current_board)
            current_board = []
    return boards

def getRows(board):
    rows = []
    current_row = []
    for i in range(len(board)):
      for line in board:
        current_row.append(line[i])
      rows.append(current_row)
      current_row = []
    return rows

def appendIfNotIn(arrayToAppend, array):
    included = False
    for a in arrayToAppend:
      if a == array: included = True
    if not included: arrayToAppend.append(array)

def flatten_array(array):
    return np.array(array).flatten()

def getResult(board, current_draw):
    winning_number = current_draw[-1]
    score = sum(set(flatten_array(board)) - set(current_draw))
    return score * winning_number

def findWinningBoard(boards, draws):
    current_draw = []
    for number in draws:
      current_draw.append(number)
      for board in boards:
        for line in board:
          if all(item in current_draw for item in line):
            return getResult(board, current_draw)
        for row in getRows(board):
          if all(item in current_draw for item in row):
            return getResult(board, current_draw)

def findLastWinningBoard(boards, draws):
    current_draw = []
    winning_boards = []

    for number in draws:
      current_draw.append(number)

      for board in boards:
        rows = getRows(board)
        for line in board:
          if all(item in current_draw for item in line):
            appendIfNotIn(winning_boards, board)
            if len(winning_boards) == len(boards):
              return getResult(board, current_draw)
        for row in rows:
          if all(item in current_draw for item in row):
            appendIfNotIn(winning_boards, board)
            if len(winning_boards) == len(boards):
              return getResult(board, current_draw)


class TestDay4(unittest.TestCase): 
    def testGetDraws(self):
      assert getDraws(read_file('test_data')) == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

    def testGetBoards(self):
      assert getBoards(read_file('test_data'))[0] == [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6,10,3,18 ,5],
        [1,12,20,15,19],
      ]
    
    def testGetRows(self):
      board = [
        [22, 13, 17, 11, 0],
        [8, 2, 23, 4, 24],
        [21, 9, 14, 16, 7],
        [6,10,3,18 ,5],
        [1,12,20,15,19],
      ]
      assert getRows(board) == [[22, 8, 21, 6, 1], [13, 2, 9, 10, 12], [17, 23, 14, 3, 20], [11, 4, 16, 18, 15], [0, 24, 7, 5, 19]]

    def testfindWinningBoard(self):
      lines = read_file('test_data')
      draws = getDraws(lines)
      boards = getBoards(lines)
      assert findWinningBoard(boards, draws) == 4512

    def testLastWinningBoard(self):
      lines = read_file('test_data')
      draws = getDraws(lines)
      boards = getBoards(lines)
      assert findLastWinningBoard(boards, draws) == 1924

    def testPart1(self):
      lines = read_file('data')
      draws = getDraws(lines)
      boards = getBoards(lines)
      result = findWinningBoard(boards, draws)
      print(result)
      assert result == 55770
    
    def testPart2(self):
      lines = read_file('data')
      draws = getDraws(lines)
      boards = getBoards(lines)
      result = findLastWinningBoard(boards, draws)
      print(result)
      assert result == 2980

if __name__ == '__main__':
    unittest.main()