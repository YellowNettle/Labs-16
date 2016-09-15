__author__ = 'student'
a = 1
while a <= 100:
    if a % 3 == 0:
        if a % 5 != 0:
            print('Fizz')
        else:
            print('FizzBuzz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print(a)
    a += 1