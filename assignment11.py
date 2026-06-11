import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([
    [4,5,6],
    [7,8,9]
])

res=np.concatenate(([arr1],arr2),axis=0)
print("Combined Array:")
print(res)

flat=arr2.reshape(-1)
print("Flattened Array:")
print(flat)

rev=arr1[::-1]
print("Reversed Array:")
print(rev)

arr=np.array([10,34,5,12,77])
print("Maximum Value:")
print(np.max(arr))

print("Minimum Value:")
print(np.min(arr))

rows, cols = arr2.shape
print("Rows:", rows)
print("Columns:", cols)

print("All Elements:")
print(arr2)

print("Specific Element:")
print(arr2[1, 2])

t = 0
for row in arr2:
    for value in row:
        t += value
print("Sum :", t)

a = np.array([10, 20, 30])
b = np.array([2, 4, 5])
print("Addition:")
print(a + b)
print("Subtraction:")
print(a - b)
print("Multiplication:")
print(a * b)
print("Division:")
print(a / b)

arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("Using Nested For Loop:")
for i in arr3:
    for j in i:
        for k in j:
            print(k)

print("Using nditer:")
for x in np.nditer(arr3):
    print(x)


arr5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
arr6 = np.array([
    [6, 5, 4],
    [3, 2, 1]
])
combined = np.concatenate((arr5, arr6))
print("Combined Array:")
print(combined)

print("Mean =", np.mean(combined))
print("Median =", np.median(combined))
average = (arr5 + arr6) / 2
print("Average:")
print(average)




