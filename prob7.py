#What is the 10 001st prime number?

#Primes found via Eratosthenes Sieve

import math

def ErSieve(number=10000):
        ##
        ##                number = 1000
        ##
        limit  = int(math.sqrt(number))+1

        numbers = list(range(2,number+1))

        tdList = []
        
        # append tdList with list of [int, boolean]
        for n in range(len(numbers)):
          temp = [numbers[n],True]
          tdList.append(temp)

        # set non primes to false
        for j in tdList:
                if j[0] <= limit:       #only need to use numbers untill sqrt(n)
                  if j[1] == True:
                          for i in range(j[0],number+1,j[0]):
                                  if i != j[0]:
                                      tdList[i-2][1] = False

        #want to count the number of primes found
        numberprimes=0
        prime = 0
        for j in tdList:
                if j[1] == True:
                        if numberprimes == 10001:
                                return numberprimes, prime
                        numberprimes += 1
                        prime = j[0]
                        #print(prime)


        return ErSieve(number+1000)
