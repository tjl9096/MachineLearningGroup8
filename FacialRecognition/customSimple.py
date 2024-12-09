#################################################
# Machine Learning
# Final Group Poject
# 
# This file will run face recognition on the trained faces
# of custom dataset on images
#################################################

import torch
import pathlib
import os
from pathlib import Path

# Fix pathlib compatibility on Windows
if os.name == 'nt':
    pathlib.PosixPath = pathlib.WindowsPath

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='Small/weights/best.pt')

def classify_images(input_path):
    """
    Classify images from a folder recursively or a single image.
    
    Args:
        input_path (str): Path to the image or folder.
    """
    # Convert input path to a Path object for easier handling
    input_path = Path(input_path)

    # Check if the input path is a directory
    if input_path.is_dir():
        # Recursively find all images in the folder
        image_files = list(input_path.rglob('*.jpg')) + list(input_path.rglob('*.png')) + list(input_path.rglob('*.jpeg'))
        print(f"Found {len(image_files)} image(s) in {input_path}.")
        
        # Process each image
        for image_file in image_files:
            print(f"Processing: {image_file}")
            results = model(str(image_file))
            results.save(save_dir='output/')  # Save results in an 'output' folder
    elif input_path.is_file():
        # Process a single image
        print(f"Processing single image: {input_path}")
        results = model(str(input_path))
        results.save(save_dir='output/')  # Save results in an 'output' folder
        results.show()  # Display the image with detections
    else:
        print("Error: Provided path is neither a valid file nor a directory.")

# Update the path below to classify either a folder or a single image
classify_images('custom_datasets/images/test')
