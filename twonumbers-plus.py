def solution(numbers):
    answer = []
    total=[]
    n=len(numbers)
    for i in range(0,n):
        for j in range (i+1,n):
            k=numbers[i]+numbers[j]
            if k not in total:
                total.append(k)

    total.sort()       
    return total

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))

