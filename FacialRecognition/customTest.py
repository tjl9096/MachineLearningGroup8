#################################################
# Machine Learning
# Final Group Project
# 
# This file will run face recognition on the trained faces
# of a custom dataset on video files
#################################################

import torch
import cv2
import pathlib
from tqdm import tqdm  # For progress bar

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='Large/weights/best.pt')

# Load video source
video_path = "./IMG_3725.MOV"  # Replace with 0 for webcam
is_webcam = video_path == 0
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) if not is_webcam else None
print(f"Video Properties: Width={frame_width}, Height={frame_height}, FPS={fps}, Total Frames={total_frames}")

# VideoWriter for output
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (frame_width, frame_height))

# Progress bar setup for non-webcam sources
progress_bar = tqdm(total=total_frames, desc="Processing Video", unit="frame") if not is_webcam else None

# Process frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No more frames or error reading video.")
        break

    # Resize frame to 640x640 for YOLO model
    resized_frame = cv2.resize(frame, (640, 640))

    # Inference
    results = model(resized_frame)

    # Render results
    rendered_frames = results.render()
    rendered_frame = rendered_frames[0]

    # Resize rendered frame back to original size for saving
    original_size_rendered_frame = cv2.resize(rendered_frame, (frame_width, frame_height))

    # Write the rendered frame to the output video
    out.write(original_size_rendered_frame)

    # Display the frame if using a webcam
    if is_webcam:
        cv2.imshow('YOLOv5 Detection', original_size_rendered_frame)

        # Break on 'q' key press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        # Update progress bar for video file
        progress_bar.update(1)

# Clean up resources
cap.release()
out.release()
if progress_bar:
    progress_bar.close()
cv2.destroyAllWindows()

print("Processing complete. Output saved to 'output.avi'.")
