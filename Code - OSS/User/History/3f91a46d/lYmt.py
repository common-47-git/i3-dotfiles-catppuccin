import cv2
import os

walls_path = "/home/andrew/Pictures/walls-catppuccin-mocha"

for filename in os.listdir(walls_path):
    file_path = os.path.join(walls_path, filename)
    
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        im = cv2.imread(file_path)

        if im is not None:
            height, width = im.shape[:2]
            aspect_ratio = width / height
            expected_ratio = 16 / 9

            if abs(aspect_ratio - expected_ratio) < 0.01:
                print(f"{filename}: OK ({width}x{height})")
            else:
                print(f"{filename}: NOT 16:9 ({width}x{height}) — deleting")
                os.remove(file_path)
        else:
            print(f"{filename}: Error reading")
