import torch
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model = torch.hub.load('ultralytics/yolov5', 'custom', path='Small/weights/best.pt')

# update the path of image file below
result = model('custom_datasets/images/test/42b4b379-IMAG4443.jpg' )

result.show()