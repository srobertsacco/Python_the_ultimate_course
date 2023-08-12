## string manipulation

a = 1
b = 2.5
c = "MyString"

y= a + b
print(y)
print(c)

## user input

Name = input('Enter Your Name:')
Age = input("Enter Your Age:")

print("My Name is:", Name)
print("My Age is:", Age)

## math operators

a = 100
b = 20

z = a + b 
print("z value is", z)

z = a - b
print("z value is", z)

z = a/b
print("z value is", z)

z = a * b
print("z value is", z)

## random number generator

import random

x =random.randint(0,2)
print("random number is:", x)

## Projct Names and Random Score

import random

Name1 = input("Enter First Name:")
Name1RandomNumber = random.randint(0, 10)

Name2 = input("Enter Second Name:")
Name2RandomNumber = random.randint(0, 10)

Name3 = input("Enter Third Name:")
Name3RandomNumber = random.randint(0, 10)

print(Name1, "Got a value of:", Name1RandomNumber)
print(Name2, "Got a valule of:", Name2RandomNumber)
print(Name3, "Got a value of:", Name3RandomNumber)

## if statements

skillpoints = 15

if skillpoints < 15:
    print("Welcome to city 1. THis is the easy part.")
    
  ## if elif else
  
forwardButton = True
  
backwardButton = True 

#0 : no rotation
#1 : clockwise rotation FW
#2 : anti-clockwise rotation BW

motorstatus = 0

if forwardButton == True:
    motorStatus = 1
    print("Car is moving forward")

elif backwardButton == True:
    motorstatus = 2
    print("Car is moving Backward")
    
else:
    motorstatus = 0
    print("Car is not moving")
    
## project grade

grade = int(input("Enter the Grade: "))

if grade>90:
    print("You Got an AA! Congrats!")

elif grade>85:
    print("You Got an BA! Congrats!")

elif grade>80:
    print("You Got an BB! Congrats!")

elif grade>75:
    print("You Got an CB! Congrats!") 
    
elif grade>70:
    print("You Got an CC! Congrats!") 
    
elif grade>65:
    print("You Got an CD! Congrats!")
    
elif grade>60:
    print("You Got an DC!")
    
elif grade>55:
    print("You Got an F! You suck!")
  
  
## lists

names= ["James","Elli","MrHamsho","Adem","Aida"]
ages= [24, 25, 21, 48, 17]
print(names[5], ages[5] )

## list append

shoppingCart = ['Oranges', 'Milk', 'Almonds']

item = input("please enter the name of the product:")
shoppingCart.append(item)

item = input("please enter the name of the product:")
shoppingCart.append(item)

item = input("please enter the name of the product:")
shoppingCart.append(item)

print("Your items are:", shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']
shoppingCart.clear()
print(shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']
shoppingCart.remove("Almond")
print(shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']

shoppingCart.pop()
print(shoppingCart)

shoppingCart = ['Oranges', 'Milk', 'Almonds']

length = len(shoppingCart)
print(length)

shoppingCart.clear()

if len(shoppingCart) == 0:
    print("Your shopping cart is empty!")

database = [ ["John", "MrHamsho"]  , [25, 29] ]

print(database[0][1])
print(database[1][1])

while(1):
    userInput = input("Enter a letter")
    print(userInput)
    
    if userInput == 'exit':
        break 
    
t = ("A", "B", "C")

## finite machines

state=1
while(1):
    transit = input("Enter a letter: ")
    print("You have entered", state)
    
    if state == 1:
        if transit == 'W':
            state = 2

    elif state == 2:
    
        if transit == 'G':
            state = 3
        
        elif state == 2:
            if transit == 'G':
                state= 3
            
            elif transit == 'S':
                state=1
                
        elif state == 3:
            if transit == 'L':
                state=1
        print("Right NOw you are in state:", state)
        
        ## Enumerate
        
    cars = ["BMW", "Hyundai", "Toyota", "Jaguar"]
    
    for i, items in enumerate(cars):
        print(items)
        print(i)
        
l = ["apples", "bananas", "strawberries"]
 
for element in l:
    print(element)
    
a = [1,3,5,7,9]

for element in a:
    element= element+2
    print(element)
    
for i in range (0, len(a) ):
    a[1] = a[i] + 2
    
print(a)

shapes = ["square", "circle", "triangle"]
centers = [ (10,10), (50,50), (100,100)]
colors = ["red", "blue", "yellow"]

#for i in range (0, len(shapes)):
#   print(shapes[1], centers[1])

for shape, center, color in zip(shapes, centers, colors):
    print(shape, center, color)
    
s= "This is nice"
#print(s)

li0ifNumbers = [x for x in range(10) if x%2 ==0]
print(li0ifNumbers)

#4px x 4px
# 16x x 16x

imagePixels = [ 
               [0,0], [1,0], [2.0], [3.0]
               [0.1], [1.1], [2.1], [3.1]
               [0.2], [1.2], [2.2], [3.2]
               [0.3], [1.3], [2.3], [3.3]
               
            ]

#shift x axis 3 pixles to the right 
for i in range(0 , len(imagePixels)):
    imagePixels[i][0]= imagePixels[i][0] + 3

print(imagePixels)

#shift Y axis 2 pixels downwards
for i in range(0 , len(imagePixels)):
    imagePixels[i][0]= imagePixels[i][0] + 2
    
print(imagePixels)

## functions

db1=["kate", "Moss", "David"]
db2=["Lee", "Steve"]
db3=["Tony", "Lara"]

def addToDatabase(name):
    
    global db1
    global db2
    global db3
    
    db1=[name]
    db2=[name]
    db3=[name]
    
    
addToDatabase('John')
addToDatabase("MrHamsho")
print("Db 1 is:", db1)
print("Db 2 is:", db2)
print("Db 3 is:", db3)

def pwr2(num):
    pw2= num*num
    div = num/num
    return pw2, div

pw2, div= pwr2(5)
print("pw2 is ", pw2)
print("div is ", div)


