#submitted 30/04/2021
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            #print(stack)
            #print(elem)
            if elem == "+":
                thingy = stack.pop()
                stack[len(stack) - 1] = str(int(stack[len(stack) - 1]) + int(thingy))
                continue
            elif elem == "-":
                thingy = stack.pop()
                stack[len(stack) -1] = str(int(stack[len(stack) - 1]) - int(thingy))
                continue
            elif elem == "*":
                thingy = stack.pop()
                stack[len(stack) - 1] = str(int(stack[len(stack) - 1]) * int(thingy))
                continue
            elif elem == "/":
                isneg = False
                thingy = stack.pop()
                if (int(thingy) < 0):
                    isneg = True
                if int(stack[len(stack) - 1]) < 0:
                    isneg = not isneg
                stack[len(stack) - 1] = str(abs(int(stack[len(stack) - 1])) // abs(int(thingy)))
                if isneg:
                    stack[len(stack) - 1] = str(int(stack[len(stack) - 1]) * -1)
            else: 
                stack.append(elem)
                continue
        return int(stack[0])