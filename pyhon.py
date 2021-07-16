arr = []
print("평균 내고자 하는 수를 입력해주세요 ,로끊어서")
arr = input().split(",")
print(arr)
n=len(arr)
for i in range(0,n):
    arr[i] = int(arr[i])
print(arr)
print(n)    