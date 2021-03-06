# 6201012610052 Assingment สำหรับ Boolean expression string ในข้อที่ 1 และ 2
# PyGame version: 1.9.6
#------------------------Complete----------------------------
# 17.50 07/08/2020 แก้ไขเล็กน้อย
# 01.55 08/08/2020 แก้ไขการแปลงเป็น postfix
# 16.56 08/08/2020 เพิ่ม expression tree และแก้ไข postfix
# 1.56 09/08/2020 แก้ไขการแปลง postfix และ เพิ่มการวาด pygame ปัญหาที่พบเจอ(ยังแก้ไม่ได้) ตัวอักษรกระพริบ และ ขนาดการสร้างวงกลมให้เข้ากับรุปแบบสมการไม่ดีอย่างที่ควร
# 5.00 09/08/2020 แก้ไขการจัดตำแหน่งในการวาด  Tree (ยังไม่สามารถแก้ปัญหาตัวอักษรกระพริบได้
# 13.07 12/08/2020 update version pygame แก้ไขให้โค้ดสามารถเช้ากับ version pygame 1.9.6 (ก่อนหน้าเป็น 2.0.0 dev10)
# 1.31 13/08/2020 แก้ไขอักษรกระพริบ
# 1.53 18/08/2020 เพิ่มการสร้างตาราง หมายเหตุ ยังไม่ได้สรา้งให้สามารถรับบ input จาก .txt และ output ออกไปใน .txt
# 8.11 18/08/2020 เพิ่มการสร้างตารางที่ input เป็น .txt และสร้าง output เข้าไปในไฟล์ .txt ของ input
# 19.56 19/08/2020 ทำการปรับให้ Not operator ให้ child อยู่ตรงกลาง เปลีายนชื่อตัวแปรและฟังชันก์ของโค้ดให้เหมาะสม

import pygame
import math
from itertools import product
class boolExpStr():
    
    def __init__(self, equation = None):
        self.equa = equation.replace(" ","") # ตัดวงเล็บ

    def isOperand(self, ch):
        if ch not in set('+&!()'):
            return True

    # show input
    def str_equation(self): 
        str_equation = ''
        for ch in self.equa:
            str_equation += ch
        return str_equation

    # find variables in equation
    def findVar(self): 
        all_Var = list()
        for ch in self.list_equation(self.equa):
            # if ch in ['I0', 'I1', 'I2','I3']:
            if self.isOperand(ch):
                all_Var.append(ch)
        return sorted(list(set(all_Var)))

    # checkOperator        
    def isOperator(self, ch):
        if ch == '+' or ch == '&' or ch == '!':
            return True
        else:
            return False

    #put equation into list 
    def list_equation(self, equa): 
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

    # make the equation to be postfix for creating expression Tree 
    def convertPost(self):
        equation = self.list_equation(self.equa)
        openC = 0

        for ch in equation: # Check if equation have wrong barcket
            if ch == '(':
                openC += 1
            elif ch == ')':
                openC -= 1
        if openC != 0:
            print("Error equation, pls check barcket")
            if openC > 0:
                return "too '(' "
            elif openC < 0:
                return "too ')' "

        priority = {'+':1, '&':1, '!':2, '(':0}
        postfix = []
        stack = []

        for ch in equation:
            if self.isOperand(ch) :
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

    # Check data of Equation    
    def cheack_dataEqua(self):
        #==================================
        print('------------------------------------------------------------')
        word1 = ''
        word2 = ''
        for ch in self.list_equation(self.equa):
            word1 += ch  + ' '
        print('Origin = ',word1)
        for ch in self.convertPost():
            word2 += ch + ' '
        print('Postfix = ',word2)
        print('Variable are = ', self.findVar())
        #==================================
        print('------------------------------------------------------------')
        return None
    
    def createTable(self):
        print('------------------------------------------------------------')
        var_equation = self.findVar()
        num_var_equation = len(var_equation)
        case_list = []
        fields = []

        # สร้างหัวของตาราง
        for var in var_equation:
            fields.append(var)
        fields.append(self.str_equation()) #str_equation คือสมการ

        inputs = product([int(True), int(False)], repeat = num_var_equation)
        for boolean in inputs:
            case_list.append(list(boolean))
        
        
        for l in range(len(case_list)):
            new_equa = self.str_equation()
            for k in range(num_var_equation):
                new_equa = new_equa.replace(var_equation[k],str(case_list[l][k])) # ทำการเปลี่ยนตัวแปรในสมการให้อยู่ในรูปของ T, F

            # ทำการใช้สมการใหม่ ในการหา คำตอบ
            eachEqua = boolExpStr(new_equa)
            root = expressionTree(eachEqua.convertPost())
            result = evaluateExpressionTree(root)
            case_list[l].append(result) # ใส่คำตอบ

        # สร้างหัวของตาราง
        for f in fields:
            print(f, end = ' | ')
        print('\n')   
        new = ''
        list_ = []
        # สร้างข้อมูล Truth Table 
        for i in range(len(case_list)):
            for j in range(len(case_list[i])):
                lenStr = len(fields[j]) - len(str(int(case_list[i][j])))
                left_lenStr = (lenStr)//2
                right_lenStr = len(fields[j]) - left_lenStr - len(str(int(case_list[i][j])))
                new = ' '*left_lenStr + str(int(case_list[i][j])) + ' '*right_lenStr
                print(new, end = ' | ')
            print('\n')
        print('------------------------------------------------------------')
        return True

