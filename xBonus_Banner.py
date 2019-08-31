message = input('What would you like your banner to say? ')
a = '*'
height = 3
width = len(message)+4
for i in range(height):
    if i == 0 or i == (height-1): 
        print('*'* width)
    else:
        print('* '+ message + ' *')