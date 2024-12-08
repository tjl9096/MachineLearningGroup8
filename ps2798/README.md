# **Object Detection Project**

A robust object detection model trained to identify team members faces with YOLOv5.

---

## **Setup**
To get started, clone the repository and install the required dependencies:
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

This script can be customized for specific requirements or workflows.


## **Model Information**
### **Weights**
- **Large**: Best for high accuracy but slower inference.
- **Medium**: Balanced trade-off between speed and accuracy.
- **Small**: Fast inference with lower accuracy.

Ensure the corresponding weights files are available in the `[Large, Medium, Small]/weights/` directory.


## **Notes**
- Make sure your input images/videos are accessible and correctly specified in the `--source` argument.
- Adjust the confidence threshold (`--conf`) for more or fewer detections.

---
