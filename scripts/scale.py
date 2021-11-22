import numpy as np
import cv2 as cv

# scale.py V1.0

# This scripts takes an svg and converts it to a size that is manageable for
# the robots of MLF

# dimensions are in mm

MIN_X = 20
MAX_X = 300
MIN_Y = 20
MAX_Y = 300

def crop_useles_info(img):
    """
    Takes the full svg and crops the parts that are not the signatur (curve
    to draw)
    :param img: opencv img
    :return: opencv cropped img
    """
    pass

def scale_to_final_size_mm(img, dimesions):
    """
    Converts svg curve to desired drawing size (in mm)
    :param img: opencv img
    :param dimesions: tupple = (width, height) in mm
    :return: opencv cropped img
    """
    WIDTH, HEIGHT = dimesions
    pass


