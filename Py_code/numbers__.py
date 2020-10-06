for i in range(1,100):
    if i%3 == 0:
        if i%5 == 0:
            print('Fizz',end='')
        else:
            print('Fizz')
    elif i%5 != 0:        
        print(i)
    if i%5 == 0:
        print('Buzz')
