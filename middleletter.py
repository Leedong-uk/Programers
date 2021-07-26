def solution(s):
    n=len(s)
    answer=''
    total=list(s)

    if n%2==1:
        k=round(n/2)
        answer=str(total[k])
    else:
        k=int(n/2)
        answer=str(total[k-1]+total[k])
        
       
    return answer



print(solution("abcde"))
print(solution("qwer"))
