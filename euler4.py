import math

def numbertest(number):
    #potent gives the amount of "zeroes" in the number
    potent = int(math.log(number,10))
    #gives a number in the form 10**x same length as half the number
    x = 10**((potent)//2)
    term = 10**int(math.log(number//x,10))
    #gives half of the digits, except middle if odd
    first = number//term
    last  = number%(10*x)
##    print(potent)
##    print(x)
##    print(first)
##    print(last)
    loop = 0
    tempString = ''
    tempNumber = 0
    while loop < ((potent+1)//2):
        tempNumber = first%10
#        print(tempNumber)
        first      = first//10
        tempString += str(tempNumber)
        loop +=1
    first = int(tempString)
    
##    print(first)
    
    if first == last:
        return True
    else:
        return False
#find all palindromes in the range
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
#find 
def findproduct(number):    
    for n in range(100, number//2):
        if number%n == 0 and (number/n) < 1000 and n < 1000:
            return n
    else:
        return False
