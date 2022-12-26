import re
import random


# (1): Output will be 4
print("(Q1): Output Will Be 4 \n\n")


# (2): Output will be "John","Peter"
print('(Q1): Output will be "John","Peter" \n\n')

# (3): User Password Validation

user_input = input("(Q3): Enter Password For Validation:\n\n")
x = True
while x:
    if len(user_input) < 6 or len(user_input) > 12:
        break
    elif not re.search("[a-z]", user_input):
        break
    elif not re.search("[0-9]", user_input):
        break
    elif not re.search("[A-Z]", user_input):
        break
    elif not re.search("[$#@]", user_input):
        break
    elif re.search("\s", user_input):
        break
    else:
        print("\nValid Password")
        x = False
        break
if x:
    print("\nNot a Valid Password")


# (4): Loop Printing

a = [4, 7, 3, 2, 5, 9]
c = 0
print("\n(Q4): ")
for b in a:
    print("Element Value : ", b, "Element Position Index Value : ", c)
    c = c + 1


# (5): Printing Even Values in a String

print("\n\n")

str_par = "H1e2l3l4o5w6o7r8l9d"

res2 = 0


def values_string(str_arg):
    res1 = ""
    for i in range(len(str_arg)):
        if i % 2 == 0:
            res1 = res1+str_arg[i]
    return res1


print("(Q5):\n Declared String : ", str_par)
print("Printing Even Indexes Values : ", values_string(str_par))


# (6): Printing Even Values in a String
print("\n\n")


def reverse(str1):
    rev = ''.join(reversed(str1))
    return rev


s = "rise to vote sir"

print("(Q6):\n The original string  is : ", s)
print("The reversed string(using loops) is : ", reverse(s))


# (7): count and print the numbers of each character
print("\n\n")


def alphabet_counter(string_arg):
    a = string_arg.count('a')
    b = string_arg.count('b')
    c = string_arg.count('c')
    d = string_arg.count('d')
    e = string_arg.count('e')
    f = string_arg.count('f')
    g = string_arg.count('g')

    print("Counting Alphabets: \na,%s\nb,%s\nc,%s\nd,%s\ne,%s\nf,%s\ng,%s\n" % (a, b, c, d, e, f, g))

    return


string_phrase = "bcdefgabc"
print("(Q7): \nDeclared String : ",string_phrase)
alphabet_counter(string_phrase)


# (8): Intersection of the given List

list_1 = [12, 3, 6, 78, 35, 55]
list_2 = [12, 24, 35, 24, 88, 120, 155]


def intersection_finder(list1, list2):
    list_3 = [value for value in list1 if value in list2]
    return list_3


print("(Q8): \nPrinting List 1 : ", list_1)
print("Printing List 2 : ", list_2)
print("Printing Intersection From Given Lists : ", intersection_finder(list_1, list_2))


# (9): list after removing all duplicate values with original order reserved.
print("\n\n")


def remove_duplicate(li_rem):
    new_list = []
    seen = set()
    for item in li_rem:
        if item not in seen:
            seen.add(item)
            new_list.append(item)

    return new_list


list_rem = [12, 24, 35, 24, 88, 24, 120, 155, 88, 120, 155]
print("(Q9): \nDeclared Numbers List: ", list_rem)
print("Removed Duplicate Values From Given List : ", remove_duplicate(list_rem))


# (10): printing the list after removing the value 24 in given list
print("\n\n")

list_prn = [12, 24, 35, 70, 88, 120, 155]
print("(Q10): \nDeclared Numbers List : ", list_prn)
list_prn = [x for x in list_prn if x != 24]
print("Removed 24 From Given List : ", list_prn)


# (11): printing the list after removing the number 0,4,5 in given list
print("\n\n")
num_list = [12, 24, 35, 70, 88, 120, 155]
print("(Q11): \nDeclared Numbers list : ", num_list)
num_list = [x for (i, x) in enumerate(num_list) if i not in (0, 4, 5)]
print("List Printing Removing 0th, 4th, 5th No. : ", num_list)


# (12): printing the list after removing delete numbers which are divisible by 5 and 7 in given list
print("\n\n")
div_list = [12, 24, 35, 70, 88, 120, 155]
div_list1 = [x for x in div_list if x % 5 != 0 and x % 7 != 0]
print("(Q12): \nDeclared Numbers List : ", div_list)
print("List with Removing Numbers Divisible by 5 and 7 : ", div_list1)


# (13): randomly generating a list with 5 numbers, which are divisible by 5 and 7 , list no between 1 and 1000 inclusive
print("\n\n")

blank_list = []
for x in range(5):
    ran_list = random.randint(1, 1001)
    blank_list.append(ran_list)
divisible_list = [i for i in blank_list if i % 5 == 0 and i % 7 == 0]
print("(Q13): \nRandomly Generated List : %s" % blank_list)
print("Divisible Numbers By 5 and 7 : %s" % divisible_list)


# (14): Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
print("\n\n")
given_no = 5
# given_no = int(input("Enter the Number of Sequence: "))


def sequence_sum(g_no):
    float_value = 0.0
    for seq_no in range(1, g_no + 1):
        float_value = float_value + (seq_no / (seq_no+1))
    return float_value


print("(Q14): \nSum of Sequence 1/2+2/3+3/4+4/5 : \n", sequence_sum(given_no))
