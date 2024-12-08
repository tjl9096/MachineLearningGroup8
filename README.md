# MachineLearningGroup8
Final Group Project for Intro to Machine Learning

Tyler Lapiana
Anindhya Kushagra
Rushil Patel
Prateek Sharma

INSTRUCTIONS:
When cloning the repository, please run the command: "git clone --recurse-submodules https://github.com/tjl9096/MachineLearningGroup8"

If you have already cloned the repository but did not clone the submodules, you can run: "git submodule update --init --recursive"

You can check that the submodule has successfully been obtained if the "yolov3" directory is not empty. 

Next, you will need to download the requirements. First, ensure you are in the FinalGroupPoject directory. Then, please run: 
```bash 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -r yolov3/requirements.txt
```
This does the model training on the coco128 dataset by converting images to garyscale for better detection of grayscale images

Now, you should be able to run our test files: compareGrayscale.py and 

---

Then there is custom Dataset that we trained model yolo5 on our Faces for recognition purposes for more details refer [Custom Dataset](ps2798/README.md)