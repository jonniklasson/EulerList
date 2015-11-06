
from readfile import readfile

numbers = str.split(readfile('gridnumbers.txt'))
for k in range(len(numbers)):
    numbers[k] = int(numbers[k][0])*10+int(numbers[k][1])

def Square():
    out = 0
    for n in range(0,400-63):
        j = n+20
        k = j+20
        l = k+20
        #print(numbers[n],numbers[j],numbers[k],numbers[l])
        #horizontal
        p1 = numbers[n]*numbers[n+1]*numbers[n+2]*numbers[n+3]
        p2 = numbers[j]*numbers[j+1]*numbers[j+2]*numbers[j+3]
        p3 = numbers[k]*numbers[k+1]*numbers[k+2]*numbers[k+3]
        p4 = numbers[l]*numbers[l+1]*numbers[l+2]*numbers[l+3]
        #vertical
        p5 = numbers[n]*numbers[j]*numbers[k]*numbers[l]
        p6 = numbers[n+1]*numbers[j+1]*numbers[k+1]*numbers[l+1]
        p7 = numbers[n+2]*numbers[j+2]*numbers[k+2]*numbers[l+2]
        p8 = numbers[n+3]*numbers[j+3]*numbers[k+3]*numbers[l+3]
        #diagonal
        p9 = numbers[n]*numbers[j+1]*numbers[k+2]*numbers[l+3]
        p10 = numbers[n+3]*numbers[j+2]*numbers[k+1]*numbers[l]
        res = max(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10)
        out = max(res,out)
        print(out)
    return out
Square()
           
