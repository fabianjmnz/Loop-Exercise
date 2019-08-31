#Exercise 1) 1 to 10
for i in range(1,11):
    print(i)
print('\n')

#Exercise 2) n to m
start = int(input('Enter a start number! '))
end = int(input('Enter a end number!'))
for i in range(start,end+1):
    print(i)
print('\n')

#Exercise 3) Odd Numbers
for i in range(10):
    if i%2 != 0 and i != 0:
        print(i)
print('\n')

#Exercise 4) Print a Square
a = '*'
number = 5
for i in range(number):
    print(a*number)
print('\n')

#Exercise 5) Print a Square 2
number = int(input('What length would you like the square to be? '))
a = '*'
for i in range(number):
    print(a*number)
print('\n')

#Exercise 6) Print a Box
height = int(input('What should the height be? '))
width = int(input('What should the width be? '))
for i in range(height):
    if i == 0 or i == (height-1):
        print('*'* width)
    else:
        print('*'+(' '*(width-2)+'*'))

#Exercise 7) Print a Triangle    LIKED
a = '*'
row = 20
column = 12
countdown = 0
for i in range(row):
    if i >= ((column//2)):  #checks the continuation of a symmetrical pyramid within given rows and columns
        break
    for j in range(column): 
        if j == ((column//2)): # checks if in the center of the # of columns
           pyramid = (' '*((column//2)-countdown))+(a*(2*(i+1)-1)) #equation
    countdown += 1        #part of equation
    print(pyramid)         #prints line by line 


#Exercise 8) Print a Triangle 2
a = '*'
row = int(input('How many rows would you like? '))
column = int(input('How many columns would you like? '))
countdown = 0
for i in range(row):
    if i >= ((column//2)):  #checks the continuation of a symmetrical pyramid within given rows and columns
        break
    for j in range(column): 
        if j == ((column//2)): # checks if in the center of the # of columns
           pyramid = (' '*((column//2)-countdown))+(a*(2*(i+1)-1)) #equation
    countdown += 1        #part of equation
    print(pyramid) 
print('\n')

#Exercise 9) Mulitplication Table
for i in range(1,11):
    for j in range(1,11):
        sum = i*j
        print(f'{i} x {j} = {sum}')
print('\n')

#Exercise Bonus: Print a Banner
message = input('What would you like your banner to say? ')
a = '*'
height = 3
width = len(message)+4
for i in range(height):
    if i == 0 or i == (height-1): 
        print('*'* width)
    else:
        print('* '+ message + ' *')
print('\n')
    
#Exercise Bonus: Triangle Numbers
j=1
for i in range(100):
        if i == 0:
            print(f'{j}  for when the triangle number is {i+1}')
        else:
            j= j+i+1
            print(f'{j}  for when the triangle number is {i+1}' )
print('\n')

#Exercise Bonus: Factor a Number
number = int(input('Input a Number! '))
print (f'Factors of {number} are: ')
for i in range(1,number+1):
    if i > (number//i):
        break
    if (number%i) == 0:
        print(f' {i} x {number//i}')
