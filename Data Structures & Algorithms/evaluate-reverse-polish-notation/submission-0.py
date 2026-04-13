class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+","-","*","/"]
        for i in tokens:
            
            if i in operations:
                a = stack.pop()
                b = stack.pop()
                
                if i == "+":
                    stack.append(int(a+b))
                elif i == "-":
                    stack.append(int(b-a))
                elif i == "*":
                    stack.append(int(a*b))
                elif i == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(i))
                
            
        return stack.pop()
                

        