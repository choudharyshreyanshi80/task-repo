import numpy as np

#1)
arr1=np.array([[6,-8,73,-110],
               [np.nan,-8,0,94]
])
arr1=np.nan_to_num(arr1,nan=0)
print("After replacing NaN with 0:")
print(arr1)
trans=np.transpose(arr1)
print("\nAfter interchanging rows and columns:")
print(trans)

#2)
arr2 = np.arange(24).reshape(2, 3, 4)
print("Original Shape:", arr2.shape)
new = np.moveaxis(arr2, 0, 2)
print("New Shape:", new.shape)
print(new)

#3)
arr = np.array([
    [10, np.nan, 30],
    [20, 40, np.nan],
    [30, 50, 60]
])
col_mean = np.nanmean(arr, axis=0)
indices = np.where(np.isnan(arr))
arr[indices] = np.take(col_mean, indices[1])
print("Array after replacing NaN with column average:")
print(arr)

#4)
arr4 = np.array([
    [6, -8, 73, -110],
    [0, -8, 0, 94]
])
arr4[arr4 < 0] = 0
print(arr4)

#5)
a1 = np.array([[3, 4],
                 [5, 6]])
a2 = np.array([[1, 0],
                 [7, 8]])
avg = (a1 + a2) / 2
print("Average of Arrays:")
print(avg)
combined = np.concatenate((a1.flatten(), a2.flatten()))
print("Mean:", np.mean(combined))
print("Median:", np.median(combined))
values, counts = np.unique(combined, return_counts=True)
mode = values[np.argmax(counts)]
print("Mode:", mode)

#6)
A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])
B = np.array([9, -6, 17])
sol = np.linalg.solve(A, B)
print(sol)

A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])
B = np.array([
    [9],
    [-6],
    [17]
])
A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)
print("Solution:")
print(X)

#7)Sem result

import matplotlib.pyplot as plt

# Semester 3 Marks
sem3 = [89, 87, 82, 87, 95, 82, 84, 87, 84, 90]
# Semester 4 Marks
sem4 = [88, 86, 91, 89, 86, 93, 80, 93, 93, 80]

subjects = [
    "Sub1", "Sub2", "Sub3", "Sub4", "Sub5",
    "Sub6", "Sub7", "Sub8", "Sub9", "Sub10"
]

plt.figure(figsize=(12, 6))
plt.plot(subjects, sem3,
         marker='o',
         linestyle='-',
         label='Semester 3')

plt.plot(subjects, sem4,
         marker='s',
         linestyle='-',
         label='Semester 4')

plt.title("Semester 3 vs Semester 4 Result Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(70, 100)
plt.grid(True)
plt.legend()

# Average Marks
sem3_avg = sum(sem3) / len(sem3)
sem4_avg = sum(sem4) / len(sem4)
print("Semester 3 Average:", round(sem3_avg, 2))
print("Semester 4 Average:", round(sem4_avg, 2))
plt.show()