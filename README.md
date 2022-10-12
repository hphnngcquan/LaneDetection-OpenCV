**LaneDetection_Thesis2022-23**

Project Development Plan:
1. Camera Calibration
2. Preprocessing 
3. Bird's Eye View
---
## Camera Calibration
- Prepare 9x6 pattern chessboard for calibration
![Chessboard Pattern for Calibration](/calib/9x6_pattern.jpg)
<p align = "center">
9x6 chessboard pattern

- Pattern setting (at least 10 scenario)
- Draw Chessboard Connners
- Undistort Test Image
- Result
![Calibration Result for Test Image](/output_images/chessboard_conners//calibresult.jpg)
<p align = "center">
Calibration Result for Test Image


For Reference: [OpenCV Camera Calibration Tutorial in Python](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html)

## Preprocessing
### Bird's Eye View
The chosen source and destination point

| Source        | Destination   |View|  
|:-------------:|:-------------:| :-------:| 
| 190, 720     | x, 0        | Bottom left|
| 596, 447      | x, 720      | Top left|
| 685, 447     | x, 720      | Top right|
| 1125, 720      | x, 0        | Bottom right|



