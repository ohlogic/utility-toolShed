#!/usr/bin/python3

import sys
import numpy as np
import imageio
from skimage import img_as_ubyte
#import matplotlib.pyplot as plt
import warnings
import time


frame_times = []
FPS = 0
start_t = time.time()
fullscreen = True


try:
  from OpenGL.GLUT import *
  from OpenGL.GL import *
  from OpenGL.GLU import *
except:
  print ('''
ERROR: PyOpenGL not installed properly.
        ''')
  sys.exit()



def drawText( value, x,y,  windowHeight, windowWidth, step = 18 ):
    """Draw the given text at given 2D position in window
    """
    glMatrixMode(GL_PROJECTION)
    # For some reason the GL_PROJECTION_MATRIX is overflowing with a single push!
    # glPushMatrix()
    matrix = glGetDouble( GL_PROJECTION_MATRIX )
    
    glLoadIdentity()
    glOrtho(0.0, windowHeight or 32, 0.0, windowWidth or 32, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    glRasterPos2i(x, y)
    lines = 0
    for character in value:
        if character == '\n':
            glRasterPos2i(x, y-(lines*18))
        else:
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(character))
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    # For some reason the GL_PROJECTION_MATRIX is overflowing with a single push!
    # glPopMatrix()
    glLoadMatrixd( matrix ) # should have un-decorated alias for this...
    
    glMatrixMode(GL_MODELVIEW)



class GLRenderShape:
    def Triangle(self):
        glBegin(GL_TRIANGLES)
        glColor3f(0., 1., 1.)
        glVertex3f(-1, -1, 0.)
        glColor3f(1., 0., 1.)
        glVertex3f(1., -1., 0.)
        glColor3f(1., 1., 1.)
        glVertex3f(0, 1, 0.)
        glEnd()


class Scene:

    def __init__(self):
        self.quadric = gluNewQuadric()
        self.render_shapes = GLRenderShape()
        self.init()
        self.eye = [0.25, .25, -100]
        self.center = [0.2, -.3, 0]
        self.up = [0, 1, 0]


    def display(self):
        global FPS
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(45, 0., 0. , 1.)
        glScalef(0.5, 0.5, 0.5)
        self.render_shapes.Triangle()
        glPopMatrix()

        glPushAttrib(GL_COLOR_BUFFER_BIT)
        glColor3f(0.4, 0.2, 0.2)
        glPushMatrix()
        glTranslatef(0, .25, 0)
        glutSolidTeapot(0.25)
        glPopMatrix()
        glPopAttrib()

        glPushMatrix()
        glColor3f(1., 0., 0.)
        glTranslatef(-.5, -.5, -1)
        gluSphere(self.quadric, 0.5, 32, 32)
        glPopMatrix()


        glColor3f(1., 1., 1.) # text color
        text = str( 'FPS: ' + str(FPS)  )
        drawText( text, 12,95,       0, 100 )
        
        glutSwapBuffers()

        #glFlush()



    def reshape(self, width, height):
        self.width = width
        self.height = height
        glViewport(0, 0, self.width, self.height)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def keyboard(self, key, x, y ):
        global fullscreen
    
        print ('key:' , key)
        if key == b'\x1b': # ESC
            sys.exit()
        elif key == b's' or key == b'S':
            filename = 'a1.png'
            print('saving screen shot to %s' % filename)
            glReadBuffer(GL_FRONT)
            im = glReadPixels(0, 0, self.width, self.height, 
                                   GL_RGBA, GL_UNSIGNED_INT)
            imageio.imwrite('a1.png', np.flipud(np.uint8(im)))
            
            im_depth = glReadPixels(0, 0, self.width, self.height, GL_DEPTH_COMPONENT, GL_FLOAT)

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                im_depth = img_as_ubyte(np.flipud(im_depth))
                        
            imageio.imwrite('filename.jpg', im_depth)
                   
            #import matplotlib.pyplot as plt
            #plt.imshow(np.flipud(im_depth))
            #plt.show()                   
        elif key == b'r' or key == b'R': # manual rotate
            glRotatef(1, 0, 1, 0)
            glutPostRedisplay()
            
        elif key == b'f' or key == b'F': #fullscreen toggle
        
            if (fullscreen == True):
                glutReshapeWindow(512, 512)
                glutPositionWindow(int((1360/2)-(512/2)), int((768/2)-(512/2)))
                fullscreen = False
            else:
                glutFullScreen()
                fullscreen = True
                
        print('done')

    def mouse(self, button, state, x, y):
        print(button, state, x, y)

    def motion(self, x, y):
        #print(x, y)
        pass

    def init(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)



def timer(a):
    global start_t
    global frame_times
    global FPS
    
    glRotatef(1, 0, 1, 0)
    glutPostRedisplay()
    
    end_t = time.time()
    time_taken = end_t - start_t
    start_t = end_t
    frame_times.append(time_taken)
    frame_times = frame_times[-20:]
    FPS = len(frame_times) / sum(frame_times)


    glutTimerFunc(  int(1/60), timer, 0)
    
    time.sleep(1/60.0) #VERY simplistically run the app at ~60 fps, avoids high CPU usage!



if __name__ == '__main__':
    start = time.time()

    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    w1 = glutCreateWindow('COMP557 Sample')
    glutInitWindowPosition(int((1360/2)-(512/2)), int((768/2)-(512/2)))

    fullscreen = False
    #glutFullScreen()
    
    scene = Scene()
    glutReshapeFunc(scene.reshape)
    glutDisplayFunc(scene.display)
    glutKeyboardFunc(scene.keyboard)
    glutMouseFunc(scene.mouse)
    glutMotionFunc(scene.motion)
    
    # glutEntryFunc(print( 'Entry' ))
    # glutKeyboardUpFunc( print( 'KeyboardUp' ))
    # glutPassiveMotionFunc( print( 'PassiveMotion' ))
    # glutVisibilityFunc( print( 'Visibility' ))
    # glutWindowStatusFunc( print( 'WindowStatus' ))
    # glutSpecialFunc( print( 'Special' ))
    # glutSpecialUpFunc( print( 'SpecialUp' ))
    
    scene.init()
    
    
    time_taken = time.time() - start
    FPS = 1. / time_taken
    
    glutTimerFunc( int(1/60), timer, 0)

    glutMainLoop()

