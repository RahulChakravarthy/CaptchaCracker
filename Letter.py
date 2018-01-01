from AlphaNumeric import AlphaNumeric as Pattern


class Letter():
    __RGBListOfTuples = list()
    __dimension = tuple()

    def __init__(self, RGBlistOfTuples=list, dimension=tuple):
        self.__RGBListOfTuples = RGBlistOfTuples
        self.__dimension = dimension

    # Scales the size of the RGB list to the specified size of the incoming x and y parameters and returns the new list
    # Scales the incoming RGB list as well if there isn't an easy ratio to modify current letter RGB list
    def __scaleSize(self, __charValueToScale=list()):
        return __charValueToScale, self.__RGBListOfTuples

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

        for charIndex, charValue in charCombinations.items():
            __scaledCharValue, __scaledCurrRGBList = self.__scaleSize(charValue)
            fitness = 0
            for x in range(0, len(__scaledCharValue[0]), 1):
                for y in range(0, len(__scaledCharValue), 1):
                    # Implement some form of pixel comparison algorithm to determine if the template pixel position is similar to the newRGBlist pixel position
                    if __scaledCurrRGBList[y][x] == __scaledCharValue[y][x]:
                        fitness += 1

            if fitness < 40:  # if the overall match of the newRGBList is way off the current letter template, remove it from the possible combination list.
                del charCombinations[charIndex]

        return charCombinations.popitem()
