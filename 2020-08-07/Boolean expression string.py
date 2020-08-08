# 6201012610052 Assingment สำหรับ Boolean expression string ในข้อที่ 1
# ยังไม่สมบูณ์
# 17.50 07/08/2020 แก้ไขเล็กน้อย
# 01.55 08/08/2020 แก้ไขการแปลงเป็น postfix
# 16.56 08/08/2020 เพิ่ม expression tree และแก้ไข postfix


class boolExpStr():
    
    def __init__(self, equation):
        self.equa = equation.replace(" ","")
#checkOperator        
    def isOperator(self, c):
        if c == '+' or c == '&' or c == '!':
            return True
        else:
            return False
#นำสมการใส่เข้าไปใน list 
    def putInList(self,equa): 
        SYMBOLS = set('+&!()')

        mark = 0 
        result = []
        for i in range(len(equa)):
            if equa[i] in SYMBOLS:
                if mark != i:
                    result.append(equa[mark:i])
                if equa[i] != ' ':
                    result.append(equa[i])
                mark = i+1
        if mark != len(equa):   
            result.append(equa[mark:len(equa)])

        return result
#Postfix 
    # สร้างเพื่อจะนำไปทำเป็น Tree 
    def convertPost(self):
        equa = self.putInList(self.equa)
        openC = 0

        for ea in equa:
            if ea == '(':
                openC += 1
            elif ea == ')':
                openC -= 1
        if openC != 0:
            print("Error equation, pls check barcket")
            if openC > 0:
                return "too '(' "
            elif openC < 0:
                return "too ')' "

        # print(equa)
        alphabet = ['0', '1', 'I1', 'I2','I3','I0']
        priority = {'+':1, '&':1, '!':1, '(':0}
        postfix = []
        stack = []

        for ch in equa:
            if ch in alphabet :
                postfix.append(ch)
            elif ch in '&!+':
                if len(stack) != 0 and priority[ch] <= priority[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(ch)
            elif ch == '(':
                stack.append(ch) 
            elif ch == ')':
                while (len(stack) != 0) and stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()

        while len(stack) != 0:
            postfix.append(stack.pop())
        return postfix
#ExpressionTree   
    class eT():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def inorder(self, t):
        if t is not None:
            self.inorder(t.left)
            print((t.value),inorder(t.right))

    def expressionTree(self):
        stack = []
        print(self.putInList(self.equa))
        print(self.convertPost())

        for ch in self.convertPost():
            if ch != '&+!': # operand
                t = self.eT(ch)
                stack.append(t)
            # elif ch == '!':

            else: # operator 
                # ดึงเอาตัวอักษร
                t = self.eT(ch)
                t1 = stack.pop()
                t2 = stack.pop()
                # put in right and left
                t.right = t1
                t.left = t2

                stack.append(t)
        
        t = stack.pop()           

        return t

        
eq1 = boolExpStr("(I0&I1 + !(I1&I2))")
eq2 = boolExpStr("!(1+0)")
eq3 = boolExpStr("!(!(0+I0&1))")
eq4 = boolExpStr("(I0+!I1+!(I2))&(!I0+I1+I2)")
eq5 = boolExpStr("!(I0&I1)+!(I1+I2)")
eq6 = boolExpStr("(((I0&I1&!I2)+!I1)+I3)")

# print(eq4.convertPost())
print(eq1.expressionTree())
