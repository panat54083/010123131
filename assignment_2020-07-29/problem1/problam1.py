###################################################################
#6201012610052 งาน problem 1
###################################################################
import pygame
import pygame.camera
from pygame.locals import *
import sys


def open_camera( frame_size=(640,480),mode='RGB'):
    pygame.camera.init()
    list_cameras = pygame.camera.list_cameras()
    print( 'Mumber of cameras found: ', len(list_cameras) )
    if list_cameras:
        # use the first camera found
        camera = pygame.camera.Camera(list_cameras[0], frame_size, mode )
        return camera 
    return None 

class rect_data():
    def __init__(self):
        self.firstx = None
        self.firsty = None
        self.secx = None
        self.secy = None
        self.rpw = None
        self.rph = None
        self.m = None
        self.n = None
        self.rect = None

# scr_w, scr_h = 640, 480
pygame.init()
clock = pygame.time.Clock()
camera = open_camera()
if camera:
    camera.start()
else:
    print('Cannot open camera')
    sys.exit(-1)

#-------------------------------------------------------------------------------------------
listRectData = list()
numRect = 0
M,N = 10, 8
fps = 30
x_pos = 0
y_pos = 0

listRemove = list()
#-------------------------------------------------------------------------------------------
img = None
is_running = True
while is_running:
                    
    # try to capture the next image from the camera 
    img = camera.get_image()
    if img is None:
        continue

    # get the image size
    img_rect = img.get_rect()
    img_w, img_h = img_rect.w, img_rect.h
    
    screen = pygame.display.set_mode((img_w, img_h))

    surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )
    # print(img_w, img_h)
    # draw (MxN) tiles of the images
    scr_w, scr_h = img_w, img_h
    
    rw, rh = scr_w//M, scr_h//N

    for i in range(N):
        for j in range(M):
            # draw a green frame (tile) and fill black colour
            # save data of rect

            nameRect = 'Rect'+str(numRect + 1)
            listRectData.append(nameRect)

            listRectData[numRect] = rect_data()
            listRectData[numRect].firstx = x_pos
            listRectData[numRect].firsty = y_pos
            listRectData[numRect].secx = int(x_pos + scr_w/M)
            listRectData[numRect].secy = int(y_pos + scr_h/N)
            rpw = j*rw
            rph = i*rh

            listRectData[numRect].rpw = rpw
            listRectData[numRect].rph = rph
            # rect = (x_pos, y_pos, rw, rh)
            rect = (j*rw, i*rh, rw, rh)
            listRectData[numRect].rect = rect


            numRect += 1
            x_pos += scr_w / M
        y_pos += scr_h / N
        x_pos = 0

    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            is_running = False
            if img:
                # save the current image into the output file
                pygame.image.save( img, 'image.jpg' )
        elif e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            for data in listRectData:
                if data.firstx <= mx <= data.secx and data.firsty <= my <= data.secy:
                    print("EIEI")               
                    listRemove.append(data)

    for own in listRectData:
        pygame.draw.rect( surface, (0,255,0), own.rect,1)

        # surface.blit( surface ,own.rect, own.rect)
    for orther in listRemove:
        surface.blit( img, orther.rect, orther.rect)      
            
    # write the surface to the screen and update the display
    
    screen.blit( surface, (0,0) )
    # screen.fill((255, 255, 255))
    pygame.display.update()
    clock.tick(fps)
# close the camera
camera.stop()

print('Done....')
###################################################################
