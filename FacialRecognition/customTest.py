#################################################
# Machine Learning
# Final Group Poject
# 
# This file will run face recognition on the trained faces
# of custom dataset on video files
#################################################


import torch
import cv2
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load the YOLOv5 model
# Change the below path to any of the below 
# 'Small/weights/best.pt'
# 'Medium/weights/best.pt'
# 'Large/weights/best.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path='Large/weights/best.pt')



# Load video source (0 for webcam, or provide a video file path)
video_path = 0  # Replace with the path to the video file or 0 for webcam
cap = cv2.VideoCapture(video_path)

# Check if the video file or webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open video source.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create a VideoWriter object to save output
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width, frame_height))

# Process video frame by frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Break the loop if no frames are returned

    # Perform inference on the current frame
    results = model(frame)

    # Convert results to a format suitable for OpenCV
    rendered_frame = results.render()[0]  # Render results on the frame

    # Write the rendered frame to the output file
    out.write(rendered_frame)

    # Display the frame
    cv2.imshow('YOLOv5 Detection', rendered_frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()