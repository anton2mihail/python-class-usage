class Profile:
    _previousId = 12345
    MAXFRIENDS = 6
    def __init__(self, n, a, c):
        Profile._previousId = Profile._previousId + 1
        self._id = Profile._previousId
        self._name = n
        self._age = a
        self._city = c
        self._relationshipStatus = "It's complicated :|"
        self._profileStatus = "Today is a good day #WesternRocks"
        self._friendsList = []

    def __repr__(self):
        return self._name + " has " +str(len(self._friendsList)) + " friends and lives in " + self._city

    def setRStatus(self, newStat):
        self._relationshipStatus = newStat

    def setPStatus(self, pStat):
        self._profileStatus = pStat

    def getRStatus(self):
        return self._relationshipStatus

    def getPStatus(self):
        return self._profileStatus

    def addFriend(self, pta):
        if len(self._friendsList) < Profile.MAXFRIENDS:
            self._friendsList.append(pta)
        else:
            print("Too many friends!")


