import os, time
import mysql.connector
import webbrowser

username = input("Enter mysql user name: ")
password = input("Enter mysql password: ")

try:
	conn = mysql.connector.connect(host = 'localhost', user = username, passwd= password)
	print("Connected")
	print()
	print("1. Wait, program is opening")
	print("2. You have to enter password again if needed!!")
	
	os.system(f'cmd /c "mysql -u {username} -p < database/students.sql"')

	try:
		os.rename('database/students.sql','database/students-old.sql')
	except:
		pass
                
	
	print("3. Go to 'http://127.0.0.1:6969'")
	
	os.system('cmd /k "python manage.py runserver 6969"')

except Exception as e:
	print(e)
