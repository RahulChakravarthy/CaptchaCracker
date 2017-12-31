from AlphaNumeric import AlphaNumeric as Pattern
class Letter():
    __RGBListOfTuples = list()
    __dimension = tuple()

    def __init__(self, RGBlistOfTuples=list, dimension=tuple):
        self.__RGBListOfTuples = RGBlistOfTuples
        self.__dimension = dimension

    def identify(self,):
        for x in range(0, self.__dimension[0], 1):
            for y in range(0, self.__dimension[1], 1):
                pass
