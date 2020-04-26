fname = input('enter the file name: ')
try:
    fh = open(fname)
except:
    print('code is wrong')
    quit()

for abc in fh :
    dd = abc.rstrip()
    print(abc.upper())
