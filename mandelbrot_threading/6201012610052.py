#6201012610052
import threading
import time
import cmath
import pygame
#---------------------------------------------------------------
pygame.init()

scr_w = 1000
scr_h = 1000
screen = pygame.display.set_mode( (scr_w, scr_h) )

pygame.display.set_caption('Mandelbrot')

clock = pygame.time.Clock()

surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
#---------------------------------------------------------------

drawingX = 2 #number of picture x-aixs
drawingY = 2 #number of picture y-aixs

#---------------------------------------------------------------

mandelCreate = True
running = True
stop_thread = False

#---------------------------------------------------------------

listArea = list()

x_pos = 0
y_pos = 0
N = drawingX*drawingY
num = 0


lock = threading.Lock()
list_threads = []

#---------------------------------------------------------------
#find position of each area
class dataArea():
    def __init__(self):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

    def __str__(self):
        return str(self.x1, self.y1, self.x2, self.y2)

#---------------------------------------------------------------
# save data of area # Ref. https://stackoverflow.com/questions/55319181/how-to-scroll-the-background-surface-in-pygame
for y in range(drawingY):
    for x in range(drawingX):
        a = "drawArea"+str(num)
        listArea.append(a)   
        listArea[num] = dataArea()
        listArea[num].x1 = x_pos
        listArea[num].y1 = y_pos
        listArea[num].x2 = int(x_pos + scr_w / drawingX)
        listArea[num].y2 = int(y_pos + scr_h / drawingY)

        num += 1
        x_pos += scr_w / drawingX


    y_pos += scr_h / drawingY
    x_pos = 0 
#---------------------------------------------------------------

def mandelbrot(c,max_iters=100):
    i = 0
    z = complex(0,0)
    while abs(z) <= 2 and i < max_iters:
        z = z*z + c
        i += 1 
    return i

#---------------------------------------------------------------

def drawing(x1, y1, x2, y2):
    global mandelCreate
    
    # x1 = area.x1
    # y1 = area.y1
    # x2 = area.x2
    # y2 = area.y2
    while not stop_thread:
        if mandelCreate:
            mandelCreate = False
            scale = 0.006
            offset = complex(-0.55,0.0)
            w2, h2 = (x2-x1)/2, (y2-y1)/2
            for x in range(x1, x2):
                for y in range(y1, y2):
                    re = scale*(x-w2) + offset.real
                    im = scale*(y-h2) + offset.imag
                    c = complex( re, im )
                    color = mandelbrot(c, 63)
                    r = (color << 6) & 0xc0
                    g = (color << 4) & 0xc0
                    b = (color << 2) & 0xc0
                    surface.set_at( (x, y), (255-r,255-g,255-b) )
        with lock:
            screen.blit( surface, (round(x1),round(y1) ))
        pygame.display.update()
    # pygame.time.delay(5)

#---------------------------------------------------------------

for i in range(N):

    t = threading.Thread(target = drawing, args = (listArea[i].x1,listArea[i].y1,listArea[i].x2,listArea[i].y2))
    list_threads.append(t)
#---------------------------------------------------------------

for t in list_threads:
    t.start()
#---------------------------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # drawing(listArea)

    # screen.blit( surface, (0,0) )
    # pygame.display.update()
#---------------------------------------------------------------

clock.tick(30)

stop_thread = True    
pygame.quit()
print( 'PyGame done...')

# Ref. https://stackoverflow.com/questions/55319181/how-to-scroll-the-background-surface-in-pygame
