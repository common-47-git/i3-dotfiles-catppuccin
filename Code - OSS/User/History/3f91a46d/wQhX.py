import cv2

im = cv2.imread('~/Pictures')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
print(type(im.shape))