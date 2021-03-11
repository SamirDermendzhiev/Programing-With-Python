import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-test_1', help="Run test case 1", action='store_const', default=False, const=True)
parser.add_argument('-test_2', help="Run test case 2", action='store_const', default=False, const=True)
parser.add_argument('-test_3', help="Run test case 3", action='store_const', default=False, const=True)
parser.add_argument('-test_4', help="Run test case 4", action='store_const', default=False, const=True)
args = parser.parse_args()

class AdjacentFinder:
    colors = []

    def __init__(self, file):
        #count the
        self.currentCount = 0
        self.highestCount = 0
        #read the file
        self.open_file(file)

    def open_file(self, File):
        with open(File) as file:
            #get the first row
            dimentions = file.readline().rstrip().split(" ")
            #save width and height
            self.height = int(dimentions[0])
            self.width = int(dimentions[1])

            #read the lines of the file and store them
            for line in file:
                lineelements = line.rstrip().split(" ")
                self.colors.append(lineelements)

    #Main algoryth function
    def findSequence(self):
        #read every element in clors
        for row in range(self.height):
            for col in range(self.width):
                #if its empty skip
                if self.colors[row][col] != "":
                    #get the color we are looking for, empty the element and send it to be checked
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
        #we get an array of positions to check their adjacent positions
        #and return an array with the adjacent colors matching the one we are looking for to keep checking
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


#test case 1
if (args.test_1 == True):
    File = "./tests/test_1"
    Colors = AdjacentFinder(File)
    Colors.findSequence()

# test case 2
if (args.test_2 == True):
    File = "./tests/test_2"
    Colors = AdjacentFinder(File)
    Colors.findSequence()

#test case 3
if (args.test_3 == True):
    File = "./tests/test_3"
    Colors = AdjacentFinder(File)
    Colors.findSequence()

#test case 4
if (args.test_4 == True):
    File = "./tests/test_4"
    Colors = AdjacentFinder(File)
    Colors.findSequence()
