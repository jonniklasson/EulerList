##
##new side a	new side b	new side c
##T1:	a − 2b + 2c	2a − b + 2c	2a − 2b + 3c
##T2:	a + 2b + 2c	2a + b + 2c	2a + 2b + 3c
##T3:	−a + 2b + 2c	−2a + b + 2c	−2a + 2b + 3c

def TreeFindPythagoras(a,b,c)
    if a+b+c == 1000:
        return (a,b,c)
    elif a+b+c < 1000:
        TreeFindPythagoras((a-2b+2c),(2a-b+2c),(2a-2b+3c))
        TreeFindPythagoras((a+2b+2c),(2a+b+2c),(2a+2b+3c))
        TreeFindPythagoras((-a+2b+2c),(-2a+b+2c),(-2a+2b+3c))

        
    #left
    a - 2b +
    2c	2a - b + 2c
    2a - 2b + 3c
    #middle
    a + 2b + 2c
    2a + b + 2c
    2a + 2b + 3c
    #rigth
    -a + 2b + 2c
    -2a + b + 2c
    -2a + 2b + 3c
