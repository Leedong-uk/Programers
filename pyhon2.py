num1=int(input())
num2=int(input())
num3=int(input())

cal=num1 * num2 * num3

cal2=str(cal)
cal3=list(cal2)

n=len(cal3)

for i in range(0,n):
    cal3[i]=int(cal3[i])

for i in range (0 ,10):
    a=cal3.count(i)
    print(a)
    

