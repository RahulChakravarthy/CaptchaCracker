from numpy.core.test_rational import lcm

from AlphaNumeric import AlphaNumeric as Pattern


class Letter:
    __RGBListOfTuples = list(list())
    __dimension = tuple()   # (X width, Y height)

    def __init__(self, RGBlistOfTuples=list(list()), dimension=tuple()):
        self.__RGBListOfTuples = RGBlistOfTuples
        self.__dimension = dimension

    # Scales the size of the RGB list to the specified size of the incoming x and y parameters and returns the new list
    # Scales the incoming RGB list as well if there isn't an easy ratio to modify current letter RGB list
    def __scaleSize(self, __charValueToScale=list(list())):
        __RGBListOfTuplesChange = self.__RGBListOfTuples # Don't want to modify the current object RGB list so make copy of it

        __RGBListSizeX = self.__dimension[0]
        __RGBListSizeY = self.__dimension[1]

        __charValueToScaleSizeX = len(__charValueToScale[0])
        __charValueToScaleSizeY = len(__charValueToScale)

        # Scale length/x value first
        totalXLength = lcm(__RGBListSizeX, __charValueToScaleSizeX)

        # Scale the current RGB list
        for rowIndex, rowValue in enumerate(__RGBListOfTuplesChange):
            __RGBListOfTuplesChange[rowIndex] = [rgbCode for rgbCode in rowValue for _ in range(int(totalXLength/__RGBListSizeX))]
        # Scale the incoming charValue list
        for rowIndex, rowValue in enumerate(__charValueToScale):
            __RGBListOfTuplesChange[rowIndex] = [rgbCode for rgbCode in rowValue for _ in range(int(totalXLength/__charValueToScaleSizeX))]

        # Scale height/y value next
        totalYHeight = lcm(__RGBListSizeY, __charValueToScaleSizeY)

        # Scale the current RGB list
        for columnIndex, columnValue in enumerate(__RGBListOfTuplesChange):
            __RGBListOfTuplesChange[:][columnIndex] = [rgbCode for rgbCode in columnValue for _ in range(int(totalYHeight / __RGBListSizeY))]
        # Scale the incoming charValue list
        for columnIndex, columnValue in enumerate(__charValueToScale):
            __RGBListOfTuplesChange[:][columnIndex] = [rgbCode for rgbCode in rowValue for _ in range(int(totalYHeight / __charValueToScaleSizeY))]

        return __charValueToScale,__RGBListOfTuplesChange

    def identify(self):
        characterList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                         "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        characterValue = [Pattern.A, Pattern.B, Pattern.C, Pattern.D, Pattern.E, Pattern.F, Pattern.G, Pattern.H,
                          Pattern.I, Pattern.J, Pattern.K, Pattern.L, Pattern.M, Pattern.N,
                          Pattern.O, Pattern.P, Pattern.Q, Pattern.R, Pattern.S, Pattern.T, Pattern.U, Pattern.V,
                          Pattern.W, Pattern.X, Pattern.Y, Pattern.Z, Pattern.ZERO, Pattern.ONE, Pattern.TWO,
                          Pattern.THREE, Pattern.FOUR, Pattern.FIVE, Pattern.SIX, Pattern.SEVEN, Pattern.EIGHT,
                          Pattern.NINE]
        charCombinations = dict(zip(characterList, characterValue))
        charFitness = dict.fromkeys(characterList, 0)
        for charIndex, charValue in charCombinations.items():
            __scaledCharValue, __scaledCurrRGBList = self.__scaleSize(charValue)
            fitness = 0
            for x in range(0, len(__scaledCharValue[0]), 1):
                for y in range(0, len(__scaledCharValue), 1):
                    if __scaledCurrRGBList[y][x] is __scaledCharValue[y][x]:
                        fitness += 1

            charFitness[charIndex] = fitness / (len(__scaledCharValue[0]) * len(__scaledCharValue)) # Scales the fitness based on size of entire captcha, to keep measurements accurate

        return max(charFitness, key=lambda n: charFitness.get(n))

