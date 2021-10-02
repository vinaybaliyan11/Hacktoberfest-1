print('enter 1 for addition')
print('enter 2 for subtraction')
print('enter 3 for division')
print('enter 4 for multiplication')
print('enter 5 for exponents')
print('enter 6 for remainder')
print('enter 7 for percentage')
print()
def simple_calc():
    a = input('enter the sign of calculaton = ' )
    if a == '7':
        b = int(input('enter the achieved score = '))
        c = int(input('enter total score = '))
        percent = b / c * 100
        print(f'you have scored {percent} percent')
    else:
        b = int(input('enter the first number = '))
        c = int(input('enter the second number = '))
    if a == '1':
        add = b + c
        print('addition of these numbers = ' + str(add))
    elif a == '2':
        subtract = b - c
        print('subtraction of these numbers = ' + str(subtract))
    elif a == '4':
        multiply = b * c
        print('multiplication of these numbers = ' + str(multiply))
    elif a == '3':
        fdivide = b / c
        print('division of these numbers = ' + str(fdivide))
    elif a == '5':
        power = b ** c
        print('power of these numbers = ' + str(power))
    elif a == '6':
        remainder = b % c
        print('remainder of these numbers = ' + str(remainder))
    print()
    print('enter \'c\' to continue')
    print('enter \'e\' to exit')
simple_calc()
print()
i = 0
while i == 0:
    a = input('enter \'c\' or \'e\' : ')
    if a == 'e':
        i += 1
    else:
        simple_calc()
