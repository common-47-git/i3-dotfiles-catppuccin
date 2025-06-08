import cv2
import os

walls_path = "/home/andrew/Pictures/wallpapers/"

for filename in os.listdir(walls_path):
    file_path = os.path.join(walls_path, filename)
    
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        im = cv2.imread(file_path)

        if im is not None:
            print(f"{filename}: {im.shape}")
        else:
            print(f"{filename}: Error.")
