import numpy as np 
my_list1 = (1,2,3,3,4)
my_list2 = (4,5,6,7,9)
new_array = np.array([my_list1,my_list2])
print('Adding list 1 to list 2 creates an array', new_array)

#Indexing arrays
print('Python starts indexing from zero', new_array[0])
n_array = np.arange(0,12)
print(n_array)
#Indexing arrays
print('Python starts indexing from zero', n_array[1])
a_arr = n_array[0:6]
print(a_arr)
a_arr [:] = 15
print(a_arr)
#Copying arrays 
b_arr = a_arr.copy()
print(b_arr)

#Working on multidimensional arrays
c_array = np.append(new_array,b_arr).reshape(4,4)
print(c_array)
# Accessing elts in an array
print(c_array[0][1])
print(c_array[:2][:])
print(c_array[:2,:1])