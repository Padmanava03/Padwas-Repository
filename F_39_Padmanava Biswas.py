import mysql.connector as cnt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
con=cnt.connect(host="localhost",user="root",database="student_examination_portal")
def operation(curr):
    x=module()
    if(x==1):
        student(curr)
    if(x==2):
        course(curr)
def module():
    print('Select any one of the modules:\n1.Stuent\n2.Course\n3.Batch\n4.Department\n5.Examination')
    a=int(input("Choice: "))
    return a
def report(a,x,m):
    f=open("Report.txt","a")
    f.write('+--------------+--------------------------------+-----+-----+--------+\n')
    f.write('|')
    f.write(a)
    f.write(' '*(14-len(a)))
    f.write('|')
    f.write(x)
    f.write(' '*(32-len(x)))
    f.write('|')
    f.write('  ')
    f.write(str(m))
    f.write(' |')
    if(m>=90 and m<=100):
        f.write('  A  |')
        f.write(' PASSED |\n')
    elif(m>=80 and m<90):
        f.write('  B  |')
        f.write(' PASSED |\n')
    elif(m>=70 and m<80):
        f.write('  C  |')
        f.write(' PASSED |\n')
    elif(m>=60 and m<70):
        f.write('  D  |')
        f.write(' PASSED |\n')
    elif(m>=50 and m<60):
        f.write('  E  |')
        f.write(' PASSED |\n')
    else:
        f.write('  F  |')
        f.write(' FAILED |\n')
    f.close()
def delfile(k):
    z=open("Report.txt","r")
    for l, line in enumerate(z):
        if k in line:
            break
    z.seek(0)
    g=l+1
    x=z.readlines()
    i=1
    z=open("Report.txt","w")
    for j in x:
        if i!=l:
            z.write(j)
            i+=1
    z.seek(0)
    x=z.readlines()
    for j in x:
        if i!=g:
            z.write(j)
            i+=1
    z.close()
def student(mycur):
    print('-'*50)
    print('Choose what to do in student moddule?\n1.Make a student entry\n2.Update student detail\n3.Remove a student\n4.Generate report card')
    a=int(input("Choice: "))
    if(a==1):
        n=int(input("How many student you want to enter?..."))
        for i in range(1,n+1):
            print('Student entry',i,':')
            st_id=int(input("ID: "))
            st_name=input("Name: ")
            st_roll=int(input("Roll number: "))
            stbatch_id=input("Batch ID: ")
            print('Enter the marks of the following subjects:')
            python=int(input("Python programming: "))
            maths=int(input("Mathematics: "))
            physics=int(input("Physics: "))
            chem=int(input("Chemistry: "))
            eng=int(input("English: "))
            st_marks=(python+maths+physics+chem+eng)//5
            query="Insert into student(stu_id,name,roll,batch_id) VALUES('{}','{}','{}','{}')".format(st_id,st_name,st_roll,stbatch_id)
            try:
                mycur.execute(query)
                con.commit()
                print("Details entered successfully.....")
                report(str(st_id),st_name,st_marks)
            except:
                con.rollback()
                print('Fail to enter the data...the student ID you entered is already registered.....')
    elif(a==2):
        mycur.execute("Select * from student")
        data=mycur.fetchall()
        if (data==[]):
            print('There is no data of students to perform the update operation.....')
        else:
            print("('Student ID', 'Name', 'Class Roll Number', 'Batch ID')")
            for i in data:
                print(i)
            b=int(input('1.Batch ID\n2.Roll number\nWhat you want to update?...'))
            if(b==1):
                t=mycur.rowcount
                n=int(input("How many students detail you want to update?..."))
                if(n>t or n<1):
                    print("Out of range.....")
                else:
                    for i in range(1,t+1):
                        st_id=int(input("Student ID: "))
                        mycur.execute("Select stu_id from student where stu_id='{}'".format(st_id))
                        d=mycur.fetchall()
                        if not d:
                            print("There is no data of",st_id,"is avaible.....")
                        else:
                            stbatch_id=input("Batch ID: ")
                            c=input('Are you sure you want to update?...y/n...')
                            if(c=='y' or c=='Y'):
                                query="Update student set batch_id='{}' where stu_id='{}'".format(stbatch_id,st_id)
                                try:
                                    mycur.execute(query)
                                    con.commit()
                                    print("Details updated successfully.....")
                                except:
                                    con.rollback()
            else:
                t=mycur.rowcount
                n=int(input("How many students detail you want to update?..."))
                if(n>t or n<1):
                    print("Out of range.....")
                else:
                    for i in range(1,t+1):
                        st_id=input("Student ID: ")
                        mycur.execute("Select stu_id from student where stu_id='{}'".format(st_id))
                        d=mycur.fetchall()
                        if not d:
                            print("There is no data of",st_id,"is avaible.....")
                        else:
                            st_roll=int(input("Roll number: "))
                            c=input('Are you sure you want to update?...y/n...')
                            if(c=='y' or c=='Y'):
                                query="Update student set roll='{}' where stu_id='{}'".format(st_roll,st_id)
                                try:
                                    mycur.execute(query)
                                    con.commit()
                                    print("Details updated successfully.....")
                                except:
                                    con.rollback()
    elif(a==3):
        mycur.execute("Select * from student")
        data=mycur.fetchall()
        if (data==[]):
            print('There is no data of students to perform the remove operation.....')
        else:
            print("('Student ID', 'Name', 'Class Roll Number', 'Batch ID')")
            for i in data:
                print(i)
            t=mycur.rowcount
            n=int(input("How many students you want to remove?..."))
            if(n>t or n<1):
                print("Out of range.....")
            else:
                for i in range(1,t+1):
                    st_id=int(input("Student ID: "))
                    mycur.execute("Select stu_id from student where stu_id='{}'".format(st_id))
                    d=mycur.fetchall()
                    if not d:
                        print("There is no data of",st_id,"is avaible.....")
                    else:
                        c=input('Are you sure you want to delete?...y/n...')
                        if(c=='y' or c=='Y'):
                            query="Delete from student where stu_id='{}'".format(st_id)
                            try:
                                mycur.execute(query)
                                con.commit()
                                print("Details deleted successfully.....")
                                delfile(str(st_id))
                            except:
                                con.rollback()
    elif(a==4):
        f=0
        z=open("Report.txt","r")
        y=z.read()
        for i in y:
            if (i.isdigit()):
                f=1
                break
        if(f==0):
            print('There is no data to generate a report card.....')
        else:
            z=open("Report.txt","a")
            z.write('+--------------+--------------------------------+-----+-----+--------+\n')
            z=open("Report.txt","r")
            print(z.read())
        z.close()
