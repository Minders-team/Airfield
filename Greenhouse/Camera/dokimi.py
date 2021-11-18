#/usr/bin/env python
# coding: utf-8

import pygame
import pygame.camera
from pygame.locals import *
import time

pygame.init()
pygame.camera.init()


class Capture(object):
    def __init__(self):
        import os
        os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
        self.size = (800,600)
        # create a display surface. standard pygame stuff
        self.display = pygame.display.set_mode(self.size, 0)

        # this is the same as what we saw before
        self.clist = pygame.camera.list_cameras()
        
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        
        for camera in self.clist:
            try:
                self.cam = pygame.camera.Camera(camera, self.size)
                self.cam.start()
                break
            except:
                print('Camera %s failed, trying next.' % camera)
        

        # create a surface to capture to.  for performance purposes
        # bit depth is the same as that of the display surface.
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)
        self.clock = pygame.time.Clock()

    def get_and_flip(self):
        # if you don't want to tie the framerate to the camera, you can check
        # if the camera has an image ready.  note that while this works
        # on most cameras, some will never return true.
        if self.cam.query_image():
            self.snapshot = self.cam.get_image(self.snapshot)

        # blit it to the display surface.  simple!
        self.display.blit(self.snapshot, (0,0))
        pygame.display.flip()

    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                    # close the camera safely
                    self.cam.stop()
                    going = False
                    print('Stopping')
                    return

            self.get_and_flip()
            self.clock.tick(10)

if __name__ == '__main__':
    try:
        camera = Capture()
        camera.main()
    except Exception as e:
        print(e)
        pass
    
    pygame.display.quit()
    pygame.quit()