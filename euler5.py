def smallestmultiple():
    number = 2
    loop   = True
    while loop:        
        for n in range(2,21):
            if number%n != 0:
                continue    
            return n
        number += 1
       
    
