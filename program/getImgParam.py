import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import glob
import os
import sys
from moviepy.editor import VideoFileClip

img = mpimg.imread("test_images/test5.jpg")
plt.imshow(img)
plt.show()
