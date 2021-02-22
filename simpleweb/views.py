from django.shortcuts import render,redirect
from django.http import HttpResponse

import mysql.connector as mcdb


# Establishing connection with MySQL Database.
my_connection = mcdb.connect(
    host="localhost", user="root", passwd="0000"
)
mycursor_connection = my_connection.cursor()

# Creating initial Database
mycursor_connection.execute(
    "CREATE DATABASE IF NOT EXISTS School_Management_System_by_KunwarYuvraj"
)
print('Database "School_Management_System_by_KunwarYuvraj" Created!')

# Choosing initial Database to work.
conn = mcdb.connect(host="localhost", user="root", passwd="0000", database='School_Management_System_by_KunwarYuvraj')
print('Successfully connected to database')
cur = conn.cursor()

def index(request):
    return render(request, 'index.html')

def tables(request):
    cur.execute("SELECT * FROM `student`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'tables.html', {'students': data}) 


def categorylisting(request):
    cur.execute("SELECT * FROM `student`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'view.html', {'students': data})  

######################################

def categorycreate(request):
    return render(request, 'add.html')   


def studentadd(request):
    return render(request, 'studentadd.html')   


def categoryaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['txt1']
        # cur.execute("INSERT INTO `tb_category`(`category_name`) VALUES ('{}')".format(catname))
        cur.execute(f"INSERT INTO `tb_category`(`category_name`) VALUES ('{catname}')")
        conn.commit()
        return redirect(categorylisting) 
    else:
        return redirect(categorylisting)

def studentaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        # uid = request.POST['uidz']
        rno = request.POST['rnoz']
        name = request.POST['namez']
        clas = request.POST['classz']
        addr = request.POST['addrz']
        gen = request.POST['genderz']
        pno = request.POST['pnoz']
        email = request.POST['emailz']
        # cur.execute("INSERT INTO `tb_category`(`category_name`) VALUES ('{}')".format(catname))
        cur.execute(f"insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) VALUES ({rno}, '{name}', '{clas}', '{addr}', '{gen}', '{pno}', '{email}')")
        conn.commit()
        return redirect(tables) 
    else:
        return redirect(tables)

################################
def categorydelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_category` where `category_id` = {}".format(id))
    conn.commit()
    return redirect(categorylisting) 


def studentdelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `student` where `UID` = {}".format(id))
    conn.commit()
    return redirect(tables) 
#########################################

def categoryedit(request,id):
     
    print(id)
    cur.execute("select * from `student` where `uid` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'edit.html', {'categories': data})   


def studentedit(request,id):
     
    print(id)
    cur.execute("select * from `student` where `UID` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'studentedit.html', {'students': data})   

############################################################
def categoryupdate(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['txt2']
        cur.execute("update `student` set `Roll_No` ='{}' where `uid`='{}'".format(catname,catid))
        conn.commit()
        return redirect(categorylisting) 
    else:
        return redirect(categorylisting)


def studentupdate(request):
    if request.method == 'POST':
        print(request.POST)
        uid = request.POST.get('uidz')
        # uid = request.POST['uidz']
        rno = request.POST['rnoz']
        name = request.POST['namez']
        clas = request.POST['classz']
        addr = request.POST['addrz']
        gen = request.POST['genderz']
        pno = request.POST['pnoz']
        email = request.POST['emailz']
        cur.execute(f"update `student` set `Roll_No`={rno},`Name` ='{name}', `Class`='{clas}', `Address`='{addr}', `Gender`= '{gen}', `Phone_No` = '{pno}', `Email` = '{email}' where UID = {uid} ")

        # cur.execute("update `student` set `Roll_No`={} where `UID` = {}".format(rno, 1004))
        conn.commit()
        return redirect(tables) 
    else:
        return redirect(tables)