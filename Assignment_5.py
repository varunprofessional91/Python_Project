import numpy as np
import csv as cs
import pandas as pd

# Q(1): given SalaryGender CSV file and store the data from each column in a separate NumPy array
print("\n\nQ(1):\n")

abc = []
with open('phd.csv', 'rt')as f:
    data = cs.reader(f)
    for row in data:
        str1 = str(row)
        abc.append(str1)

for i in abc:
    ab = i.split(',')
    abd0 = np.array(ab[0])
    abd1 = np.array(ab[1])
    abd2 = np.array(ab[2])
    abd3 = np.array(ab[3])
    abd4 = np.array(ab[4])
    print(abd0, abd1, abd2, abd3)

# Q(2): Find: 1.The number of men with a PhD 2. The number of women with a PhD
print("\n\nQ(2):\n")
print("\n-------Male List with phd Graduation------")
with open('phd.csv', 'rt')as f:
    data = cs.reader(f)
    for row in data:
        str1 = str(row)
        if row[1] == "phd" and row[3] == "male":
            print(str1)

print("\n-------Female List with phd Graduation--------")
with open('phd.csv', 'rt')as f:
    data1 = cs.reader(f)
    for row1 in data1:
        str2 = str(row1)
        if row1[1] == "phd" and row1[3] == "female":
            print(row1)

# Q(3): Storing “Age” and “PhD” columns in one DataFrame and delete the data of all people who done.
print("\n\nQ(3):\n")

emp_box = []
with open('phd.csv', 'rt')as f:
    data2 = cs.reader(f)
    for row in data2:
        str1 = str(row)
        if row[1] == "phd":
            emp_box.append((row[1], row[2]))
print(pd.DataFrame(emp_box))

# Q(4): Calculate the total number of people who have a PhD degree from SalaryGender CSV file.
print("\n\nQ(4):\n")

emp_box_12 = 0
with open('phd.csv', 'rt')as f:
    data33 = cs.reader(f)
    for row in data33:
        str1 = str(row)
        if row[1] == "phd":
            emp_box_12 += 1
print("Total Number of Phd Degrees Holder : ", emp_box_12)

# Q(5): How do you Count The Number Of Times Each Value Appears In An Array Of Integers?
print("\n\nQ(5):\n")


def count_num_of_times(a_lst, a_len):
    c_list = []
    for vc in range(a_len):
        r_lst = 0
        for ac in range(a_len):
            if vc == a_lst[ac]:
                r_lst += 1
        c_list.append(r_lst)
    return c_list


arr_list = [1, 2, 5, 2, 4, 3, 4, 7, 8, 8]
arr_len = len(arr_list)
print("Given List For Count Integers : ", arr_list)
print("Integer Value No. of Times", count_num_of_times(arr_list, arr_len))

# Q(6): Create a numpy array and filter the elements greater than 5.
print("\n\nQ(6):\n")

npy_arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
npy_lst = []
for na in range(len(npy_arr)):
    for na1 in range(len(npy_arr[na])):
        if npy_arr[na][na1] > 5:
            npy_lst.append(npy_arr[na][na1])
print("Greater than 5 in Numpy Array Values Are : ", npy_lst)

# Q(7): Create a numpy array having NaN (Not a Number) and print it.
print("\n\nQ(7):\n")

npy_arr_nan = ([np.nan, 1., 2., np.nan, 3., 4., 5.])
add_arr = []
add_arr1 = []
for nan_value in range(len(npy_arr_nan)):
    add_arr.append(npy_arr_nan[nan_value])
for nan_value1 in range(len(npy_arr_nan)):
    add_arr1.append(nan_value1)
print(add_arr)
print(add_arr1)

# Q(8): Create a 10x10 array with random values and find the minimum and maximum values.
print("\n\nQ(8):\n")

npy_mat = np.random.randint(10, size=(10, 10))

for min_val in range(10):
    min_value = np.amin(npy_mat[min_val])
    max_value = np.amax(npy_mat[min_val])
    print("Array Index %d : Min Value || %d Max Value || %d" % (min_val, min_value, max_value))

# Q(9): Create a random vector of size 30 and find the mean value.
print("\n\nQ(9):\n")

ran_vec = np.random.random(30)
ran_len = len(ran_vec)
ran_sum = np.sum(ran_vec)
mean_value = ran_sum / ran_len
print("Mean Value of Random Vector Size of 30 : %d " % mean_value)

# Q(10): Create numpy array having elements 0 to 10 And negate all the elements between
print("\n\nQ(10):\n")

npy_mat_1 = np.random.randint(10, size=(1, 10))
npy_ar = np.negative(npy_mat_1)
x = np.array([-1, -4, 0, 2, 3, 4, 5, -6])
print("Original array:")
print(x)
print("Replace the negative values of the said array with 0:")
x[x < 0] = 0
print(x)
print(npy_mat_1)

# Q(11): Create a random array of 3 rows and 3 columns and sort it according to 1st column 2nd column or 3rd column.
print("\n\nQ(11):\n")

npy_mat1 = np.random.randint(10, size=(3, 3))
npy_sort = np.sort(npy_mat1)
print("Original Numpy Array : \n ", npy_mat1)
print("Sorted Numpy Array : \n ", npy_sort)

# Q(12): Create a four dimensions array get sum over the last two axis at once.
print("\n\nQ(12):\n")

npy_mat1 = np.random.randint(10, size=(4, 4, 4))
# arr_sum = npy_mat1.sum(axis=(2, 2))
print(npy_mat1)
# print(arr_sum)

# Q(13): Create a random array and swap two rows of an array.
print("\n\nQ(13):\n")

npy_mat2 = np.random.randint(10, size=(4, 4))
arr_sum11 = np.swapaxes(npy_mat2, 0, 1)
print("Original Array : \n", npy_mat2)
print("\nSwapped Array : \n", arr_sum11)

# Q(14): Create a random matrix and Compute a matrix rank.
print("\n\nQ(14):\n")

npy_mat3 = np.random.randint(10, size=(4, 4))
npy_mat4 = np.matrix.view(npy_mat3)
print("", npy_mat3, "\n")
print(npy_mat4)
###
