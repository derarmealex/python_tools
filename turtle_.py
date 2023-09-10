import turtle

def angles(x):
	turtle.shape('turtle')
	turtle.pencolor('red')
	for i in range(x):
		turtle.forward(100)
		turtle.left(360 / x)
	turtle.done()
	
x = int(input('Enter a number of angles: '))
if x > 2:
	angles(x)
else:
	print('Enter a number bigger than 2!')