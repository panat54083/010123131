class Infix:
    def __init__(self, equation):
        self.equa = equation.replace(' ','')
    
    def list_equation(self):
        SYMBOLS = set('+-*/()')
        equation = self.equa
        mark = 0
        result = []
        for i in range(len(equation)):
            if equation[i] in SYMBOLS:
                if mark != i:
                    result.append(equation[mark:i])
                if equation[i] != ' ':
                    result.append(equation[i])
                mark = i+1
        if mark != len(equation):   
            result.append(equation[mark:len(equation)])

        return result

    def calculateOperator(self, x, y, operator):
        if operator == '+':
            return int(x) + int(y)
        elif operator == '-':
            return int(x) - int(y)
        elif operator == '*':
            return int(x) * int(y)
        elif operator == '/':
            return int(x) / int(y)            

    def convertPostfix(self):
        priority = {'+':1,'-':1,'*':2,'/':2,'(':0}
        postfix = []
        stack = []

        equation = self.list_equation()
        for ch in equation:
            if ch not in '+-*/()':
                postfix.append(ch)
            elif ch in '+-*/':
                if len(stack) != 0 and priority[ch] <= priority[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while (len(stack) != 0) and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
        
        while len(stack) != 0:
            postfix.append(stack.pop())
        return postfix

    def calculatePostfix(self):
        equation = self.convertPostfix()
        SYMBOLS = set('+-*/')
        stack = []
        str_result = ''
        
        for ch in equation:
            if ch not in SYMBOLS:
                stack.append(ch)
            elif ch in SYMBOLS:
                ch2 = stack.pop()
                ch1 = stack.pop()
                stack.append(self.calculateOperator(ch1, ch2, ch))
        
        for i in stack:
            str_result = str_result + str(i)
        
        return str_result


if __name__ == "__main__":
    text1 = Infix('1+1+1+1+1+1')
    print(text1.convertPostfix())
    print(text1.calculatePostfix())