#--------------------------------------------------------------------#
#                    PYGAME EXPRESSION TREE                          #
#--------------------------------------------------------------------#

class eT(): # Class for create Node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.center = False
# Create Expression tree (input must be postfix form)
def expressionTree(equation):  
    stack = []
    for ch in equation:

        if ch not in '&+!': # operand
            t = eT(ch)
            stack.append(t)

        elif ch == '!':
            t = eT(ch)
            t1 = stack.pop()
            t.center = True
            t.right = t1
            
            stack.append(t)

        else: # operator 
            # pop operand
            t = eT(ch)
            t1 = stack.pop()
            t2 = stack.pop()
            # put in right and left
            t.right = t1
            t.left = t2

            stack.append(t)
    t = stack.pop()          

    return t

# Find height of Expression Tree
def height(node):  #Ref https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
    if node is None: 
        return 0 ;  
    else : 

        l_height = height(node.left) # Keep checking the left
        r_height = height(node.right) # Keep checking the right
  
        # find which one larger
        if (l_height > r_height): 
            return l_height+1
        else: 
            return r_height+1

# Read in Inorder Form
def inorder(node): 
	if node is not None: 
		inorder(node.left) 
		print(node.value,end ='')
		inorder(node.right)

# Calculate Boolean
def evaluateExpressionTree(root): # root ให้ใส่ expressionTree #Ref https://www.geeksforgeeks.org/evaluation-of-expression-tree/

    if root is None:
        return None
    if root.left is None and root.right is None:
        return root.value

    # evaluate left tree     
    left_eval = evaluateExpressionTree(root.left)
	# evaluate right tree
    right_eval = evaluateExpressionTree(root.right)

    # Determine Logic
    if root.value == '+':
        return left_eval or right_eval
    elif root.value == '&':
        return left_eval and right_eval
    elif root.value == '!':
        return not right_eval

