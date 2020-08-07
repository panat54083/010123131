# 6201012610052 Assingment สำหรับ Boolean expression string ในข้อที่ 1
# ยังไม่สมบูณ์
# 17.50 07/08/2020 แก้ไขเล็กน้อย
# 01.55 08/08/2020 แก้ไขการแปลงเป็น postfix 

class boolExpStr():
    
    def __init__(self, equation):
        self.equa = equation.replace(" ","")
        
        self.items = []

    def putInList(self,equa): # นำสมการใส่เข้าไปใน list 
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

        print(equa)
        alphabet = ['0', '1', 'I1', 'I2','I3']
        priority = {'+':1, '&':1, '!':1, '(':0}
        postfix = []
        stack = []

        for ch in equa:
            if ch in alphabet :
                postfix.append(ch)
            elif ch in '!+&':
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
        
eq1 = boolExpStr("(I0&I1 + !(I1&I2))")
eq2 = boolExpStr("!(1+0)")
eq3 = boolExpStr("!(!(0+I0&1))")
eq4 = boolExpStr("((I0+!I1+!(I2))&(!I0+I1+I2)")
eq5 = boolExpStr("!(I0&I1)+!(I1+I2)")
eq6 = boolExpStr("(((I0&I1&!I2)+!I1)+I3)")

print(eq1.convertPost())
