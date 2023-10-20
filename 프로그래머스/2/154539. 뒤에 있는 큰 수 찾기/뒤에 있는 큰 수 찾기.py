def solution(numbers):
    answer = [0] * len(numbers)
    stack = []
    for i in range (len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    for i in stack:
        answer[i] = -1
    
    return answer