# **Object Detection Project**

A robust object detection model trained to identify team members faces with YOLOv5.


## **Setup**
For running the model without training you can use the below commands to setup

If you are not in the FacialRecognition directory, please do so:
```bash
cd FacialRecognition
```

Next we need to download the higher version model we used to train

# AI Model
```bash 
git clone https://github.com/ultralytics/yolov5  # clone
```

## **How to Run Detection**
Run the detection script to detect objects in images, videos, or streams.

## **Usage**
If you want to run a custom detection script on a provided video, use:
```bash
python customTest.py
```
If you want to run only on an image/s, run:
```bash 
python customSimple.py
```

To see the results of these scripts, take note of where the outputs are saved as mentioned when ran. These outputs are photos, so you may need another way of viewing them.

These scripts can be customized for specific requirements or workflows.

---

Here are the command line commands that were used in making these scripts:

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

## **Model Information**
### **Weights**
- **Large**: Best for high accuracy but slower inference.
- **Medium**: Balanced trade-off between speed and accuracy.
- **Small**: Fast inference with lower accuracy.

Ensure the corresponding weights files are available in the `[Large, Medium, Small]/weights/` directory.

---