# Drawing in Pygame
# Drawing nodes
def drawTree(node, x, y, dx, h): #ref https://gist.github.com/Liwink/b81e726ad89df8b0754a3a1d0c40d0b4
    if node is not None:
        # Draw nodes
        pygame.draw.circle(surface, BLUE, (int(x), int(y)), int(radius))
        pygame.display.update()

        #Draw line
        if node.left is not None:
            #(x1, y1),(x2, y2)
            pygame.draw.line(surface,BLUE ,[int(x),int(y)],[int(x-dx),int(y+1/h*300)],2)
        if node.right is not None:
            if node.center is not True:
                pygame.draw.line(surface,BLUE ,[int(x),int(y)],[int(x+dx),int(y+1/h*300)],2)
            else:
                pygame.draw.line(surface,BLUE ,[int(x),int(y)],[int(x),int(y+1/h*300)],2)
        # recursive until out of node or node is None
        # Draw the left and right sides.
        drawTree(node.left, x-dx, y+1/h*300, dx/2, h)
        if node.center is not True:
            drawTree(node.right, x+dx, y+1/h*300, dx/2, h)
        else: # กรณีคือ root = Not
            drawTree(node.right, x, y+1/h*300, dx/2, h)

        return True

# Drawing Text
def drawText(node, x, y, dx, h):
    if node :
        # Draw text in each node
        text_surface = text_font_for_drawingtree.render(str(node.value), True , BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (int(x), int(y))

        surface.blit(text_surface, (text_rect))
        pygame.display.update()

        # recursive until out of node or node is None
        # Draw the left and right sides.
        drawText(node.left, x-dx, y+1/h*300, dx/2, h)
        if node.center is not True:
            drawText(node.right, x+dx, y+1/h*300, dx/2, h)
        else:
            drawText(node.right, x, y+1/h*300, dx/2, h)
        return True

# main in Pygame
def drawExpression():
    global running

    while running:
        
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(screen, "screenshot.jpeg")
                running = False
            # press ESC
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.image.save(screen, "screenshot.jpeg")
                    running = False
        
        screen.fill((255, 255, 255))
        screen.blit(text, text_rect_label)
        screen.blit(surface, (0, 0))
        pygame.display.update()
    
    pygame.quit()

#-------------------------------------------------------------------#
#                               Input                               #
#-------------------------------------------------------------------#

# equation
listOfEquation = ["(I0&I1 + !(I1&I2))", "!(1+0)",
                 "!(!(0+I0&1))", "(I0+!I1+!(I2))&(!I0+I1+I2)",
                  "!(I0&I1)+!(I1+I2)", "(((I0&I1&!I2)+!I1)+I3)",
                  "!A+B+C&D"]
# N มี 1-6
# N = 1  >>>  "(I0&I1 + !(I1&I2))"
# N = 2  >>>  "!(1+0)"
# N = 3  >>>  "!(!(0+I0&1))"
# N = 4  >>>  "(I0+!I1+!(I2))&(!I0+I1+I2)"
# N = 5  >>>  "!(I0&I1)+!(I1+I2)"
# N = 6  >>>  "(((I0&I1&!I2)+!I1)+I3)"
# N = 7  >>>  "!A+B+C%D"
 
N = 7
eq = boolExpStr(listOfEquation[N-1])
#--------------------------------------------------------------------
# main Variable
anyeq = eq.convertPost() # Convert infix to postfix
variable  = eq.findVar() # variabel in equation
node = expressionTree(eq.convertPost()) # Create Node from equation

running = True
fps = 60
h = height(node)

#--------------------------------------------------------------------
# Cheack in foramtion of Equation
eq.cheack_dataEqua()
print('height of nodes is ',height(node))

#--------------------------------------------------------------------
# Result of create Table
eq.createTable()

#-------------------------------------------------------------------#
#                               PYGAME                              #
#-------------------------------------------------------------------#
pygame.init()
pygame.display.set_caption('Expression Tree')

clock = pygame.time.Clock()

scr_w, scr_h = 800, 600
screen = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA)

#--------------------------------------------------------------------
BLUE = pygame.Color('#7FFFD4')
BLACK = pygame.Color('#000000')
radius = (scr_w**2 + scr_h**2)**(1/2)/50
text_font_for_drawingtree = pygame.font.SysFont("leelawadeeui", int(radius*1.5))
text_font_for_label = pygame.font.SysFont("comicsansms", int(radius*2))

