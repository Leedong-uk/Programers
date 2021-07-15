def average(many):
    result=0
    for i in many:
        result+=i
    average=result/len(many)

    print("평균은 %d입니다" %average)

arr = []
print("평균 내고자 하는 수를 입력해주세요 ,로끊어서")
arr = input().split(",")
n=len(arr)
for i in range(0,n):
    arr[i] = int(arr[i])
print(arr)
print(n)


average(arr)

