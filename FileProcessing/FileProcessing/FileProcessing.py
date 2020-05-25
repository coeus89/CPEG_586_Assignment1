import sys
from Student import Student

def displayFile():
    fobj = open("S:/Users/Jkara/OneDrive/Documents/CPEG_586/Assignments_Workspace/FileProcessing/FileProcessing/Students.txt", "r")
    for line in fobj:
        print(line)

def copyFile():
    fobj = open("S:/Users/Jkara/OneDrive/Documents/CPEG_586/Assignments_Workspace/FileProcessing/FileProcessing/Students.txt", "r")
    fobj2 = open("S:/Users/Jkara/OneDrive/Documents/CPEG_586/Assignments_Workspace/FileProcessing/FileProcessing/Students2.txt", "w")
    for line in fobj:
        print(line)
        fobj2.write(line)
    fobj2.write("\n12344" + " " + "Gerard" + " " + "Way" + " " + "96" + " " + "89")
    fobj2.close()

def processGrades():
    fobj = open("S:/Users/Jkara/OneDrive/Documents/CPEG_586/Assignments_Workspace/FileProcessing/FileProcessing/Students.txt", "r")
    fobj2 = open("S:/Users/Jkara/OneDrive/Documents/CPEG_586/Assignments_Workspace/FileProcessing/FileProcessing/StudentGrades.txt", "w")
    for line in fobj:
        parts = line.split(" ")
        s1 = Student("","",0)
        s1.id = parts[0]
        s1.firstName = parts[1]
        s1.lastName = parts[2]
        s1.addTestScore(parts[3])
        s1.addTestScore(parts[4])
        s1.grade = s1.computeGrade()
        # now write id and grade to an output file
        fobj2.write(s1.id + " " + s1.lastName + " " + s1.grade + "\n")
    fobj2.close()
    print("done processing processGrades..")


def main():
    displayFile()
    copyFile()
    processGrades()

if __name__ == "__main__":
    sys.exit(int(main() or 0))
