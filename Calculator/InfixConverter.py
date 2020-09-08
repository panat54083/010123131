class Infix:
    def __init__(self, equation):
        self.equa = equation.replace(' ','')
        self.problam  = False

    def list_equation(self):
        SYMBOLS = set('+-*/()')
        equation = self.equa
        for i in range(len(equation)):
            
            if equation[i] == '-':
                if i == 0:
                    equation = '0' + equation[i:]
                elif equation[i-1] not in '0123456789':
                    print(i)
                    equation = equation[:i] + '0' + equation[i:]
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

    

    def check_problam(self):
        equation = self.list_equation()
        count = 0
        for ch in equation:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
        if count != 0 :
            if count > 0 :
                self.problam = True
            else:
                self.problam = True
        else:
            self.problam = False

    def calculateOperator(self, x, y, operator):
        if operator == '+':
            return float(x) + float(y)
        elif operator == '-':
            return float(x) - float(y)
        elif operator == '*':
            return float(x) * float(y)
        elif operator == '/':
            return float(x) / float(y)            

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

        # str_result = "%.2f" % round(float(str_result), 5)
        
        return str_result
    


if __name__ == "__main__":
    text1 = Infix('1+1+1+1+1+1')
    text2 = Infix('-2+2')
    print(text1.convertPostfix())
    print(text2.convertPostfix())
    print(text1.calculatePostfix())
    print(text2.calculatePostfix())
