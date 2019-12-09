import matplotlib.pyplot as plt
#%matplotlibinline
import numpy as np
#Introduction to numpy craeting an array 
my_list1 = (1,2,3,3,4)
my_list2 = (4,5,6,7,9)
new_array = np.array([my_list1,my_list2])
print('Adding list 1 to list 2 creates an array', new_array)

#Usage of Shape
print(new_array.shape)

#Datatype of the array
print(new_array.dtype)

#General functions of numpy
#zeros, ones, empty, eye, arrange
#zeros

print('Prints out all zeros elts ', + np.zeros(5))

#ones
print('Prints out all ones elts ', + np.ones([5,5]))

#eye
print('Prints out an identity matrix', + np.eye(5))

#Scalar Operations on arrays
#multiplication
print('Multiplication of arrays result' , + new_array*new_array)

#Exponential Multiplication
print('Print array raised to a powwer', + new_array**3)

#Division 
print('Prints out array divided by another ', + new_array / (1/new_array))# reciporcal is 1/by a number

#Indexing Arrays 
print('The python indexing starts from zero', + new_array[0])
#General operations on a numpy array
A = np.arange(1, 15, 2)
print(A)

#Square root of numbers
B = np.sqrt(A)
print('The value of the array is ', + B)

#Exponential value of numbers
C = np.exp(A)
print('The value of C is ', + C)

#Addition 
D = np.add(A,B,C)
print('The value of D is', + D)

#Maximum
E = np.maximum(C,D)
print('The maximum of any two arrays is returned elementwise as an new array', + E)

#Saving and loading arrays 
#Saving single arrays
np.save('saved_array', E)
#new file created is an npy file
new_array = np.load('saved_array.npy')
print(new_array)

#Saving multiple arrays
array1 = np.arange(25,1000,10)
array2 = np.arange(25,1000,10)
np.savez('mlarrays.npz', x =array1, y = array2)
loadnpz = np.load('mlarrays.npz')
print('printing elts in array 1 named x', + loadnpz['x'])
print('printing elts in array 2 named y', + loadnpz['y'])

#Saving to .txt files
np.savetxt('notepad.txt', array1, delimiter=',')
loadtxt = np.loadtxt('notepad.txt', delimiter=',')
print('the text file contains an array of numbers array 1 precisely', + loadtxt)

# Statistical processing of data
axes_values = np.arange(-100,100.10)
dx , dy = np.meshgrid(axes_values,axes_values)

function = 2*dx + 3*dy
print('values for dx', + dx)
plt.imshow(function)
plt.title('plot of 2dx + 3dy')
plt.colorbar()
plt.savefig('newfig.png')

function2 = np.cos(dx) + np.sin(dy)
#print('values for dx', + dx)
plt.imshow(function2)
plt.title('plot of cos and sine')
plt.colorbar()
plt.savefig('newfig2.png')

#Conditional Clauses and Boolean Operations
w= np.array([10,20,50,70])
u= np.array([25,40,30,45])
condition =np.array([True,True,False,False])
z = [a if cond else b for a, cond, b in zip(w, condition,u)]
print(z)
# using np.where function

z2 = np.where(condition,u,w)
print(z2)

z3 = np.where(u >= 30, 0, 1)
print(z3)

# Standard Functions in Numpy 
#Summimg a column
print(w.sum())

b = np.array([[10,14,23,67], [25,67,56,50]])
print('column wise summation', + b.sum(0))

# mean, standard deviation, variance
print('The value of the mean is ', + u.mean())
print('The value of the standard deviation is ', + u.std())
print('The value of the variance is ', + w.var())
print('Column wise calculation', + b.var(0))

# Logical Operators 
condition2 = np.array([True,False,True])
print('This the OR logical operator returns TRUE if any of the items is  TRUE',  condition2.any())
print('This is the AND logical operator returns TRUE if all the items are TRUE', condition2.all())

# Sorting an array 
unsorted_array = np.array([12,10,35,15,5,2,1,12,20,19,23,13,20])
unsorted_array.sort() # .sort() sorts an array of numbers 
print('This function sorts an array ', unsorted_array)

# using the unique function 
arr1= np.array(['solid', 'solid','gas','gas','solid','liquid'])
print('Prints out the unique elts in an array', np.unique(arr1))

#in1d is a function which checks if elts in one array is in another prints out true if yes and otherwise
print('prints out the elts ', np.in1d(['sold','solid','solid','gas','liquid','liqud'],arr1))