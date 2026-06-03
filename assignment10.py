import numpy as np
# 2D array

array1=np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
print(array1)
array1=np.nan_to_num(array1,nan=0)
print(array1)
array1_trans=array1.T
print(array1_trans)

# 3D array

array1=np.arange(24).reshape(2,3,4)
print(array1.shape)

arr=np.moveaxis(array1,0,2)
print(arr.shape)
print(arr)

# replacing

arrr=np.array([[1,2,np.nan],[4,np.nan,6],[7,8,9]])
col_mean=np.nanmean(arrr,axis=0)
indices=np.where(np.isnan(arrr))
arrr[indices]=np.take(col_mean,indices[1])
print(arrr)

#replacing

arr1 = np.array([10, -5, 20, -8, 15])
arr1[arr1 < 0] = 0
print(arr1)
