'''
Sum all natural numbers below 1000 that are divisible by 3 and 5

'''
temp = 0
for n in range(1,1000):
    if (n%3 == 0) or (n%5 == 0):
        temp += n
print(temp)
