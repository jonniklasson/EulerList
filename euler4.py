import math

def findpalindrome():
    for n in range(997002,10099, -1):
        if numbertest(n) == True:
            check = findproduct(n)
            if check != False:
                out1 = n
                out2 = n/check
                out3 = check
                return('largest palindrome found is %s, product of %s and %s'
                      % (str(out1),str(out2),str(out3)))

def reversenumber(number):
    numLen  = int(math.log(number,10))
    resNum  = 0
    for n in range(numLen+1):
        k = numLen - n
        tempNum = number%10
        number  = number//10
        resNum  += tempNum * (10**k)
    return resNum
    

def findproduct(number):    
    for n in range(100, number//2):
        if number%n == 0 and (number/n) < 1000 and n < 1000:
            return n
    else:
        return False

def numbertest(number):
    #log 10 of the number converted to int, number 1111 = 3
    potent = int(math.log(number,10))
    #integer division (3//2 = 1) number = 1111 -> x = 10
    x = 10**((potent)//2)
    #number = 1111 x = 10 term = 100
    term = 10**int(math.log(number//x,10))
    #simple, integer division by 10 removes last number
    #1111//100 = 11 (first 2 digits)
    #modulus gives last number
    #1111%100  = 11 
    first = number//term
    last  = number%(10*x)
    first = reversenumber(first)
    
    if first == last:
        return True
    else:
        return False


