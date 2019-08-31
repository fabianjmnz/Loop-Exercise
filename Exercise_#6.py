height = int(input('What should the height be? '))
width = int(input('What should the width be? '))
for i in range(height):
    if i == 0 or i == (height-1):
        print('*'* width)
    else:
        print('*'+(' '*(width-2)+'*'))