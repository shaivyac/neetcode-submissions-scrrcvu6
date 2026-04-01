class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        opening = {'{':'}','(':')','[':']'}
        closing = {'}':'{',')':'(',']':'['}
        for i in s:
            if i in opening.keys():
                stack.append(i)
            elif i in closing.keys():
                #print(stack[-1])
                if stack and stack[-1]==closing[i]:
                    stack.pop()
                else:
                    return False
            print(stack, i)
        if len(stack)>0:
            return False
        return True



        