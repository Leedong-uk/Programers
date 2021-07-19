def solution(a, b):
    answer = 0
    a_len=len(a)
    for i in range(0,a_len):
        product=a[i]*b[i]
        answer+=product
    return answer

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))
