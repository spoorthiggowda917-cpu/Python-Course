print("Hello World")

#>>>Type Conversion
age=20
s="2"
print(age+int(s))

#NoneType
x=None
print(type(x))

#>>>Arithmetic Operations
a=10
b=3
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a//b) #Floor Division
print(a%b)  #Modulus|Remainder
print(a**b) #Exponential

#>>>input/ouput 
age=input("Wt is ur age: ")
print(age)

'''1.1 Common String Operations
#Concatenation
>>>Concatenate the string'''
message=input("Enter ur mssg : ")
name=input("Enter u r name : ")
print(message + " This is " + name)

boy_name=input("Enter boy name: ")
boy_age=int(input("Enter age"))
girl_name=input("Enter girl name: ")
girl_age=int(input("Enter age"))
age_diff= abs(boy_age-girl_age) #absolute value= gives only exact value but not -ve values

print(f"{boy_name} and {girl_name}, Age difference is str({age_diff})") 

#Repitition
greeting ="Hello! "
print(greeting*6)

#1.2 String Methods
#upper()
print(greeting.upper())
#lower()
print(greeting.lower())
#strip =>removes white spaces
print(greeting.strip())
#split
print(greeting.split("l"))
#replace
print(greeting.replace("Hello","Greetings"))
#length
print(len(greeting))

#1.3 Accessing string characters
name="Spoorthi"
print(name[5])
print(name[1:8]) #slicing[start,ends+1]
print(name[:5])
print(name[1:])
print(name[-4])
#slicing
print(name[::2]) #slicing[start,ends+1,strip|skip+1]