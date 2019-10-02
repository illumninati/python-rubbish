def add(x,y):
	x = int(x)
	y = int(y)
	print(x+y)
def subt(x,y):
	x = int(x)
	y = int(y)
	print(x-y)
def mult(x,y):
	x = int(x)
	y = int(y)
	print(x*y)
def div(x,y):
	x = float(x)
	y = float(y)
	print(x/y)

com = input ("Add, subtract, multiply or divide?\n")
if com == "add":
	adx = input ("First number?\n")
	x = adx
	ady = input ("Second number?\n")
	y = ady
	print(add(x,y))
elif com == "subtract":
	sbx = input ("First number?\n")
	x = sbx
	sby = input ("Second number?\n")
	y = sby
	print(subt(x,y))
elif com == "multiply":
	mlx = input ("First number?\n")
	x = mlx
	mly = input ("Second number?\n")
	y = mly
	print(mult(x,y))
elif com == "divide":
	dvx = input ("First number?\n")
	x = dvx
	dvy = input ("Second number?\n")
	y = dvy
	print(div(x,y))
else:
	print("this aint a joke get out")

