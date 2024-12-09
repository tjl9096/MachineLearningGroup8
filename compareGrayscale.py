#################################################
# Machine Learning
# Final Group Poject
# 
# This file will compare the original versus the grayscale
# version of the coco128 dataset
#################################################

from ultralytics import YOLO

# load the models to train on
base_model = YOLO("yolov5s.pt")
grayscale_model = YOLO("yolov5s.pt")

# train each of the models on the corresponding data
# base_results = base_model.train(data="coco128.yaml", epochs=5, imgsz=640)
grayscale_results = grayscale_model.train(data="grayscale.yaml", epochs=5, imgsz=640)