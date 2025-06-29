#Tuple
#A tuple is a collection which is ordered i.e all items have a defined order and are unchangeable or "immutable" meaning that you cannot change, add, or remove items once the tuple is created
#Tuples are written with round brackets()
my_tuple=("cat", "dog", "cow")
print(my_tuple)

#tuples are indexed so they can have multiple same values (which will have different index)
print(len(my_tuple))
print("\n")
#this is a 1 item tuple
thistuple = ("apple",)
print(type(thistuple))
#this is not a tuple "below" as this is a string 
thistuple = ("apple")
print(type(thistuple))
#tuplecan contain differentt data types

#we can create table with with a tuple constructor too
print("\n")
tup = tuple(["Hello", "I", "am" , "under" , "the", "water"])
print(tup)
print("\n")
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[1:2])
print("\n")
#to check item in tuple
if "dog" in my_tuple:
    print("Yes it is!")
    
# for adding we can first convert it into list add it and then convert it back into tuple 
y = list(my_tuple)
y[1] = "Tiger"
y.append("Lion")
print(y)
tupp = tuple(y)
print(tupp)
print("\n")

#we can add tuple after tuple
T = ("Tell", "me", "whyy")
y = ("Ain't" , "nothing", "but" , "a" , "heartbreak")
T += y
print(T)
#if we are adding a single item only tuple then after 1 item only we add a single commma 
#can't remove items from a tuple 
# for that too you can convert into list first then remove and then again to tuple 

#we can completely delete a tuple by using del keyword 
del tupp
print(tupp)

#normally assigning a value to tuple is known as packing 

#we are also allowed to extract the values back into variables. This is called "UNPACKING"
q = ("red" , "yellow" , "green")
(boy , girl , man) = q
print(boy)
print(girl)
print(man)
print("\n")
#If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list (it will take the remaining values) 
# if we put astericks * in second variable then the except first and last all value will be in the second variable in the form of variables 
# * should be before the variable 

#loop to print all the values of the tuple 
for x in q:
    print(x)
print("\n")
#prrinting through the index 
for i in range (len(q)):
    print(q[i])
print("\n")
# using while loop 
i = 0
while i < len(q) :
    print(q[i])
    i = i+1
print("\n")

# join tuples 
w = ("I" , "am" , "Enjoying")
e = ("Coding", "Python")
r = w+e
print(r)
print("\n")

#multiplying 
t = e * 2
print(t)
print("\n")

num = ( 2, 4, 6, 3 , 7, 5, 7, 3, 2, 9)
h = num.count(7)
j = num.count(9)
print(h)
print(j)
print("\n")

print(num.index(4))
print(num.index(7))
