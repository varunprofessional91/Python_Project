# (1): Factor Number

fac_num = 122
# fac_num = int(input("Enter a Number : \n\n"))

for f_num in range(1, fac_num + 1):
    if fac_num % f_num == 0:
        print(f_num)

# (2): Words in a sequence

words_seq = "Hinton Brother How Are You Fine Thank You"

seq = words_seq.split()

seq.sort()

print("\n\nWords Sequence :")
for s in seq:
    print(s)

# (3): even numbers between 1000 and 3000

print("\n")
items = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        items.append(s)
print(",".join(items))

# (4): Digits and Alphabets Counting

# input_data = input("Enter a Phrase : ")

input_data = "My Cell No. 8898993037 and I Live in Bangalore"
l1 = 0
d1 = 0
for c in input_data:
    if c.isdigit():
        d1 = d1 + 1
    elif c.isalpha():
        l1 = l1 + 1
    else:
        pass
print("\n\nLetters Counting : ", l1)
print("Digits  Counting : ", d1)

# (5): Checking Number is Palindrome or Not

# no = int(input("Enter number:"))
no = 64464
no2 = no
nov = 0
while no > 0:
    digit = no % 10
    nov = nov * 10 + digit
    no = no // 10
if no2 == nov:
    print("\n\nThe number is a palindrome!")
else:
    print("\n\nThe number isn't a palindrome!")
