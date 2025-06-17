#Created by Guido van Rossum
#python is object oriented programming - concept of "objects" — which are real-world entities that contain data (attributes) and behavior (methods/functions).
#extension is .py
#identation is there (readability) equivalent to 4 spaces 
#multiline comment is not there but there is multi lines string which compiler does not read when it is not assigned to any variable 
print("Python !")
print("\n")
# the latest assigned will be considered if called 
# casting - assigning data type to a variable by declaring ; can check with type() 
# string can be single or double quotes both 
w = int(56)
q = str("Adam")
print(w)
print(q)
print("\n")
print(type(w))
print(type(q))
#camel case - only first small then next word first letter capital 
#Pascal - all first letter capital 
#Snake - all seperated by _
print("\n")
#multiple variables
e, r, t = 23, "Jules" , "s"
print(e)
print(r)
print(t)
print("\n")
#for one variable after anoher , there will be space if no space then + and in + same data type should be there different wont work 
u = "python"
i = "is"
o = "fun"
print(u, i, o, w)
print(u + i + o )
print("\n")
#global variable - variable declared outside the function
#inside function whatever local variable is there that will be only considered outside global will be considered ; inside function can use global keyword 

#datatypes - if j then complex    ; [] is list    ; {} is set   ; {  :   } is dictionary    ; () is tuple   ; frozenset is ({  })   ; b is for bytes 
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers     ; for that import random  
# format is print(random.randrange(1, 10))
# () function with this are constructors 
# if single quote in string use double quote and vice versa 

#if exact line and sequence then  : 
print ("""Twinkle twinkle
little star!!
It's a poem""")
print("\n")

# strings are arrays !!!!!!!!! so to acces any letter we use  []
p = "Strawberry"
print(p[0] , p[5])
print ("\n")
for l in p : 
    print(l)
    
print(len(p))
print("berry" in p)
print("berry" not in p)
print("verry" not in p)
#string slicing : 
print(p[3:6])
# here first is considered and last is not 
# to slice from first [:number] number is not considered 
# to slice till last then [number:] here last is considered
# in negative slicing opposite happends like [-5:-2] here -5 value wont be considered but -2 will be 
# front to last indexing   -   0 , 1, 2, 3.....
# last to front indexing   -    .....-3, -2, -1 
print('\n')
print(p.upper())
print(p.lower())
#to remove white space from begenning and end only we use strip()
print(p.replace('b', 'v'))
#The split() method returns a list where the text between the specified separator becomes the list items.


# we cant concatenate different datatype using + 
# so there is string format , f-strings   - format() 
# {} are placeholders 
# a placeholder can include modifier like {age:.2f} or math operations {2+3}
age = 18
texttt = f"legal age to vote is {age}" 
print(texttt)

#escape characters are \ characters 
# \r	Carriage Return (i.e simpliy brings the cursor to the next line)
#\ooo	Octal value	
#\xhh	Hex value


#bool of any value is true    except for o false , none , __len__ function and empty value 
# built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type
print("\n")
k = 200
print(isinstance(k, int))

# / division is upar ka value and % modulus is below value in division 

# precedednce is  - parentesis , exponent , unary , mul , div , floor div, modulus , add, sub, bitwise left , bitwise right , and , xor , or , comparision , identity , membership  , NOT , AND , OR