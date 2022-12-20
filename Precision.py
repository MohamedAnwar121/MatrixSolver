

class Precision:

    @staticmethod
    def sigFigures(noOfSig, number):
        ans = float('%{0}g'.format(noOfSig / 10) % number)
        return ans
