
my_list = [1,2,3,4]
import Numpy as np
arr = np.array(my_list)
print(arr)

#print array using numpy
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
arr = np.array(my_mat)
print(my_mat)

#print array in range 0 to 10 and difference b/w 2
print(np.arange(0,10,2))

#print number of zeros 3 times in array
a = np.zeros(3)
print(a)

#print number of zeros in 2*3 matrix
print(np.zeros((2,3)))

#print number of ones in 3*4 matrix
print(np.ones((3,4)))

#number between starting and ending 
print(np.linspace(1,10,5))

#print identity matrix using numpy
print(np.eye(4))

#print random number of array using numpy b/w  0 to 1 in one dimension
print(np.random.rand(5))

#print random number in two dimension
print(np.random.rand(5,3))

# print random number in integer . 1 is start and 10 is end and 5 is number of digit 
a =np.random.randint(1,10,5)
print(a)

# reshape of array
print(a.reshape(5,1))

# finding max and min
print(a.max())
print(a.min())

# find the index of max and min value
print(a.argmax())
print(a.argmin())

 #indexing in array
arr_2d = np.array([[5,2,6],[10,2,9],[5,3,9]])
print(arr_2d)