#!/usr/bin/env python
import tkinter as tk

global minus
minus = False

#Stores the input expression
global expression
expression = []

#class which manages the arithmetics and shows the output to reader
class inputstring:
	def __init__(self,root):
		self.number1 = 0
		self.number2 = 0
		self.operator = None
		self.ans = 0        
		self.label = tk.Label(root,text = "0",width = 16,bg= "white",fg="black",justify = tk.LEFT)    
		self.label.grid(row = 0,column = 0,columnspan =3)

	#method which generates number
	def generate(self,n):
		expression.append(n)
		inp.number1 = (inp.number1*10) + n
		print(expression)

	#clears everything
	def clearcommand(self):
		inp.number1 = 0
		inp.number2 = 0
		inp.operator = None
		inp.ans = 0
		global expression
		del expression[:]
		inp.label["text"] = "0"

	#To be continued 
	"""def backspace(self):
		if len(expression)!= 0 :
			c = expression[-1]
			if type(c) == int :
				inp.number1 = int(inp.number1/10)
				expression.pop()
			if type(c) == str :
				inp.operator = None 
				flag = None
				for i in range(len(expression)-2,-1,-1):
					if type(expression[i]) == str and expression[i]!='=':
						flag = expression[i]
						break
				if flag != None :
					print("yo" + flag)
					inp.operator = flag
				else :
					inp.operator = None
				expression.pop()
	"""

	#method which directs the output
	def getoutput(self,n):
		inp.label["text"] = str(n)

	#operator assignment
	def assignoperator(self,c):
		expression.append(c)
		if c!='=' :
			if c == '-' and inp.number1 == 0:
				global minus
				minus = True
			else :
				if inp.number1 != 0 and inp.number2 != 0 : 
					inp.operation()
					inp.number2 = inp.ans
					inp.number1 = 0
				else :
					inp.number2 = inp.number1
					inp.number1 = 0
			inp.operator = c
		else :
			if inp.number2 != 0 :
				print(inp.number1,inp.number2)
				inp.operation()
				inp.number1 = inp.ans
				inp.getoutput(inp.ans)
				print(inp.ans)
			else :
				if minus == True: 
					inp.number1 = -inp.number1
					print(inp.number1)
				else :
					print(inp.number1)
		print(expression)            

	#Arithmetic
	def operation(self):
		c = self.operator
		if c == '+':
			inp.ans = inp.number2 + inp.number1
		elif c == '-':
			inp.ans = inp.number2 - inp.number1
		elif c == '*':
			inp.ans = inp.number2 * inp.number1
		elif c == '/':
			try :
				inp.ans = inp.number2 / inp.number1
			except ZeroDivisionError :
				print("ERROR : DIVISION BY ZERO")

#Class which handles all numeric buttons
class numpadclass:
	def __init__(self,root,num):
		self.b = tk.Button(root,text = num,command = self.clickevent,padx = 10 ,pady = 10)
		self.b.value = num

	#method which arranges them in a grid
	def arrangeingrid(self,x,y):
		self.b.grid(row = x ,column = y)

	#Event Handler
	def clickevent(self):
		inp.generate(self.b.value)

#Class which handles all operational buttons
class operatorclass:
	def __init__(self,root,op):
		self.b = tk.Button(root,text = op,command = self.clickevent,padx = 11 ,pady = 11)
		self.b.value = op
	
	#method which arranges them in a grid
	def arrangeingrid(self,x,y):
		self.b.grid(row = x ,column = y)

	#Event Handler
	def clickevent(self):
		inp.assignoperator(self.b.value)

#Main Class which initializes all buttons and opens the root tkinter window
class Mainclass:

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Calculator")
		num = 0
		for i in range(3):
			for j in range(3):
				b = numpadclass(self.root,num+1)
				b.arrangeingrid(i+1,j)
				num = num + 1
		
		b = numpadclass(self.root,0)
		b.arrangeingrid(3,3)

		global inp
		inp = inputstring(self.root)

		clearbutton = tk.Button(self.root,text = "C",command = inp.clearcommand,padx = 10 ,pady = 10)
		clearbutton.grid(row = 1,column = 3)
		
		backspace = tk.Button(self.root,text = "<-",padx = 9 ,pady = 10)
		backspace.grid(row = 2,column = 3)

		operators = ['+','-','*','/','=']
		ctr = 0
		for i in operators :
			b = operatorclass(self.root,i)
			b.arrangeingrid(4,ctr)
			ctr = ctr + 1

		self.root.mainloop()

#Object
calc = Mainclass()
