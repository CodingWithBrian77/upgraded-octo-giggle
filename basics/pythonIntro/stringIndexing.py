# indexing = accessing elements of sequence using[] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"
# print(credit_number[0])
# print(credit_number[0:4]) #start is inclusive, end is exclusive
# print(credit_number[5:9])
# print(credit_number[5:]) #prints string from starting position to end
# print(credit_number[-1]) #prints number at location but using negative indexes so -1 means first in reverse
# print(credit_number[::2]) #goes from start to finish, while printing every other or 2nd character
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")
credit_number = credit_number[::-1] #prints string in reverse
print(credit_number)
