from time import sleep
import os
from picamera import PiCamera


class Camera(object):
    def __init__(self):
        self.cam = PiCamera()
        self.cam.resolution = (1024, 768)
        self.path = 0

    def capture(self, name):
        """
        Toma una foto
        :param name: nombre para la foto
        """

        sleep(1)
        self.path = os.getcwd() + "/" + name
        print(self.path)
        self.cam.capture(self.path)
