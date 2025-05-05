#***********Task Set 1: String Basics*******
#1. Concatenate Two Strings

string1=input("enter first string: ")
string2=input("enter second string: ")
string3=string1+" "+string2
print("your final string is: ", string3)
print("-------------")
#2. Find Length of a String
print("length of the string is: ",len(string3))

print("-------------")
#3. Extract Substring
space_index=string3.find(' ')
sub_string=string3[space_index+1:]
print("Sub String is: ",sub_string)

print("-------------")
#4. Convert to Upper and Lower Case
print("In UpperCase: ",string3.upper())
print("In LowerCase: ",string3.lower())

print("-------------")
#5. Check if a String is a Number
string4=input("enter a string: ")
string=string4.isnumeric()
print(string)

print("-------------")
#********Task Set 2: Numeric Types & Operations********
#1. Add, Subtract, Multiply, Divide Two Numbers
num1=int(input("enter the first number to arithmatic operation: "))
num2=int(input("enter the second number: "))
addition = num1+num2
subtraction = num1-num2
multiplication = num1*num2
division = num1/num2
print("addition:",addition, ",subtraction:", subtraction, ",multiplication:", multiplication, ",division:", division)

print("-------------")
#2. Check if a Number is Even or Odd
if num1 % 2 == 0:
    print(num1, "is even number")
else:
    print(num1, "is odd number")
print("-------------")
#3. Calculate the Area of a Circle
pi=3.14
radius=float(input("Enter radius of circle: "))
area=pi*radius**2
print("Area of circle:", area)

print("-------------")

#4. Round a Float to 2 Decimal Places
num3 = float(input("Enter a number to float the decimal: "))
rounded_value = round(num3, 2)
print("Rounded value:", rounded_value)

print("-------------")

#Use int(), float(), str() to Convert Types
num4=int("123")
num5=str(45)
num6=float("3.14")

print("int",num4,",string", num5,",float", num6)
print("-------------")

#*************Task Set 3: Type Casting Practice***************
#1. Add a Number and a String Containing a Number
# Convert the string to an integer and add it to num
result = num4 + int(num5)
print("The result of adding is:", result)

print("-------------")
#2. Input Two Numbers as Strings, Multiply Them as Integers
num7=str(input("enter a number for multiply: "))
num8=str(input("enter a number for multiply: "))

product=int(num7)*int(num8)
print(product)
print("-------------")

#3. Convert a Float to an Int and Observe the Change
num9=float(input("enter a number to convert from float to int: "))
print(int(num9))

print("-------------")

#4.Cast Boolean to Integer and Back
boolInput1 = True
boolInput2 = False
convertedBool1 = int(boolInput1)
convertedBool2 = int(boolInput2)
print(convertedBool1)  # 1
print(convertedBool2)  # 0
print(bool(convertedBool1))  # True
print(bool(convertedBool2))  # False

