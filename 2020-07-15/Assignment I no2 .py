# 6201012610052 Assingment I
# update feture 'No spawn in broder'
import pygame
import random, math

pygame.init()

scr_w, scr_h = 800, 600


screen = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption("Assignment I")

# create a new surface
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
# random Colour
clock = pygame.time.Clock()


def rgb():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    rgb1 = (red, green, blue)
    return rgb1

white = (255, 255, 255)

min_radius = 10
max_radius = 20

c = []
nonOverCir = []
cre_num = 0 
countCir = 0 # count circles
numOfCircles = 10 # number of circles

num_cir = 0
num_cre = 0
fps = 60

# --Circles--
class circle():
    def __init__(self):
        self.r = random.randint(min_radius, max_radius)
        self.x = random.randint(self.r, scr_w-self.r)
        self.y = random.randint(self.r, scr_h-self.r)
        
        self.random = random.choice([-1, 1])
        
        self.colour = rgb()
        # self.colour = (0,0,0)

    def createCir(self):
        # For circle is not in border
        proof = []
        # find circumference
        for rad in range(0,91):
            
            sine = math.sin(math.radians(rad))
            cose = math.cos(math.radians(rad))
            
            rcose = (self.r * cose) + self.x
            rsine = (self.r * sine) + self.y
            

            # find circumference
            if 0 < rcose <= scr_w and 0 < rsine <= scr_h:
                proof.append(True)
            else:
                proof.append(False)

        # print ('rcose +',str(self.x),' = ',str(rcose),' rsine = ', str(rsine))
        
        if all(proof):
            pygame.draw.circle(surface,self.colour, (self.x, self.y), self.r)



        
        pygame.draw.circle(surface,self.colour, (self.x, self.y), self.r)
    
    def orderRadius(self):
        return self.r
    
    def __str__(self):
        return str(self.r)


def largest(tar, lista): 
    c = 0
    for k in lista:
        if tar != k:
            if tar.r > k.r or tar.r == k.r :
                c+=1
    if c == len(lista) - 1:
        return True
    # else:
    #     return False
    




# In Game    
run = True
while run:
    clock.tick( fps )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # mouse        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            
            for i in nonOverCir:
                
                sqx = (mx - i.x)**2
                sqy = (my - i.y)**2
                
                if math.sqrt(sqx +sqy) < i.r:
                    if largest(i, nonOverCir):
                        
                        i.colour = white
                        i.createCir()

                        nonOverCir.remove(i)
                        
                        pygame.display.update()
                        
                   


    
    
    
    
    c.append('c' + str(cre_num)) # 
    c[cre_num] = circle()
        
    shouldprint = True
    #---------------------------------------------- # for infinity circles
    # for j in range(len(c)):
    #     if cre_num != j:
    #         dist = int(math.hypot(c[cre_num].x - c[j].x, c[cre_num].y - c[j].y))
    #         if dist < int((c[cre_num].r)+c[j].r) and c[cre_num].r:
    #             shouldprint = False
    # if shouldprint:
    #     c[cre_num].createCir() # create circle non-overlapping
    #     nonOverCir.append(c[cre_num])
    #     nonOverCir.sort(reverse = True, key=circle.orderRadius)
    #   
    # cre_num += 1

    #---------------------------------------------- for spacific number of circles
    if countCir != numOfCircles:
        for j in range(len(c)):
            if cre_num != j:
                dist = int(math.hypot(c[cre_num].x - c[j].x, c[cre_num].y - c[j].y))
                if dist < int(((c[cre_num].r)+c[j].r)) :
                    shouldprint = False
        
        if shouldprint:
            c[cre_num].createCir() # create circle non-overlapping

            nonOverCir.append(c[cre_num])
            nonOverCir.sort(reverse = True, key=circle.orderRadius) 

            countCir += 1
        cre_num += 1
        
    
    # #-----------------------------------------------       


    screen.fill(white)
    screen.blit(surface, (0, 0))
    pygame.display.update()


pygame.quit()

# cheack sort in list

for i1 in range(len(nonOverCir)):
    print(i1+1, nonOverCir[i1])

# ref https://stackoverflow.com/questions/46702987/python-pygame-randomly-draw-non-overlapping-circles
# https://stackoverflow.com/questions/29833035/how-do-i-check-to-see-if-a-mouse-click-is-within-a-circle-in-pygame
