# 6201012610052 Assingment สำหรับ Boolean expression string ในข้อที่ 1
# ยังไม่สมบูณ์
# 17.50 แก้ไขเล็กน้อย
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

#Stack    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[self.size()-1]

    def size(self):
        return len(self.items)
#Postfix 
    # สร้างเพื่อจะนำไปทำเป็น Tree 
    def convertPost(self):
        equa = self.putInList(self.equa)

        print(equa)
        alphabet = ['0', '1', 'I1', 'I2','I3']
        priority = {'+':1, '&':1, '!':1, '(':0}
        postfix = ''
        for ch in equa:
            if ch in alphabet :
                postfix += ch
            elif ch in '!+&':
                if self.isEmpty():
                    self.push(ch)
                if not self.isEmpty() and priority[ch] <= priority[self.peek()]:
                    postfix += self.pop()
                self.push(ch)
            elif ch == '(':
                self.push(ch)
            elif ch == ')':
                postfix += self.pop()
                while not(self.isEmpty) and self.peek() != "(":
                    postfix += self.pop()
                    
                self.pop()

        while not(self.isEmpty):
            postfix += self.pop()

        # แบ่งรูปแบบ postfix ให้แต่ละสมาชิกอยู่คนละ index 
        result = self.putInList(postfix)
        print(result)
        for token in range(len(result)):
            if len(result[token]) == 4:

                a = result[token][:2]
                b = result[token][2:]
                del result[token]

                result.insert(token, a)
                result.insert(token+1, b)

            elif result[token] == '01' or result[token] == '10':

                a = result[token][:1]
                b = result[token][1:]
                del result[token]
                result.insert(token, a)
                result.insert(token+1, b)
                
        return result
        
eq1 = boolExpStr("(I0&I1 + !(I1&I2))")
eq2 = boolExpStr("!(1+0)")
eq3 = boolExpStr("!(!(0+I0&1))")
eq4 = boolExpStr("(I0+!I1+!(I2))&(!I0+I1+I2)") # มีวงเล็บโผล่มา
eq5 = boolExpStr("!(I0&I1)+!(I1+I2)")
eq6 = boolExpStr("(((I0&I1&!I2)+!I1)+I3)")

print(eq6.convertPost())