def python(mycurr,i,n,r,m):
    query="Insert into python(std_id,name,roll_no,marks) VALUES('{}','{}','{}','{}')".format(i,n,r,m)
    try:
        mycurr.execute(query)
        con.commit()
    except:
        con.rollback()
def physics(mycurr,i,n,r,m):
    query="Insert into physics(std_id,name,roll_no,marks) VALUES('{}','{}','{}','{}')".format(i,n,r,m)
    try:
        mycurr.execute(query)
        con.commit()
    except:
        con.rollback()
def chem(mycurr,i,n,r,m):
    query="Insert into chem(std_id,name,roll_no,marks) VALUES('{}','{}','{}','{}')".format(i,n,r,m)
    try:
        mycurr.execute(query)
        con.commit()
    except:
        con.rollback()
def maths(mycurr,i,n,r,m):
    query="Insert into maths(std_id,name,roll_no,marks) VALUES('{}','{}','{}','{}')".format(i,n,r,m)
    try:
        mycurr.execute(query)
        con.commit()
    except:
        con.rollback()
def eng(mycurr,i,n,r,m):
    query="Insert into eng(std_id,name,roll_no,marks) VALUES('{}','{}','{}','{}')".format(i,n,r,m)
    try:
        mycurr.execute(query)
        con.commit()
    except:
        con.rollback()
def course_stats(mycurr):
    mycurr.execute("Select * from python")
    data=mycurr.fetchall()
    if(data==[]):
        print('There is no data available right now.....')
    else:
        print('*'*100)
        print('\t\t\t                 PYTHON PROGRAMMING(C001)                 \n')
        print("\t\t\t('Student ID', 'Name', 'Class Roll Number', 'Marks')")
        for k in data:
            print("\t\t\t",k)
        print('\n')
        print('*'*100)
    mycurr.execute("Select * from physics")
    data=mycurr.fetchall()
    if(data!=[]):
        print('\t\t\t                     PHYSICS(C002)                   \n')
        print("\t\t\t('Student ID', 'Name', 'Class Roll Number', 'Marks')")
        for k in data:
            print("\t\t\t",k)
        print('\n')
        print('*'*100)
    mycurr.execute("Select * from chem")
    data=mycurr.fetchall()
    if(data!=[]):
        print('\t\t\t                     CHEMISTRY(C003)                    \n')
        print("\t\t\t('Student ID', 'Name', 'Class Roll Number', 'Marks')")
        for k in data:
            print("\t\t\t",k)
        print('\n')
        print('*'*100)
    mycurr.execute("Select * from maths")
    data=mycurr.fetchall()
    if(data!=[]):
        print('\t\t\t                     MATHEMATICS(C004)                    \n')
        print("\t\t\t('Student ID', 'Name', 'Class Roll Number', 'Marks')")
        for k in data:
            print("\t\t\t",k)
        print('\n')
        print('*'*100)
    mycurr.execute("Select * from eng")
    data=mycurr.fetchall()
    if(data!=[]):
        print('\t\t\t                     ENGLISH(C005)                    \n')
        print("\t\t\t('Student ID', 'Name', 'Class Roll Number', 'Marks')")
        for k in data:
            print("\t\t\t",k)
        print('\n')
        print('*'*100)
