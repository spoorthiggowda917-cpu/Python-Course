#CLASS1 => 3/2/26
_a=1

age=int(input("wt is ur age: "))

age= str(age)#need to define separately

print(type(age))

print(age,end="---")

a=0
b=float(a)
print(b)

s="""hello
hi
spoorthi """ #triple quotes/multine can be written
s1='hello' #single
s2="hello" #double
var = 'Hi,"Spoorthi"'#if we need add quotes in print
print(var)
var1 = "Hi,'Spoorthi'"
print(var1)
s1=""" 'hi',"hello"::"""
print(s1)
a='"""hello"""' #triple quotes inside single quotes
print(a)

a="hello\"Hi\"" #escaping the double quotes
print(a)
b="hi,\"\"\"Spoorthi\"\"\"  " #escaping each quotes
print(b)
c=""" \"\"\"Spoorthi\"\"\" """
print(c)
d=' \"\"\"Spoorthi\"\"\" '
print(d)

a="Spoorthi"
print(a[-8])

a=-8
b=bool(a)
type(b)

a="TrUe"
b=bool(a) #boolean shd be given as capital
type(b)

a=False
print(a,type(a))

a=["Python","Java","Js"]
a[1]="React" #cant assign in tuple but can assign in list
print(a[1])
print("--------------------------")

#CLASS2 => 4/2/26
#constants
MAX_Count=1
MAX_COUNT=22
print(MAX_COUNT)

#String
a="1-?ABCDE123"
print(len(a))
b="banana"
print(b.count("a")) #how many times a appers in banana
print(b.count(a))

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

#CLASS3 => 5/2/26
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
print("--------------------------")

#CLASS4 => 6/2/26
#Sets 
#Sets wont be in ordered, so there is no indexes and slicing cant be done
s={5,8,6,2,3,1,3,3,3}
s.update([1,2,3,4]) #no duplicates will be added and sets always will be in order
s.remove(2)
print(s)

s1={7,8,9,5,4}
s1.pop()       # removes random number, not the last one
print(s1)
s1.discard(10) #dicard doesnot give any error if the number is not in the set ,but remove does
print(s1)
s1.clear()
print(s1)
s1.add(10) #add
s1.update([2,2,2,3,4,1,5,8,7])
print(s1)
print("--------------------------")

#Union
sp={"Python","React","C"}
v={"Python","C","J"}
print(sp.union(v))         #same as below
print(v.union(sp))
#Intersection
print(sp.intersection(v))  #same
print(v.intersection(sp))
#Differenece
print(sp.difference(v))    #gives which is present in "sp" but not in "v"
print(v.difference(sp))
print("--------------------------")

#Subsets
a={"P","J","C"}
b={"P","J","C"}
print(a.issubset(b))   #both are true
print(b.issubset(a))
#Supersets
print(a.issuperset(b)) #both are true
print(b.issuperset(a))

#Dictionaries =>{Key:Value}
a={
    "Name":"Spoorthi",
    "Age":21,
    "Skills":{"Python","Java"},
    2004:"Yes"
}
a["Age"]=22               #To update/modify => dict["key"]=value
a["Hobbies"]="dancing"    #to add
del a[2004]               #to delete
print(a.pop("Age"))       #pop=>not pops last item but whatever mentioned
print(a)
print("-------------")

a={
    "k":"v",
    1:"2",
    2:"3",
    3:"4"
}
print(a.keys())      #keys 
print(a.values())    #values
print(a.items())     #both
print("-------------")

a={
    "Dog":"dog",
    "Cat":"cat"
}
print(a.get("buffalo","persian"))  #persian wont be added to original dict but just return instead of none
#print(a["buffallo"])              #gives error if keys are not there but get wont give error
print(a.popitem())                 #removes last item
print(a)

#Complex => real+imaginary
a=2+3j
print(type(a))



