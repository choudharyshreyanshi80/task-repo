import numpy as np 

arr=np.array([2,6,8,4,11,5])
arr_2d=arr.reshape(3,2)
print(arr_2d)

print("Shape:", arr_2d.shape)
print("Dimension:", arr_2d.ndim)
print("Data Type:", arr_2d.dtype)
print("Item Size:", arr_2d.itemsize)

arr1 = np.full((3, 3), 9)
print(arr1)

arr2 = np.linspace(25, 125, 10)
print(arr2)

lst=[2,3,4,5,6]
arr3=np.array(lst)
print(arr3)

print(arr3[::-1])

arr4=np.arange(48).reshape(4,4,3)
print(arr4)
print(arr4[1,0,2])

arr5 = np.arange(1, 17).reshape(4, 4)
print(arr5)
result = arr5[1::2, ::2]
print(result)

result1 = arr4[1, :2, :2]
print(result1)

arr5 = np.array([[23, 56, 78, 93],
                [71, 82, 13, 24]])
for i in range(arr5.shape[0]):
    for j in range(arr5.shape[1]):
        if arr5[i, j] % 2 != 0:
            arr5[i, j] = -1
print(arr5)

arr6 = np.array([1, 0, 2, 0, 3, 0, 4])
indices = np.nonzero(arr6)
print(indices)

a1 = np.array([10, 20, 30])
a2 = np.array([5, 15, 25])
print(a1 + a2)
print(a1*a2)

b1 = [15,20,25] 
b2 = [10,40,37]
res= np.dot(b1,b2)
print("Dot Product:", res)