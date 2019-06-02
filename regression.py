
import math
n = int(input("Type the number of values: "))
x = []
y = []
y_square = []
x_square = []
xy = []
for i in range(n):
	x_values = int(input("x["+str(i)+"]: "))
	x.append(x_values)
for i in range(n):
	y_values = int(input("y["+str(i)+"]: "))
	y.append(y_values)
for i in range(n):
	x_square.append(x[i]**2)
	y_square.append(y[i]**2)
	xy.append(x[i]*y[i])
print(sum(x))	
#Determine r
print("Sum x: "+str(sum(x)) + " \nSum y: "+ str(sum(y)) + " \nSum y square: "+ str(sum(y_square)) + "\nSum x square: "+str(sum(x_square))+"\nSum xy: " + str(sum(xy)))
r = (n*(sum(xy)) - sum(x)*sum(y))/(math.sqrt((n*sum(x_square) - sum(x)**2)*((n*sum(y_square) - sum(y)**2))))
print("\n r: " +str(r))
b = (n*(sum(xy)) - sum(x)*sum(y))/((n*sum(x_square) - sum(x)**2))
print("\nb: " +str(b))
a = sum(y)/n - b*sum(x)/n
print("\na: " +str(a))
