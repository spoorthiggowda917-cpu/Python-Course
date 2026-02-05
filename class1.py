#CLASS1
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


print("--------------------------")
#CLASS2
#Lists
a=[1,2,3]
a.extend([4,5]) #to add more than 1 elements at the end
print(a)
a.extend(["string"])
print(a)
a.insert(1,8)
print(a)
print("--------------")
b=[5,6,7]
b.insert(9,8) #insert can be also added at last
print(b)
b.pop(2)
print(b)
print("--------------")
b1=[5,6,7,8,4,3,2,1,1,1,10,2,5,8]
b1.remove(8) #removes only first occured number,if its repeated
print(b1)
#filter(b1)  => doubt
b1.clear()
print(b1)
print("--------------")
list1=[4,8,5,6,7,9,2,1,3]
list1.sort()
print(list1)

list1.sort(reverse=True) #to sort in descending order
print(list1)

print("--------------")
list2=sorted(list1) # sorted is not a iterable function in list
print(list2)
list3=sorted(list1,reverse=True)
print(list3)

rev=[7,8,9,2,5,4,6,3,1]
rev.reverse() #reverses but wont be sorted
print(rev)

print("--------------")
a=[1,2]
b=[3,4]
c=[5,6,7]
a.extend(b) #to add two lists together but not as nested list
print(a+b) #it created new list but wont chnage original list
print(a)

print("--------------")
a=[1,2,3,4]
b=a.copy()
b.append(5)
print(b)
print(a)
# if we use copy "a" will not be changed when we make changes in "b",but if we use b=a, a can be changed originally.

print("--------------")
a.append("s")
print(a)
a.extend(["string",0])
print(a)
b=[8,7,6]
c=[4,56,8]
a.extend(b) #can also be used foe other list to add
print(a)
a.extend([b,c])
print(a)

print("--------------")
x=[1,2,3,4,5,6]
print(max(x))
x1=["apple","dog","mango"]
print(max(x1,key=len)) #gives the longest element in list
print(min(x1,key=len)) #shortest
print(sum(x))

print("--------------")
a=[1,2,3,4,5]
print(a[2:4])
print(a[::-1])

s="strrrring"
print(s.replace("r","")) #to remove element in string=>bcz there is no separate function for remove in string
print(s.replace("r","",1)) #removes only 1st occured element if repeated.
a=[1,2,2,2,2,3,5,4,6] #removes duplicate values
b=list(set(a))
print(b)

print("--------------------------")
#TUPLES =>in tuples only index and count is used nothing else
a=(1,2,3,4,5,6,7,8,9)
print(a.index(5))
print(a.count(6))