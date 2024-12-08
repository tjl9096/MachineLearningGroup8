# **Object Detection Project**

A robust object detection model trained to identify team members faces with YOLOv5.

---

## **Setup**
To get started, clone the repository and install the required dependencies:
you need to be in FacialRecognition dir
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## **How to Run Detection**
Run the detection script to detect objects in images, videos, or streams.


## **Usage**
If you want to run a custom detection script, use:
```bash
python customTest.py
```
If you want to run only on inmage/s, update the path in customSimple and run
```bash 
python customSimple.py
```

This script can be customized for specific requirements or workflows.


## **Model Information**
### **Weights**
- **Large**: Best for high accuracy but slower inference.
- **Medium**: Balanced trade-off between speed and accuracy.
- **Small**: Fast inference with lower accuracy.

Ensure the corresponding weights files are available in the `[Large, Medium, Small]/weights/` directory.


---


# Ai Model
```bash 
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt
```

# Training Command
```bash 
CUDA_VISIBLE_DEVICES=8,9 python train.py --img 640 --epochs 300 --data ../custom_dataset.yaml --weights yolov5l.pt
```

# Validation
```bash 
python val.py --data ../custom_dataset.yaml --weights runs/train/exp/weights/best.pt --img 640
```

# detection
```bash
python detect.py --weights path/to/best.pt --img 640 --conf 0.5 --source path/to/images_or_videos
```


## **Notes**
- Make sure your input images/videos are accessible and correctly specified in the `--source` argument.
- Adjust the confidence threshold (`--conf`) for more or fewer detections.

---