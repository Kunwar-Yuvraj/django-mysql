from django.shortcuts import render,redirect
from django.http import HttpResponse

import mysql.connector as mcdb


conn = mcdb.connect(host="localhost", user="root", passwd="0000", database='School_Management_System_by_KunwarYuvraj')
print('Successfully connected to database')
cur = conn.cursor()

def index(request):
    return render(request, 'index.html')


def tables(request):
    cur.execute("SELECT * FROM `student`")
    data = cur.fetchall()
    print(list(data))
    return render(request, 'tables.html', {'students': data}) 


def studentadd(request):
    return render(request, 'studentadd.html')   


def studentaddprocess(request):
    
    if request.method == 'POST':
        print(request.POST)

        rno = request.POST['rnoz']
        name = request.POST['namez']
        clas = request.POST['classz']
        addr = request.POST['addrz']
        gen = request.POST['genderz']
        pno = request.POST['pnoz']
        email = request.POST['emailz']

        cur.execute(f"insert into student(Roll_no, Name, Class, Address, Gender, Phone_No, Email) VALUES ({rno}, '{name}', '{clas}', '{addr}', '{gen}', '{pno}', '{email}')")
        conn.commit()
        return redirect(tables) 
    else:
        return redirect(tables)


def studentdelete(request,id):
     
    print(id)
    cur.execute("delete from `student` where `UID` = {}".format(id))
    conn.commit()
    return redirect(tables) 


def studentedit(request,id):
     
    print(id)
    cur.execute("select * from `student` where `UID` = {}".format(id))
    data = cur.fetchone()
    print(list(data))
    return render(request, 'studentedit.html', {'students': data})   


def studentupdate(request):

    if request.method == 'POST':
        print(request.POST)
        uid = request.POST.get('uidz')
        rno = request.POST['rnoz']
        name = request.POST['namez']
        clas = request.POST['classz']
        addr = request.POST['addrz']
        gen = request.POST['genderz']
        pno = request.POST['pnoz']
        email = request.POST['emailz']

        cur.execute(f"update `student` set `Roll_No`={rno},`Name` ='{name}', `Class`='{clas}', `Address`='{addr}', `Gender`= '{gen}', `Phone_No` = '{pno}', `Email` = '{email}' where UID = {uid} ")
        conn.commit()
        return redirect(tables) 

    else:
        return redirect(tables)