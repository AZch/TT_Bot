class OneScore():
    def __init__(self, first, second, whatSet):
        self.first = first
        self.second = second
        self.whatSet = whatSet
        pass

    def getFirstScore(self):
        return self.first
    def getSecondScore(self):
        return self.second
    def isZero(self):
        if (self.first + self.second == 0):
            return True
        else:
            return False
    def getCountSet(self):
        return self.whatSet
    def isMode(self):
        return self.more
    def getWhatMore(self):
        return self.whatMore