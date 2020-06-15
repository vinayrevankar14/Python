#1.Write a NumPy program to get the numpy version and show numpy build configuration.
import numpy as np
print('Version of numpy:',np.__version__)
print('Build configuration of numpy:',np.show_config())

#2.Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.
import numpy as np
a = np.array([1+2j,2+0j,9+3j])
print('Original Array:',a)
print('Complex number in an array:')
print(np.iscomplex(a))
print('Real number in an array:')
print(np.isreal(a))
print('Is number scalar or not:',np.isscalar(1))

#3.Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
a = np.array(list(map(int,input().split())))
print('Original array:',a)
print('Is none of the element in a given array is zero:',np.all(a))

#4.Write a NumPy program to test whether any of the elements of a given array is non-zero.
import numpy as np
a = list(map(int,input().split()))
arr = np.array(a)
print('Given array:',arr)
print('Elements of given array is non-zero:',np.any(arr))

#5.Write a NumPy program to test element-wise for NaN of a given array.
import numpy as np
a = np.array([1,0,2, np.nan])
print('Original array:',a)
print('Test element-wise for NaN of a given array:',np.isnan(a))

#6.Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np
a = np.array([[2,4], [8,9]])
b = np.array([[7,5], [5,5]])
print('Array 1:',a)
print('Array 2:',b)
print('Greater:',np.greater(a,b))
print('Greater-equal:',np.greater_equal(a,b))
print('Less:',np.less(a,b))
print('Less-equal:',np.less_equal(a,b))

#7.Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
import numpy as np
x = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y = np.array ([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])
print('Is equal:',np.equal(x,y))
print('Equal with tolerance:',np.allclose(x,y))

#8.Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
import numpy as np
a = np.array([1, 7, 13, 105])
print('Array:',a)
print('It\'s size of memory taken:')
print('%d bytes'%(a.size * a.itemsize))

#9.Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.
import numpy as np
print('Array of 10 zeros:',np.zeros(10))
print('Array of 10 ones:',np.ones(10))
print('Array of 10 fives:',(np.ones(10)*5))

#10.Write a NumPy program to create an array of the integers from 30 to 70.
import numpy as np
a = np.arange(30,71)
print('Array of integers from 30 to 70:')
print(a)

#11.Write a NumPy program to create an array of all the even integers from 30 to 70.
import numpy as np
a = np.arange(30,71,2)
print('Array of all even integers from 30 to 70:')
print(a)

#12.Write a NumPy program to create a 3x3 identity matrix.
import numpy as np
print('3x3 identity matrix:',np.identity(3))

#13.Write a NumPy program to generate a random number between 0 and 1.
import numpy as np
a = np.random.normal(0,1,1)
print('Random number between 0 and 1:',a)

#14.Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
import numpy as np
a = np.random.standard_normal(15)
print('Array of 15 random numbers from a standard normal distribution:',a)

#15.Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
import numpy as np
a = np.arange(15,55)
print('Array:',a)
print('values except first and last:')
print(a[1:-1])