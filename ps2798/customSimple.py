from ultralytics import yolov5

model = yolov5('custom', path='runs/train/exp5/weights/best.pt')

result = model('data/images')