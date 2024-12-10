# MachineLearningGroup8
Final Group Project for Intro to Machine Learning

Tyler Lapiana,
Anindhya Kushagra,
Rushil Patel,
Prateek Sharma,

**IMPORTANT INSTRUCTIONS**:
First, our project requires the use of a GPU.

Second, the results of the second improvement are visual in nature, so it may be better to view the results on a system that can easily show images/videos.

---

When cloning the repository, please run the command: 
```bash
git clone --recurse-submodules https://github.com/tjl9096/MachineLearningGroup8
```

If you have already cloned the repository but did not clone the submodules, you can run: 
```bash
git submodule update --init --recursive
```

---

Next, you will need to download the requirements. 

If you did not already move into the created directory, please do so:
```bash
cd MachineLearningGroup8
```

Then, please run: 
```bash 
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
This may take some time. On average, ours took around 15 minutes.

---

One of our propsed changes does the model training on the coco128 dataset by converting images to grayscale for better detection of grayscale images.

You should now be able to run our test file with the command
```bash
python compareGrayscale.py
```

There may be an error where the code cannot find the location of the grayscale database. If this is the case, you will need to modify the grayscale.yaml. You would have to change the value under "path" so that it finds the directory found at: yolov3/datasets/grayscale

---

Then there is a custom Dataset that we trained model yolov5 on our Faces for recognition purposes. For more details refer to the custom dataset README: [Custom Dataset](FacialRecognition/README.md)

This file is located under the FacialRecognition directory.
