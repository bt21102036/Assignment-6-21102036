# Q1 Python program to check perfect number using function
print("Aliquot Sum Method ")

def perfect_numbers(N):  #Aliquot Sum
   sum=0
   for i in range(1,N):
      if(N%i == 0):
         sum = sum+i
   return sum

# take inputs
N = int(input("Enter a number: "))

# check perfect number or not
if(N == perfect_numbers(N)):
   print(N, "is a perfect number")
else:
   print(N, "is not a perfect number")
print("")

print("The other method of including digit")
def perfect_number(N):
    Sum=0
    for i in range(1, N + 1):  # number equals half of the sum of all positive divisors including the number itself
        if (N % i == 0):
            Sum = Sum + i
    return Sum/2

N=int(input("Enter the number:"))
if (N==perfect_number(N)):
        print(N,"The number is a perfect number")
else:
        print(N,"The number is not a perfect number")

print("")


#Q2 Palindrome String
def isPalindrome(s):  #user-defined function
    return s == s[::-1]

# take inputs
string = input('Enter the string: ')

# calling function and display result
reverse = isPalindrome(string)
if reverse:
    print(string,'is a Palindrome')
else:
    print(string,'is not a Palindrome')

print("")


#Q3 Pascal's Triangle
def factorial(a):          #defining factorial
    i = 1
    for m in range(1, a + 1):
        i = i * m

    return i

n=int(input("Enter the number of rows:"))

for p in range(0,n):                              #number of rows
    for q in range(1,n-1):                        #number of columns
        print("")

    for r in range(0,p+1):                          #combinations formula
        coefficient=int(factorial(p)/(factorial(r)*factorial(p-r)))
        print("",coefficient,end="")

print("")


#Q4 Pangram

import string


def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in s.lower():
            return False

    return True


# Driver code
string =input("Enter the string:")
if (is_pangram(string) == True):
    print("Yes,the given string is a pangram")
else:
    print("No,the given string is not a pangram")

print("")


#Q5 Given the hyphen-separated string as user input using the input() function.
s = input("Enter the string = ")
# print the string before alteration
print('The string before alteration = ',s)
# Split the hyphen-separated strings into a list of strings using the split()
# function and store it in a variable.
w = s.split("-")
# sort the given list using the sort() function.
w.sort()
# Print the sorted sequence by joining the words in the list with a hyphen.
result = '-'.join(w)
# print the resultwords
print('The string after alteration = ', result)
print("")

#Q6 Student Data
def student_data(student_id,**kwargs):
    print("Student ID=",student_id)
    if "student_name" in kwargs:
        print("Student Name=",kwargs["student_name"])
    if "student_name" and "student_class" in kwargs:
        print("Student Name=",kwargs["student_name"],"and","Student Class=",kwargs["student_class"])

student_data(student_id="21102036")
student_data(student_id="21102036",student_name="Anshula Sharma")
student_data(student_id="21102036",student_name="Anshula Sharma",student_class="1 year")
print("")

#Q7Classes,Instances and Subclasses
class STUDENT:                             #creating class
    pass

class MARKS:
    pass

student=STUDENT()                         #creating object
marks=MARKS()

print("To check whether the object created are instances of the said classes or not:")

print(isinstance(student,STUDENT))
print(isinstance(marks,STUDENT))
print(isinstance(student,MARKS))
print(isinstance(marks,MARKS))

print("")

print(" To check whether the said classes are subclasses of the built-in object class or not:")
print(issubclass(STUDENT, object))
print(issubclass(MARKS, object))

print("")


#Q8 Printing the elements whose sum is zero
# Print all triplets within an array whose sum is zero
# arr[] with 0 sum
def findTriplets(arr, n):
    found = False
    for i in range(0, n - 2):

        for j in range(i + 1, n - 1):

            for k in range(j + 1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True

    # If no triplet with 0 sum
    # found in array
    if (found == False):
        print(" not exist ")


# Driver code
arr = [-25,-10,-7,-3,2,4,8,10]
n = len(arr)
findTriplets(arr, n)

print("")


#Q9 Parentheses
class parentheses:
        def find(str):
           a=['()','{}','[]']
           while any(i in str for i in a):
                for j in a:
                        str=str.replace(j,'')
           return not str

s=input("Enter the parentheses:")
if parentheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")









