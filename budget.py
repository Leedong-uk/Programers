def solution(d, budget):
    answer = 0
    result=0
    d.sort()
    for i in d:
        result+=i
        answer +=1
        if result >budget:
            result=result-i
            answer-=1
            break
        
    return answer

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))
