def kaboom(x,y):
    print(x+y)

try:
    kaboom([0,1,2], 'spam')
except TypeError:
    print('Mda!')
print('resuming here')
