#Runtime error,Syntax error,Logical error
#Exception handling try(doubtful code) except(similar to catch block) finally(always be executed(db,file))

try:
	a = 10/0
	print (a)
except ArithmeticError:
	print ("This statement is raising an arithmetic exception.")
finally:   #sqllite_conn.close()  or file.close()
	print ("Success.")