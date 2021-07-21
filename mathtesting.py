def solution(answers):
    answer = []

    std1=[1,2,3,4,5]
    std2=[2,1,2,3,2,4,2,5]
    std3=[3,3,1,1,2,2,4,4,5,5]
    
    count1=0
    count2=0
    count3=0
    for i in range(len(answers)):
        if answers[i]==std1[i%len(std1)]:
            count1 +=1
        if answers[i]==std2[i%len(std2)]:
            count2+=1
        if answers[i]==std3[i%len(std3)]:
            count3+=1
    
    mac= max(count1,count2,count3)

    if mac==count1: 
        answer.append(1)
    if mac==count2:
        answer.append(2)
    if mac==count3:
        answer.append(3)
    answer.sort()

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
