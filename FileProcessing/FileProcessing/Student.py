
class Student:
    def __init__(self, firstName, lastName, id):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.tests = []
        self.grade = ""
    
    def addTestScore(self, score):
        self.tests.append(score)
    
    def computeGrade(self):
        sum1 = 0
        for testscore in self.tests:
            sum1 += int(testscore)
        avg = sum1/len(self.tests)
        grade = ""
        if avg > 90:
            grade = "A"
        elif avg > 85:
            grade = "A-"
        elif avg > 80:
            grade = "B"
        else:
            grade = "B-"
        return grade
