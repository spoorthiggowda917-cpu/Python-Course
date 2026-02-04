#constants
MAX_Count=1
MAX_COUNT=22
print(MAX_COUNT)

#String
a="1-?ABCDE123"
print(len(a))
b="banana"
print(b.count("a")) #how many times a appers in banana
print(b.count(a))#doubt

c=["banana","apple","apple"] #duplicates can be used in list
print(c.count("apple"))

x="   ".join(c) #addd this string btw string in list
print(x)

#String Concatenation
x1="spoorthi"
x2="G"
x3=" ".join([x1,x2])
#or x3=x1+" "+x2 
print(x3)

#reverse
d="string2"
d1=d[2::-2] #slicing[start from where it mentioned and go reverse for working]
print(d1)

#Capitalize()=>cpas the 1st word
w=d.capitalize()
print(w)
print(d.startswith("s"))
print(d.endswith("2"))
print(d.islower())
print(d.isupper())
print(d.isnumeric()) #OR
print(d.isdigit())
print(d.isalpha()) #checks for aplhabets
print(d.isalnum()) #checks both but special char are exception

#split
print(d.split("n")) #splis at the char mentioned
#strip
s1="         replace      "
print(s1.rstrip(" ")) #removes right spcaes in string
print(s1.lstrip(" ")) #removes left