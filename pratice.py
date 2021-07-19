print("정수의 개수를 입력하세요")
n=int(input())

arr= []
print('정수를 입력하세요')
arr = input().split()

for i in range(0,n):
    arr[i] = int(arr[i])

Max = -1000000
Min = 1000000
for i in arr:
    if i > Max:
        Max=i
    if i < Min :
        Min=i

print("최대값:",Min, "최소값:",Max)
