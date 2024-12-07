import os
from PIL import Image, ImageOps

directory_path_origin = "./datasets/coco128/images/train2017"
directory_path_end = "./grayscale"

for img in os.listdir(directory_path_origin):
    img_path = os.path.join(directory_path_origin, img)
    pil_img = Image.open(img_path)
    pil_gs = ImageOps.grayscale(pil_img)
    pil_gs.save(os.path.join(directory_path_end, img), 'JPEG')