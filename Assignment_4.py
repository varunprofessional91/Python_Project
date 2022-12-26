import math as m1
import time as t1


# Q(1): A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT


# Q(2): program for searching specific data from that list.


def selection_sort(a_list):
    for i in range(len(a_list)):
        least = i
        for k in range(i + 1, len(a_list)):
            if a_list[k] < a_list[least]:
                least = k
        swap(a_list, least, i)


def swap(a, x, y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp


my_list = [5.76, 4.7, 25.3, 4.6, 32.4, 55.3, 52.3, 7.6, 7.3, 86.7, 43.5]
print("\n\nQ(2):\nGiven List : ", my_list)
selection_sort(my_list)
print("Sorted List : ", my_list)


# Q(3): program for such organization to find whether is it dark outside or not.


def weather_update(localtime):
    if 6 < localtime < 20:
        print("It's Day OutSide")
        return
    else:
        print("It's Dark Outside")
        return


local_time = t1.localtime().tm_hour
print("\n\nQ(3): \nCurrent Time : %d:%d" % (t1.localtime().tm_hour, t1.localtime().tm_min))
weather_update(local_time)


# Q(4): program to find distance between two locations when their latitude and longitudes are given.


def distance_calculator(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    cal = 0.5 - m1.cos((lat2 - lat1) * p) / 2 + m1.cos(lat1 * p) * m1.cos(lat2 * p) * (
            1 - m1.cos((lon2 - lon1) * p)) / 2
    earth_radius = 6371
    radius = earth_radius * 2
    distance = round(radius * m1.asin(m1.sqrt(cal)), 2)
    return distance


lat_1 = 13.6
lon_1 = 15.6
lat_2 = 14.5
lon_2 = 17.3
print("\n\nQ(4):\nGiven Values For Distance\nLatitude 1 : %d\nLongitude 1 : %d\nLatitude 2 : %d\nLongitude 2 : %d" % (
    lat_1, lon_1, lat_2, lon_2))
print("\nDistance Between Locations : %d km" % distance_calculator(lat_1, lon_1, lat_2, lon_2))

# Q(5): Bank system. with Options: cash withdraw, cash deposit, change password. with user Input

print("\n\nQ(5):\n")

account_name = ""
deposit_amount = 0
created_password = ""


def banking():
    print("------------Apna Bank------------")
    print("Enter 0 For Create Account")
    print("Enter 1 For Cash Withdrawal")
    print("Enter 2 For Cash Deposit")
    print("Enter 3 For Change Password")
    print("Enter 4 For Account Information")
    print("Enter 5-9 For Banking Logout")
    print("---------------------------------")
    inp = int(input("\nEnter Your Option -: "))
    print("\n")
    if inp == 0:
        create_account()
        return
    elif inp == 1:
        cash_withdraw()
        return
    elif inp == 2:
        cash_credit()
        return
    elif inp == 3:
        change_password()
        return
    elif inp == 4:
        account_information()
        return
    else:
        print("Logout From Banking")
        return


def create_account():
    print("---------Create Account---------")
    acc_name = input("Enter Your Name : ")
    dep_amt = int(input("Enter Deposit Amount : "))
    pass_word = input("Enter Your Password : ")
    global account_name, deposit_amount, created_password
    account_name = acc_name
    deposit_amount = dep_amt
    created_password = pass_word
    print("\nAccount Created Successfully\n")
    print("---------------------------------")
    return banking()


def cash_withdraw():
    print("---------Cash Withdrawal---------")
    with_amt = int(input("Enter Withdrawal Amount : "))
    global deposit_amount
    if with_amt < deposit_amount:
        deposit_amount = deposit_amount - with_amt
        print("\nCash Withdrawal Successfully\n")
        print("Current Balance is : %d\n" % deposit_amount)
    else:
        print("\nInsufficient Account Balance\n")
    print("---------------------------------")
    return banking()


def cash_credit():
    print("---------Cash Deposit---------")
    dep_amt = int(input("Enter Deposit Amount : "))
    global deposit_amount
    deposit_amount = deposit_amount + dep_amt
    print("\nCash Deposit Successfully\n")
    print("Current Balance is : %d\n" % deposit_amount)
    print("-------------------------------")
    return banking()


def change_password():
    print("---------Change Password---------")
    global created_password
    chge_pass = input("Enter Old Password : ")
    if created_password == chge_pass:
        new_pass = input("Enter New Password : ")
        created_password = new_pass
        print("\nPassword Changed Successfully\n")
    else:
        print("\nWrong Password Try Again\n")
    print("----------------------------------")
    return banking()


def account_information():
    print("---------Account Information---------")
    global created_password, deposit_amount, account_name
    print("\nAccount Name : %s\nAccount Balance : %d\nAccount Password: %s\n" % (
        account_name, deposit_amount, created_password))
    print("-------------------------------------")
    return banking()


banking()

# Q(6): Divisible by 7 but are not a multiple of 5, between 2000 and 3200 in a comma-separated on a single line.
print("\n\nQ(6):\n")
inline = []
for x in range(2000, 3201):
    if (x % 7) == 0:
        y = x / 5.0
        if (y % 5) != 0:
            inline.append(str(x))
print(",".join(inline))

# Q(7): compute the factorial of a given numbers. Use recursion to find it.
print("\n\nQ(7):\n")


def recursion_factorial(number):
    if number == 1:
        return number
    else:
        return number * recursion_factorial(number - 1)


number_input = int(input("Enter a Number For Factorial : "))
print("The Factorial of %d is : %d" % (number_input, recursion_factorial(number_input)))

# Q(8): calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]

print("\n\nQ(8):\n")


def square_root(i1, i2, i3):
    c = 50
    h = 30
    arg = [i1, i2, i3]
    out = []
    for x1 in range(3):
        formula = (2 * c * arg[x1]) / h
        sqr_root = m1.sqrt(formula)
        output = int(sqr_root)
        out.append(output)
    print("Given Values for Square Roots : %d,%d,%d" % (arg[0], arg[1], arg[2]))
    print("Square Roots  of Given Values : %d,%d,%d" % (out[0], out[1], out[2]))
    return


na = []

number_input = input("Enter 3 Numbers with Comma For Square Root : ")
spl_val = number_input.split(",")
for xv in spl_val:
    gv = int(xv)
    na.append(gv)

square_root(na[0], na[1], na[2])

# Q(9): calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
print("\n\nQ(9):\n")


def array_dimensional(r, c):
    array_1 = [[i * j for j in range(c)] for i in range(r)]
    return array_1


row = int(input("Enter Rows Numbers : "))
col = int(input("Enter Column Numbers : "))

print(array_dimensional(row, col))

# Q(10): comma separated sequence of words, comma-separated sequence after sorting them alphabetically
print("\n\nQ(10):\n")
words_list = input("Enter Words, Comma Separated : ")
words_list = words_list.split(",")
words_list = sorted(words_list)
print(",".join(words_list))

# Q(11): sequence of lines as input and prints the lines after all characters in the sentence capitalized.
print("\n\nQ(11):\n")
input_lines = []
print("Enter Words Sequence : ")

while True:
    words_input = input("-: ")
    if not words_input:
        break
    input_lines.append(words_input.upper())
for x in input_lines:
    print(x)

# Q(12): Remove all duplicate words and sort them alphanumerically.
print("\n\nQ(12):\n")
words_seq = input("Words Separated By WhiteSpace : ")
seq_split = words_seq.split(' ')
words_set = set(seq_split)
seq_wd = ' '.join(sorted(words_set))
print("Removed Duplicate Words,Sorted : ", seq_wd)
print("Given Paragraph : ", words_seq)

# Q(13): sequence of comma separated 4 digit binary no. and check they are divisible by 5 or not
print("\n\nQ(13):\n")


def binary_conversion(binary_val):
    out_binary = []
    bin_val = binary_val.split(",")
    num_val = [x1 for x1 in bin_val]
    for p in num_val:
        x1 = int(p, 2)
        if not x1 % 5:
            out_binary.append(p)
    out_put = ','.join(out_binary)
    return out_put


inp_val = input("Enter 4 Digit Binary Values Comma Separated : ")
print("Divisible By 5 or Not, Printing in Binary Number : ", binary_conversion(inp_val))

# Q(14): program that accepts a sentence and calculate the number of upper case letters and lower case letters
print("\n\nQ(14):\n")


def string_test(string_val):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for val in string_val:
        if val.isupper():
            d["UPPER_CASE"] += 1
        elif val.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print("Given String : ", string_val)
    print("Uppercase Alphabets : ", d["UPPER_CASE"])
    print("Lowercase Alphabets : ", d["LOWER_CASE"])


string_test(input("String Lower & Upper Case Count : "))

# Q(15): Examples of Fsum and Sum
print("\n\nQ(15):\n")

set_list = {1, 2, 3, 1.2}  # set
dict_list = {1: 1.2, 2: 2.1, 3: .1}  # dictionary
tuple_list = (1, 2, 3.0)  # tuple
list_list = [1, 0.2, 3]  # list
frozenset_list = frozenset([2, 1.3, 4])  # frozenset

print("------------Fsum Examples For Python Data types-------------")
print(" Fsum of Sets...... || ", m1.fsum(set_list), " || Data Type ||", type(set_list))
print(" Fsum of Dictionary || ", m1.fsum(dict_list.values()), " || Data Type ||", type(dict_list))
print(" Fsum of Tuples.... || ", m1.fsum(tuple_list), " || Data Type ||", type(tuple_list))
print(" Fsum of List...... || ", m1.fsum(list_list), " || Data Type ||", type(list_list))
print(" Fsum of FrozenSets || ", m1.fsum(frozenset_list), " || Data Type ||", type(frozenset_list))
print("------------------------------------------------------------")
print("------------Sum Examples For Python Data types-------------")
print(" Sum of Sets...... || ", sum(set_list), " || Data Type ||", type(set_list))
print(" Sum of Dictionary || ", sum(dict_list.values()), " || Data Type ||", type(dict_list))
print(" Sum of Tuples.... || ", sum(tuple_list), " || Data Type ||", type(tuple_list))
print(" Sum of List...... || ", sum(list_list), " || Data Type ||", type(list_list))
print(" Sum of FrozenSets || ", sum(frozenset_list), " || Data Type ||", type(frozenset_list))
print("-----------------------------------------------------------")