def course_stcs(mycurr):
    mycurr.execute("Select * from student")
    data=mycurr.fetchall()
    if (data==[]):
        print('There is no data of students to show the course statistics.....')
    else:
        id=[]
        Marks=[]
        Grades=[]
        query="Select * from python"
        mycurr.execute(query)
        data=mycurr.fetchall()
        for i in data:
            id.append(i[0])
        for i in range(0,len(id)):
            query="Select(select SUM(marks) FROM python WHERE std_id=('{}'))+(select SUM(marks) FROM physics WHERE std_id=('{}'))+(select SUM(marks) FROM chem WHERE std_id=('{}'))+(select SUM(marks) FROM maths WHERE std_id=('{}'))+(select SUM(marks) FROM eng WHERE std_id=('{}')) as RESULT".format(id[i],id[i],id[i],id[i],id[i])
            mycurr.execute(query)
            data=mycurr.fetchall()
            for j in data:
                Marks.append(j[0]//5)
        for i in range(0,len(Marks)):
            if(Marks[i]>=90 or Marks[i]<=100):
                Grades.append('A')
            elif(Marks[i]>=80 or Marks[i]<90):
                Grades.append('B')
            elif(Marks[i]>=70 or Marks[i]<80):
                Grades.append('C')
            elif(Marks[i]>=60 or Marks[i]<70):
                Grades.append('D')
            elif(Marks[i]>=50 or Marks[i]<=60):
                Grades.append('E')
            else:
                Grades.append('F')
        g=np.array(Grades)
        # Creating histogram
        fig, axs = plt.subplots(1, 1,figsize =(5,6),tight_layout = True)
        axs.set_facecolor("black")
        # Remove x, y ticks
        axs.xaxis.set_ticks_position('none')
        axs.yaxis.set_ticks_position('none')
        # Add padding between axes and labels
        axs.xaxis.set_tick_params(pad = 5)
        axs.yaxis.set_tick_params(pad = 10)
        # Add x, y gridlines
        axs.grid(visible = True, color ='grey',linestyle ='-.', linewidth = 0.5,alpha = 0.6)
        # Add text watermark
        fig.text(0.9, 0.15, 'F-39 Padmanava Biswas',fontsize = 12,color ='red',ha ='right',va ='bottom',alpha = 0.7)
        # Creating histogram
        N,bins,patches=axs.hist(g,bins=['A','B','C','D','E','F'])
        # Setting color
        fracs=((N**(1 / 5)) / N.max())
        norm=colors.Normalize(fracs.min(), fracs.max())
        for thisfrac,thispatch in zip(fracs, patches):
            color=plt.cm.viridis(norm(thisfrac))
            thispatch.set_facecolor(color)
        # Adding extra features
        plt.xlabel("Grades",fontweight='bold')
        plt.ylabel("Number of students",fontweight='bold')
        plt.title('Nnumber of students v/s Grades')
        plt.show()
def course(mycur):
    print('-'*50)
    print('Choose what to do in course module?\n1.Enroll a student in a course\n2.View performance of all students in the course\n3.Show course statistics')
    a=int(input("Choice: "))
    if(a==1):
        mycur.execute("Select * from student")
        data=mycur.fetchall()
        if (data==[]):
            print('There is no data of students to perform the enroll operation.....')
        else:
            n=int(input('How many students you want to enroll in the courses?...'))
            for k in range(n):
                st_id=int(input('Student ID: '))
                mycur.execute("Select stu_id from student where stu_id='{}'".format(st_id))
                d=mycur.fetchall()
                if not d:
                    print("The following student ID",st_id,"hasn't benn registered.....")
                else:
                    st_name=input('Student name: ')
                    st_roll=int(input('Roll. no.: '))
                    l=['C001','C002','C003','C004','C005']
                    v=['Python Programming','Physics','Chemistry','Mathematics','English']
                    for j in range(5):
                        print('Enter marks obtained by student',st_id,'in',v[j],', Course ID:',l[j])
                        st_marks=int(input('Marks obtained: '))
                        if(l[j]=='C001'):
                            python(mycur,st_id,st_name,st_roll,st_marks)
                        elif(l[j]=='C002'):
                            physics(mycur,st_id,st_name,st_roll,st_marks)
                        elif(l[j]=='C003'):
                            chem(mycur,st_id,st_name,st_roll,st_marks)
                        elif(l[j]=='C004'):
                            maths(mycur,st_id,st_name,st_roll,st_marks)
                        elif(l[j]=='C005'):
                            eng(mycur,st_id,st_name,st_roll,st_marks)
    elif(a==2):
        course_stats(mycur)
    elif(a==3):
        course_stcs(mycur)
if con.is_connected():
    cur=con.cursor()
    operation(cur)
    while True:
        print('-'*50)
        a=input('Want to perform any other operations?...y/n...')
        if(a=='y' or a=='Y'):
            operation(cur)
        else:
            print('THANK YOU. HAVE A GREAT DAY SIR :)')
            break
else:
    print('Sorry not able to connect.....')