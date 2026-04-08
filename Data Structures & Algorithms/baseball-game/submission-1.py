class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scorestacks = [int(operations[0])]
        summation=0
        for i in operations[1:]:
            if i == "C":
                scorestacks.pop()
            elif i == "+":
                b = scorestacks.pop()
                a = scorestacks.pop()
                c = int(a)+int(b)
                scorestacks.append(a)
                scorestacks.append(b)
                scorestacks.append(c)
            elif i == "D":
                a = scorestacks.pop()
                c = int(a)*2
                scorestacks.append(a)
                scorestacks.append(c)
            else:
                scorestacks.append(int(i))
            print(i, scorestacks)
        for j in scorestacks:
            summation += int(j)
        return summation

            
            
            
            
