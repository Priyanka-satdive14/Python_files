for num1 in range(1,100):
    if (num1 % 3 ==0) and (num1 %5 ==0):
        print (f'{num1} FizzBuzz')
    elif (num1 % 3==0):
        print (f'{num1}  Fizz')
    elif (num1 % 5==0):
        print (f'{num1} Buzz')