from distutils.log import error
import datetime
# whoAreyou = input('Enter your Name: ')
# print('Hello ' + whoAreyou)

# className = input('Enter your Class Name: ')
# print('Saved class ' + className)

# classDate = input("Enter your class schdule. /n ex Monday, Wednesday")
# print('Saved schedule' + classDate)

# classTime = input("Enter your class time. /n ex, 10:30")

# classTeacher = input("Enter your Teacher's Name: ")
# print('Saved class ' + classTeacher)

# classRepeat = input('Does your class repeat, /n Yes or no?')
# print('Saved Class' + className + classDate + classTime 'with' + classTeacher)

# whenClassRepeat = input("What time? /n ex. 05-16-2022")
# print('Saved Class' + className + classDate + classTime + 'until' + whenClassRepeat + 'with' + classTeacher)



def class_create():
    className = ""
    while (True):
    
        className = input('Enter your Class Name: ')
        print('Saved class ' + className)
        if (className == ""):
            print('Please enter your Class Name: ')
        else:
            break
    
    return className
 
x= class_create()
print(x)



def class_createA():
    classDate = ""
    dlw = ["M", "T", "W", "TH", "F", "S"]

    while (True):
    
        print("\n[M] Enter M for Monday")
        print("[T] Enter T for Tuesday")
        print("[W] Enter W for Wednesday.")
        print("[TH] Enter TH for Thursday.")
        print("[F] Enter F for Thursday.")
        print("[S] Enter S for Thursday.")
        classDate = input("Enter your class schdule: ")
        
        if classDate in dlw:
            print('Saved schedule ' + classDate)
            break
        else:
            print('Please enter your schdule like this: M (for Monday) ')
    
    return classDate

class_createA()

def class_createB():
    classTime = 0
    hhh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while (True):
        
        classTime = int(input("Enter the hour your class starts. /n ex, 10 for 10:30:"))
        print(classTime, type(classTime))
        if classTime in hhh:
            print('Saved ')
            break
    return classTime

class_createB()

    
def class_createC():
    classTimeM = 0
    mmm = range(60)
    while (True):
        
        classTimeM = int(input("Enter the minutes your class starts. /n ex, 30 for 10:30:"))
        print(classTimeM, type(classTimeM))
        if classTimeM in mmm:
            print('Saved ')
            break
    
    return classTimeM

class_createC()

def class_createD():
    classTeacher = ""
    while (True):
    
        classTeacher = input("Enter your Teacher's Name: ")
        print('Saved class ' + classTeacher)
        if (classTeacher == ""):
            print('Please enter your Class Name: ')
        else:
            break
    
    return classTeacher

class_createD()


