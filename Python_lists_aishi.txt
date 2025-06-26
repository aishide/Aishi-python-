#To store collections of data there are 4 built in data types 
#list 
#tuples
#set 
#dictionary
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""


#LIST
#list items are indexed from 0 to ........
#order of the list does not change , if we add any item then it will add in the last
# is it changable i.e we can add , change or remove
# as list items are indexed duplicate items are allowed 
print("LIST \n")
myList = ["bag" , "book" , "pen" , "sharpner", "highlighter"]
numList = [4, 5 , 3, 2, 2]
print(numList)
print(myList)
#length 
print(len(myList))
# a lisyt can contain different datatypes
list1 = ["aishi", 2, "Python" , 'a' , 5.6]
print(list1)
#type
print(type(myList))
# can use list constructor to create list too
list2 = list(("apple", 5, "BANANA", True , 'e'))
print(list2)
# for declaring boolean values true and false the T of True must be capital and f pf false other wise string
#accessing item 
print(list2[2])
#here too negative indexing and range i.e [ : ]
# to check existence of item 
print("apple" in list2)
print("Apple" in list2)
print("Aishi" not in list2)
# change value of item 
list2 [1] = "Guava"
print(list2)
list2 [1:3] = ["blackcurrant", "watermelon"]
print(list2)
#multiple items ki space leke we can assign it only 1 value too 
# The insert() method inserts an item at the specified index:
list2.insert(2, "watermelon")
print(list2)
print("\n")
list2.append("Aishi")
print(list2)
print("\n")
list2.insert(1, "ais")
print(list2)
print("\n")
list2.extend(numList)
print(list2)
#in extend here we can extend or append set dictionary and other too its not compulory here that we have to extend it with list only   ; output is a list only 
list2.remove("e")
print(list2)
#if the item in the remove is multiple in list then it will remove it once which will come first 
# remove takes only 1 item we cant remove multiple items at once in pop also only 1 item at a time 
list2.pop(9)
print(list2)
#if pop item is not mentioned it is blank i.e () then it will automatically remove the last element 
del list2[0]
print(list2)
# del and then the list name - will delete the whole list 
#clear clears the list names an empty list with not a single item in it 
myList.clear()
print(myList)

print("\n")
print("\n")

LIST = ["Aishi" , "Loves" , "Dogs"]
for x in LIST:
    print(x)
print("\n")
#through index 
for i in range(len(LIST)):
    print(LIST[i])
print("\n")
#using while loop 
i = 0 
while i <len(LIST):
    print(LIST[i])
    i = i+1
    
# OR USING LIST COMPREHENSION 
[print(x) for x in numList]
print("\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#or 
print("\n")
newlist = [x for x in fruits if "a" in x]
print(newlist)
# syntax ---> newlist = [expression for item in iterable if condition == True]
#.sort() sorts the list alphabetically and numerically 
print("\n")
LIST.sort()
print(LIST)
print("\n")
#for descending in () we write reverse = True  (only t capital else small)
#or simply .reverse()
LIST.sort(reverse = True)
print(LIST)
#sort is case sensetive it will first sort the caputal once first then the small once 
# to sort without case sensetive in  () we write  key = str.lower
print("\n")
NEW = ["apple" , "BANANA" , "Mango" ,"orange" , "KIWI" ]
print(NEW)
NEW.sort()
print(NEW)
NEW.sort(key = str.lower)
print(NEW)
print ("\n")
print("\n")
#copy list :
Fruits = NEW.copy() 
print(Fruits)
#or
FRUITS = list(NEW)
#list should be in all small letters 
print(FRUITS)
#or using a slice operator [:]
#example
FRUit = NEW[:]
print(FRUit)
print("\n")
print("\n")
#joining to lists 
NEWw = FRUITS + fruits
print(NEWw)

# or 
for x in fruits:
    FRUITS.append(x)
print(FRUITS)

#or 
FRUITS.extend(fruits)
print(FRUITS)

"""
So the functions are 
append() , clear(),  copy(), count() , extend(), index() , insert() , pop(), remove(), reverse() , sort()"""