class Student:
    _lastStudentNumber = 250650110
    MAXCOURSES = 5

    def __init__(self, fName="kemi", lName="Ola"):
        self._firstName = fName
        self._lastName = lName
        self._fullName = fName + " "+ lName
        self._listOfCourses = []
        Student._lastStudentNumber = Student._lastStudentNumber + 1
        self._studentNumber = Student._lastStudentNumber

    def getName(self):
        return self._fullName

    def getStudentNumber(self):
        return self._studentNumber

    def addCourse(self, cName):
        if(len(self._listOfCourses) < Student.MAXCOURSES):
            self._listOfCourses.append(cName)
        else:
            print("****You cannot have that many courses****")

    def printStudent(self):
        print("*************")
        print("Name:", self._fullName)
        print("Student #: ", self._studentNumber)
        if (len(self._listOfCourses) > 0):
            print("The student is enrolled in the following courses:")
            for c in self._listOfCourses:
                print(c, end=" | ")
            print()
        else:
            print("The student is not enrolled in any courses!")