def solution(strArr):
    answer = [strArr[i].upper() if i % 2 else strArr[i].lower() for i in range(len(strArr))]
    return answer
