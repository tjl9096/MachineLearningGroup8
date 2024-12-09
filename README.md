# MachineLearningGroup8
Final Group Project for Intro to Machine Learning

Tyler Lapiana
Anindhya Kushagra
Rushil Patel
Prateek Sharma

INSTRUCTIONS:
First, our project requires the use of a GPU.

When cloning the repository, please run the command: "git clone --recurse-submodules https://github.com/tjl9096/MachineLearningGroup8"

If you have already cloned the repository but did not clone the submodules, you can run: "git submodule update --init --recursive"

You can check that the submodule has successfully been obtained if the "yolov3" directory is not empty. 

Next, you will need to download the requirements. First, ensure you are in the FinalGroupPoject directory. Then, please run: 
```bash 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -r yolov3/requirements.txt
```
One of our propsed changes does the model training on the coco128 dataset by converting images to grayscale for better detection of grayscale images

Now, you should be able to run our test file compareGrayscale.py

---

Then there is a custom Dataset that we trained model yolov5 on our Faces for recognition purposes. For more details refer to [Custom Dataset](FacialRecognition/README.md)
