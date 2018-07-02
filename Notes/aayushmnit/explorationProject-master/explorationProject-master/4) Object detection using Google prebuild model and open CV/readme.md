# Object-Detector-App

A real-time object recognition application using [Google's TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) and [OpenCV](http://opencv.org/).

## Getting Started
Open object_detection_tutorial.ipynb notebook to run the code sequentially. Make sure you have all the requirements installed on your machine before running it.

## Tests
```
pytest -vs utils/
```

## Requirements
- [Anaconda / Python 3.5](https://www.continuum.io/downloads)
- [TensorFlow 1.2](https://www.tensorflow.org/)
- [OpenCV 3.0](http://opencv.org/)

## Notes
- OpenCV 3.1 might crash on OSX after a while, so that's why I had to switch to version 3.0. See open issue and solution [here](https://github.com/opencv/opencv/issues/5874).

## Output
![alt text](https://github.com/aayushmnit/explorationProject/blob/master/4\)%20Object%20detection%20using%20Google%20prebuild%20model%20and%20open%20CV/output.gif)
