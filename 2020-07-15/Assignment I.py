#6201012610052 เป็นโค้ดสำหรับ Assignment I

import pygame
import random, math

pygame.init()
scr_w, scr_h = 800, 600
screen = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption("Assignment I")
# create a new surface
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
# random Colour

def rgb():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    rgb1 = (red, green, blue)
    return rgb1
clock = pygame.time.Clock()

radius = random.randint(10, 20)
num_cir = 0
num_cre = 0
white = (255, 255, 255)
# --Circles--
class circle():
    def __init__(self):
        self.x = random.randint(radius, scr_w)
        self.y = random.randint(radius, scr_h)
        self.r = random.randint(10, 20)
        self.colour = rgb()

    def new(self):
        pygame.draw.circle(surface,self.colour, (self.x, self.y), self.r)
    


def largest(tar, lista): 
    c = 0
    for k in lista:
        if tar != k:
            if tar.r > k.r or tar.r == k.r :
                c+=1
    if c == len(lista) - 1:
        return True
    


c = []
d_c = []
cre_num = 0 
num = 0 # count circles
cir_num = 10 # number of circles

# In Game    
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # mouse        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            
            for i in d_c:
                
                sqx = (mx - i.x)**2
                sqy = (my - i.y)**2
                
                if math.sqrt(sqx +sqy) < i.r:
                    if largest(i, d_c):
                        pygame.draw.circle(surface,white, (i.x, i.y), i.r)
                        d_c.remove(i)
                        pygame.display.update()
                    # pygame.draw.circle(surface,white, (i.x, i.y), i.r)
                    # d_c.remove(i)
                    # pygame.display.update()

    clock.tick( 10 )
    
    
    
    c.append('c' + str(cre_num)) # 
    c[cre_num] = circle()
        
    shouldprint = True
    #---------------------------------------------- # for infinity circles
    for j in range(len(c)):
        if cre_num != j:
            dist = int(math.hypot(c[cre_num].x - c[j].x, c[cre_num].y - c[j].y))
            if dist < int((c[cre_num].r)+c[j].r):
                shouldprint = False
    if shouldprint:
        c[cre_num].new() # create circle non-overlapping
        d_c.append(c[cre_num])
        
    cre_num += 1

    #---------------------------------------------- for spacific number of circles
    # if num != cir_num:
    #     for j in range(len(c)):
    #         if cre_num != j:
    #             dist = int(math.hypot(c[cre_num].x - c[j].x, c[cre_num].y - c[j].y))
    #             if dist < int((c[cre_num].r)+c[j].r):
    #                 shouldprint = False
    #     if shouldprint:
    #         c[cre_num].new() # create circle non-overlapping
    #         d_c.append(c[cre_num])
    #         num += 1
    #     cre_num += 1
    #-----------------------------------------------       
    

        
        
    screen.fill((255, 255, 255))
    screen.blit(surface, (0, 0))
    pygame.display.update()


pygame.quit()


# ref https://stackoverflow.com/questions/46702987/python-pygame-randomly-draw-non-overlapping-circles
# https://stackoverflow.com/questions/29833035/how-do-i-check-to-see-if-a-mouse-click-is-within-a-circle-in-pygame