#--------------------------------------------------------------------
# Label
text = text_font_for_label.render(str(eq.str_equation()), True, BLACK)
text_rect_label = text.get_rect()
text_rect_label.center = (text.get_width()//2,text.get_height()//2)

# x, y are position of picture and  dx is the variable that can change position
# drawTree(node, x, y, dx, h)
drawTree(node, scr_w//2, (scr_h-100)//h, scr_w//math.log(h*15) ,h)
# drawText(node, x, y, dx, h)
drawText(node, int(scr_w//2), int((scr_h-100)//h), int(scr_w//math.log(h*15)) ,int(h))  

#--------------------------------------------------------------------
# draw Expression Tree
drawExpression()

#--------------------------------------------------------------------
class ExpressionInTxt:
    def __init__(self, textName):
        self.textName = textName # รับ input ที่เป็นชื่อ ไฟล์

    def readText(self): # อ่าน บรรทัดแรกเพื่อดึงสมการออกมา
        with open(self.textName, 'r') as file_:
            line = file_.readline()
            print('line = ',line)
            return line


    def writeTable(self): # นำสมการที่ได้ไปทำขั้นตอนการสร้าง table
        with open(self.textName, 'a') as file_:
            if self.readText() == False:
                return False

            else:
                file_.write('\n')
                file_.write('------------------------------------------------------------')
                file_.write('\n')
                file_.write('------------------------Truth Table-------------------------')
                file_.write('\n')
                file_.write('------------------------------------------------------------')
                file_.write('\n')
                
                equation = self.readText() # สมการ
                equation.replace('\n', '')
                input_ = boolExpStr(equation)
                print(equation)
                var_equation = input_.findVar() #ตัวแปรในสมการ
                print(var_equation)
                num_var_equation = len(var_equation) #จำนวนตัวแปร

                case_list = []
                fields = []

                for var in var_equation: # หัวข้อของตาราง
                    fields.append(var)
                fields.append(equation)

                inputs = product([int(True), int(False)], repeat = num_var_equation) # ทำการเก็บค่าแต่ละกรณี
                for boolean in inputs:
                    case_list.append(list(boolean))

                for l in range(len(case_list)):
                    new_equa = equation
                    # print(new_equa)
                    for k in range(num_var_equation):
                        new_equa = new_equa.replace(var_equation[k],str(case_list[l][k])) # ทำการเปลี่ยนตัวแปรในสมการให้อยู่ในรูปของ T, F
                    # print(case_list[l])
                    # print(new_equa)
                    # ทำการใช้สมการใหม่ ในการหา คำตอบ
                    eachEqua = boolExpStr(new_equa)
                    root = expressionTree(eachEqua.convertPost())
                    result = evaluateExpressionTree(root)
                    case_list[l].append(result) # ใส่คำตอบ
            
                # สร้างหัวของตาราง
                for f in fields:
                    file_.write(f)
                    file_.write(' | ')
                file_.write('\n')   
                new = ''
                list_ = []
                # สร้างข้อมูล Truth Table 
                for i in range(len(case_list)):
                    for j in range(len(case_list[i])):
                        lenStr = len(fields[j]) - len(str(int(case_list[i][j])))
                        left_lenStr = (lenStr)//2
                        right_lenStr = len(fields[j]) - left_lenStr - len(str(int(case_list[i][j])))
                        new = ' '*left_lenStr + str(int(case_list[i][j])) + ' '*right_lenStr
                        file_.write(new)
                        file_.write(' | ')
                    file_.write('\n')
                file_.write('------------------------------------------------------------')
                file_.write('\n')
                print('Writing table is Done')
                return True

#-------------------------------------------------------------------#
#                               Text                                #
#-------------------------------------------------------------------#
# สร้างไฟล์ ที่บรรทัดแรก มีแต่โจทย์ เช่น "(I0 + I1)"
# 'input1.txt'
# 'input2.txt'
# 'input3.txt'
# 'input4.txt'
# 'input5.txt'
# 'input6.txt'

# input_file = ExpressionInTxt('input1.txt')
# input_file.readText()
# input_file.writeTable()
