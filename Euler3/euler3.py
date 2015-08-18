import math

'''
Given a filename, opens the file and reads each line and returning a
list of non-whitespace characters converted into integer
used to create a list of primes from a plain text with primes.
filename, string of 
'''
def readprimes (filename):
    lines = []
    primes = []
    file = open(filename, 'r')
    #trailing and preceding whitespace removal
    all = [ line.rstrip() for line in file.readlines() ]

    #ignore empty lines
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    numstring = ''
    for line in lines:
        linesplit = line.strip(' ')
        for k in linesplit:
            if k == ' ' and numstring[-1] == ' ':
                #if previous char is whitespace, ignore and go to next
                continue
            else:
                numstring += k

    primes = numstring.split(' ')
    out = []
    for char in primes:
        out.append(int(char))
    return out

def primefactor (number, primes=readprimes("primes.txt")):

    '''
    First consider the edge case, in the case of an even number
    the max prime factor value is given by number = 2 * maxfactor
    If odd, it is instead number = 2 * 3 * maxfactor
    
    '''
##    if number % 2 == 0: #number is even
##        lim = number//2
##    else:
##        lim = number//6 #number is odd

    primes = primes[::-1] #reverse list, looking for max value (perhaps not optimal)

    for n in primes:
        if number % n == 0:
            return n
        
print(primefactor(600851475143))


    
