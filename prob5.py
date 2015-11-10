'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?

Solution:

Multiply primes in range 1 to 20

1 2 3 5 7 11 13 17 19 = 9699690

Check if evenly divisble against remaining numbers

4 6 8 9 10 12 14 15 16 18

9699690 % 4 = 2

Multiply with lowest prime factor of the number if not evenly divisible
test again. (in this case 2 since 4 is 2*2)

Answer is 232792560
'''
