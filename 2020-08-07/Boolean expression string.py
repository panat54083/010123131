# 6201012610052 Assingment สำหรับ Boolean expression string ในข้อที่ 1
# PyGame version: 1.9.6
#--------------------------Complete----------------------------
# 17.50 07/08/2020 แก้ไขเล็กน้อย
# 01.55 08/08/2020 แก้ไขการแปลงเป็น postfix
# 16.56 08/08/2020 เพิ่ม expression tree และแก้ไข postfix
# 1.56 09/08/2020 แก้ไขการแปลง postfix และ เพิ่มการวาด pygame ปัญหาที่พบเจอ(ยังแก้ไม่ได้) ตัวอักษรกระพริบ และ ขนาดการสร้างวงกลมให้เข้ากับรุปแบบสมการไม่ดีอย่างที่ควร
# 5.00 09/08/2020 แก้ไขการจัดตำแหน่งในการวาด  Tree (ยังไม่สามารถแก้ปัญหาตัวอักษรกระพริบได้
# 13.07 12/08/2020 update version pygame แก้ไขให้โค้ดสามารถเช้ากับ version pygame 1.9.6 (ก่อนหน้าเป็น 2.0.0 dev10)
# 1.31 13/08/2020 แก้ไขอักษรกระพริบ

import pygame
import math
class boolExpStr():
    
    def __init__(self, equation = None):
        self.equa = equation.replace(" ","")

    def findVariable(self):
        lista = list()
        for ela in self.putInList(self.equa):
            if ela in ['I0', 'I1', 'I2', '0', '1']:
                lista.append(ela)

        return list(set(lista))

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
        priority = {'+':1, '&':1, '!':2, '(':0}
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
#data   
    def dataOfEquation(self):
        #==================================
        print('-------------------------------------------')
        word1 = ''
        word2 = ''
        for n in self.putInList(self.equa):
            word1 += n  + ' '
        print('Origin = ',word1)
        for n in self.convertPost():
            word2 += n + ' '
        print('Postfix = ',word2)
        # print(self.convertPost())
        #==================================
        print('-------------------------------------------')
        return None      

#--------------------------------------------------------------------
# ---------------------------PYGAME---------------------------------#
#--------------------------------------------------------------------  

pygame.init()
pygame.display.set_caption('Expression Tree')

clock = pygame.time.Clock()

scr_w, scr_h = 1000, 1000
screen = pygame.display.set_mode((scr_w, scr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA)

#--------------------------------------------------------------------
BLUE = pygame.Color('#7FFFD4')
BLACK = pygame.Color('#000000')
radius = (scr_w**2 + scr_h**2)**(1/2)/40
text_font_for_drawingtree = pygame.font.SysFont("leelawadeeui", int(radius*1.5))
#--------------------------------------------------------------------
class eT():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height(node):  #Ref https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
    if node is None: 
        return 0 ;  
    else : 

        l_height = height(node.left) # ตรวจสอบทางซ้ายไปเรื่อยๆ
        r_height = height(node.right) # ตรวจสอบทางขวาไปเรื่อยๆ
  
        # find which one larger
        if (l_height > r_height): 
            return l_height+1
        else: 
            return r_height+1

def inorder(t): 
	if t is not None: 
		inorder(t.left) 
		print(t.value,end ='')
		inorder(t.right)

def expressionTree(equation):        
    stack = []
    for ch in equation:

        if ch not in '&+!': # operand
            t = eT(ch)
            stack.append(t)

        elif ch == '!':
            t = eT(ch)
            t1 = stack.pop()
            t.right = t1
            stack.append(t)

        else: # operator 
            # ดึงเอาตัวอักษร
            t = eT(ch)
            t1 = stack.pop()
            t2 = stack.pop()
            # put in right and left
            t.right = t1
            t.left = t2


            stack.append(t)

    t = stack.pop()          

    return t      
def drawTree(node, x, y, dx, h): #ref https://gist.github.com/Liwink/b81e726ad89df8b0754a3a1d0c40d0b4
    if node is not None:

        pygame.draw.circle(surface, BLUE, (int(x), int(y)), int(radius))
        pygame.display.update()
        #วาดเส้นเชื่อม
        
        if node.left is not None:
            pygame.draw.line(surface,BLUE ,[int(x),int(y)],[int(x-dx),int(y+1/h*400)],2)
        if node.right is not None:
            pygame.draw.line(surface,BLUE ,[int(x),int(y)],[int(x+dx),int(y+1/h*400)],2)
        

        # วาด ฝั่งทางซ้าย และ ทางขวา 
        drawTree(node.left, x-dx, y+1/h*400, dx/2, h)
        drawTree(node.right, x+dx, y+1/h*400, dx/2, h)
    
def drawText(node, x, y, dx, h):
    if node :
        text_surface = text_font_for_drawingtree.render(str(node.value), True , BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (int(x), int(y))
        surface.blit(text_surface, (text_rect))
        pygame.display.update()

        drawText(node.left, x-dx, y+1/h*400, dx/2, h)
        drawText(node.right, x+dx, y+1/h*400, dx/2, h)

#--------------------------------------------------------------------
# Test
#--------------------------------------------------------------------        
eq1 = boolExpStr("(I0&I1 + !(I1&I2))")
eq2 = boolExpStr("!(1+0)")
eq3 = boolExpStr("!(!(0+I0&1))")
eq4 = boolExpStr("(I0+!I1+!(I2))&(!I0+I1+I2)")
eq5 = boolExpStr("!(I0&I1)+!(I1+I2)")
eq6 = boolExpStr("(((I0&I1&!I2)+!I1)+I3)")

#--------------------------------------------------------------------
#ไว้ตรวจสอบรูปแบบของ Postfix
data = eq1.dataOfEquation()

# เปลี่ยน สมการ ได้ eq1-eq6
anyeq = eq1.convertPost()
node = expressionTree(anyeq)
print('height of nodes is ',height(node))
variable  = eq1.findVariable()
print(eq1.findVariable())
# inorder(node)
#--------------------------------------------------------------------
running = True
fps = 60
h = height(node)
#--------------------------------------------------------------------

drawTree(node, scr_w//2, (scr_h-100)//h, scr_w//math.log(h*15) ,h)
      
def drawExpression():
    global running

    while running:
        
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(screen, "screenshot.jpeg")
                running = False

        # node จุดแกน x จุดแกน y ตัวแปรเปลี่ยนแกน ความสูง
            # pygame.display.update()
        
        drawText(node, int(scr_w//2), int((scr_h-100)//h), int(scr_w//math.log(h*15)) ,int(h))  
        
        screen.fill((255, 255, 255))
        screen.blit(surface, (0, 0))
        pygame.display.update()

    pygame.quit()

drawExpression()
