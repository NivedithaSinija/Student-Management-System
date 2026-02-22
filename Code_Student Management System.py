import mysql.connector

db=mysql.connector.connect(host='localhost',user='root',password='*********',database='school_management')
cursor=db.cursor()

def addstudent():
    ID=int(input("Enter Student's ID:"))
    name=input("Enter Student's name:")
    DOB=input("Enter DOB of the student:")
    grade=input("Enter grade:")
    section=input("Enter section:")
    if grade=="11" or grade=="12":
        stream=input("Enter stream:")
        cursor.execute('Insert into student (ID,NAME,DOB,GRADE,SECTION,STREAM) VALUES (%s,%s,%s,%s,%s,%s)',(ID,name,DOB,grade,section,stream))
    else:
        cursor.execute('Insert into student (ID,NAME,DOB,GRADE,SECTION) VALUES (%s,%s,%s,%s,%s)',(ID,name,DOB,grade,section))
    db.commit()
    print('STUDENT ADDED SUCCESSFULLY')

def removestudent():
    ID= int(input("Enter Student's ID:"))
    cursor.execute('DELETE FROM student WHERE ID = %s', (ID,))
    db.commit()
    print('STUDENT REMOVED SUCCESSFULLY')

def addteacher():
    ID=int(input("Enter Teacher's ID:"))
    name=input("Enter Teacher's name:")
    sub= input("Enter Teacher's subject:")
    cursor.execute('INSERT INTO teacher (T_ID,NAME,SUBJECT) VALUES (%s,%s,%s)',(ID,name,sub))
    db.commit()
    print('TEACHER ADDED SUCCESSFULLY')

def removeteacher():
    ID=int(input("Teacher's ID: "))
    cursor.execute('DELETE FROM teacher WHERE T_ID = %s', (ID,))
    db.commit()
    print('TEACHER REMOVED SUCCESSFULLY')

def showstudent():
    cursor.execute("SELECT * FROM student")
    student=cursor.fetchall()
    if student:
        print("List of students:")
        for i in student:
            if i[3]=="11" or i[3]=="12":
                print(f"ID:{i[0]},Name:{i[1]},DOB:{i[2]},Grade:{i[3]},Section:{i[4]},Stream:{i[5]}")
            else:
                print(f"ID:{i[0]},Name:{i[1]},DOB:{i[2]},Grade:{i[3]},Section:{i[4]}")
    else:
        print("NO STUDENTS ENTERED")

def showteacher():
    cursor.execute("SELECT T_ID,NAME,SUBJECT FROM teacher")
    teacher=cursor.fetchall()
    if teacher:
        print("List of teachers:")
        for i in teacher:
            print(f"ID:{i[0]},Name:{i[1]},Subject:{i[2]}")
    else:
        print("NO TEACHERS ENTERED")

def searchstudent():
    ID=int(input("Enter student's ID: "))
    cursor.execute("SELECT GRADE FROM student WHERE ID=%s"%(ID,))
    grade=cursor.fetchone()
    if grade:
        gr=int(grade[0])
        if gr==11 or gr==12:
            cursor.execute("SELECT ID,NAME,DOB,GRADE,SECTION,STREAM FROM student WHERE ID=%s"%(ID,))
        else:
            cursor.execute("SELECT ID,NAME,DOB,GRADE,SECTION FROM student WHERE ID=%s"%(ID,))
        student=cursor.fetchone()
        if gr==11 or gr==12:
            print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}, GRADE: {student[3]}, SECTION: {student[4]}, STREAM: {student[5]}")
        else:
            print(f"ID: {student[0]}, Name: {student[1]}, DOB: {student[2]}, GRADE: {student[3]}, SECTION: {student[4]}")
    else:
        print("STUDENT NOT FOUND")

def searchteacher():
    ID=int(input("Enter teacher's ID: "))
    cursor.execute("SELECT T_ID,NAME,SUBJECT FROM teacher WHERE T_ID=%s", (ID,))
    teacher=cursor.fetchone()
    if teacher:
        print(f"ID: {teacher[0]}, Name: {teacher[1]}, Subject: {teacher[2]}")
    else:
        print("TEACHER NOT FOUND")

def updatestream():
    ID=int(input("Enter student's ID:"))
    cursor.execute("SELECT ID,NAME,DOB,GRADE,SECTION,STREAM FROM student WHERE ID=%s"%(ID,))
    student=cursor.fetchone()
    if student:
        stream=input("Enter new stream chosen:")
        cursor.execute("Update student set stream='%s' where ID=%d"% (stream,ID))
        db.commit()
        print("STREAM UPDATED")
    else:
        print("STUDENT NOT FOUND")


def login():
    print('Login')
    for i in range(3):
        c=0
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username=='sql123pyt' and password=='123':
            print("Login successful\n")
            return True
        else:
            print("Invalid Username and password\n")
            c+=1    
        if c>3:
            return False   

def menu():
    while True:
        print("""
 ---------------------------------------------------
(                                                   )
(   ..     ..    ..       ..      ..     ..      .. )
(..............SCHOOL MANAGEMENT SYSTEM.............)
(   ..     ..    ..       ..      ..     ..      .. )
(                                                   )
 ---------------------------------------------------
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 ===================================================
 ***************************************************
                    MAIN MENU
           
    1.Add new student        6.Show list of teachers

    2.Remove a student       7.Search student

    3.Add new teacher        8.Search teacher

    4.Remove a teacher       9.Update stream

    5.Show list of students  10.Logout
 ***************************************************
 ===================================================
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 """)
        c=int(input("Enter your choice:"))
        if c==1:
            addstudent()
        elif c==2:
            removestudent()
        elif c==3:
            addteacher()
        elif c==4:
            removeteacher()
        elif c==5:
            showstudent()
        elif c==6:
            showteacher()
        elif c==7:
            searchstudent()
        elif c==8:
            searchteacher()
        elif c==9:
            updatestream()
        elif c==10:
            print("Successfully logged out")
            break
        else:
            print("Invalid choice, please try again.\n")
r=login()
if r==True:
    menu()
else:
    print("Login attempt failed")
