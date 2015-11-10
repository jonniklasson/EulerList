'''
Load a file with a string of numbers
read 13 numbers, save the product
increase index by one if product is greater than
previous saved replace.
Continue until string is consumed
'''

'''
Modify read file function for new file.

'''


'''
string[n:13+n]
from n = 0 untill n = 1000-13
if 0 is in number return 0
'''
from functions.readfile import readfile
source = "data/problem8_1kNumbers.txt"

def product (string):
    val = 1
    for v in string:
        if int(v) == 0:
            return 0
        val *= int(v)
    return val

numbers = readfile(source)
saved   = 0
for n in range(0,987+1):
    prod = product(numbers[n:13+n])
    if prod > saved:
        saved = prod
print('answer is.. : %s' %(saved))    
    



