import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-test_1', help="Run test case 1", action='store_const', default=False, const=True)
parser.add_argument('-test_2', help="Run test case 2", action='store_const', default=False, const=True)
parser.add_argument('-test_3', help="Run test case 3", action='store_const', default=False, const=True)
parser.add_argument('-test_4', help="Run test case 4", action='store_const', default=False, const=True)
args = parser.parse_args()

class AdjacentFinder:
    height = None
    width = None
    colors = []

    def __init__(self, file):
        self.currentCount = 0
        self.highestCount = 0
        self.open_file(file)

    def open_file(self, File):
        with open(File) as file:
            dimentions = file.readline().rstrip().split(" ")
            self.height = int(dimentions[0])
            self.width = int(dimentions[1])

            for line in file:
                lineelements = line.rstrip().split(" ")
                self.colors.append(lineelements)

    def findSequence(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.colors[row][col] != "":
                    value = self.colors[row][col]
                    self.colors[row][col] = ""
                    positionsToCheck = [[row, col]]
                    while (len(positionsToCheck) != 0):
                        positionsToCheck = self.checkAdgecent(positionsToCheck, value)

                if self.currentCount > self.highestCount:
                    self.highestCount = self.currentCount

                self.currentCount = 0

        print(self.highestCount)

    def checkAdgecent(self, arrayToCheck, value):

        colors = self.colors
        returnToCheck = []

        for element in arrayToCheck:
            row = element[0]
            col = element[1]
            self.currentCount += 1
            if (row - 1 >= 0) and (colors[row - 1][col] == value):
                colors[row - 1][col] = ""
                returnToCheck.append([row - 1, col])
            if (col - 1 >= 0) and (colors[row][col - 1] == value):
                colors[row][col - 1] = ""
                returnToCheck.append([row, col - 1])
            if (row + 1 < self.height) and (colors[row + 1][col] == value):
                colors[row + 1][col] = ""
                returnToCheck.append([row + 1, col])
            if (col + 1 < self.width) and (colors[row][col + 1] == value):
                colors[row][col + 1] = ""
                returnToCheck.append([row, col + 1])

        return returnToCheck



if (args.test_1 == True):
    File = "./tests/test_1"
    Colors = AdjacentFinder(File)
    Colors.findSequence()
if (args.test_2 == True):
    File = "./tests/test_2"
    Colors = AdjacentFinder(File)
    Colors.findSequence()
if (args.test_3 == True):
    File = "./tests/test_3"
    Colors = AdjacentFinder(File)
    Colors.findSequence()
if (args.test_4 == True):
    File = "./tests/test_4"
    Colors = AdjacentFinder(File)
    Colors.findSequence()
