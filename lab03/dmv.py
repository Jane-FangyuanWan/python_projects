import random

fullname = input("Input your full name:\n")

date_of_birth = input("Enter date of birth (MM/DD/YY):\n")
expiration_date = date_of_birth[:5]

#name_break is a variable that stores the position (index) of the last space character (' ') in the fullname string. 
#It's found using the rfind method, which searches for the last occurrence of a specified substring or character within a string.
name_break = fullname.rfind(' ')

#a slice operation on the 'fullname" sting. It extracts a portion of the string starting from the beginning(index 0)
#up to, but not including, the position indicated by 'name_break'
first_and_middle = fullname[:name_break]
last_name = fullname[name_break+1:]

diver_license_number = random.randint(0000000, 9999999)

print("-------------------------------------")
print("Washington Driver License")
print("DL: ",diver_license_number)
print("LN: ", last_name)
print("FN: ", first_and_middle)
print("DOB: ", date_of_birth)
print("EXP: ", expiration_date + "/21")
print("-------------------------------------")


