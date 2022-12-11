# Secsvm-classifier

### What does this repository contain
This repo contain a malware analysis report called secsvm classifier .
This classifier is a static malware analysis report that uses machine learning to classify malware samples.

### Packages
The secsvm classifier is written in python and uses some packages.
When you clone this repo you should run the following command to install the packages:
```bash
pip install -r requirements.txt
```
Its been tested on python 3.6.9 and ubuntu 18.04

### How to use
* Clone this repo and follow the instructions above to install the packages.
* You should use feature extraction to extract features from the malware samples you want to classify.(use 'tools' folder)
* Then take the extracted features and put them in the folder called "data_for_niv_avi/test" and "data_for_niv_avi/train".
* In the folder called 'apg' you should change the paths in the file called "settings.py" to the paths of the folders you want to use.
* After that you should run the file called "test_secsvm.py" to classify the malware samples.




https://user-images.githubusercontent.com/92351152/206868200-0792ac74-10b4-425e-893e-35faaf10b7f0.mp4

