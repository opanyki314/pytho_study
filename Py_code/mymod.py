def countLines(name):
    f=open(name)
    count = 0
    if(f):
        for i in f: count += 1
        print("The file has %s lines" % count)
    else: print("Can't open the file.")

def countChars(name):
    f = file(name)
    count=0
    if(f):
        for i in f.read():
            for j in i: count += 1
        print("The file has %s characters" % count)
    else: print("Can't open the file.")
def test(name='saveit.txt'):
