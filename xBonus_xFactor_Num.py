number = int(input('Input a Number! '))
print (f'Factors of {number} are: ')
for i in range(1,number+1):
    if i > (number//i):
        break
    if (number%i) == 0:
        print(f' {i} x {number//i}')