import cv2

vcap = cv2.VideoCapture(0) # 0=camera

if vcap.isOpened(): 
    # get vcap property 
    print("width", vcap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`

    print("height", vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`

    # fps = vcap.get(cv2.cv.CV_CAP_PROP_FPS)