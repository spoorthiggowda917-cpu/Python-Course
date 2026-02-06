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

