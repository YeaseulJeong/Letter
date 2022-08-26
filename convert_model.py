import cv2
import numpy as np

def convert_img(receive_model, receive_img):
    net = cv2.dnn.readNetFromTorch(receive_model)
    # net = cv2.dnn.readNetFromTorch('python_models/eccv16/receive_model')
    # net = cv2.dnn.readNetFromTorch('python_models/instance_norm/receive_model')

    # Using DNN model in OpenCV
    # Torch is a framework used in Deep Learning model
    img = cv2.imread(receive_img)

    h, w, c = img.shape

    img = cv2.resize(img, dsize=(500, int(h / w * 500)))
    # Resizing maintaining the same proportion between width and height
    # w : h = 500 : new_height
    # new_height = 500 * h /w

    print(img.shape)
    # (325, 500, 3)

    MEAN_VALUE = [103.939, 116.779, 123.680]
    # Don't exactly know what these are but the most OPTIMAL VALUES

    blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)
    # blobFromImage() is data PREPROCESSING function
    # Changes of the DIMENSION is needed to use it in DNN model
    # print(blob.shape)
    # (1, 3, 325, 500)

    net.setInput(blob)
    output = net.forward()

    # Post Processing
    output = output.squeeze().transpose((1, 2, 0))
    output += MEAN_VALUE

    output = np.clip(output, 0, 255)
    # Limiting digits max 255
    output = output.astype('uint8')
    # Only in Integer type

    cv2.imshow('result', output)
    cv2.imshow('img', img)
    cv2.waitKey(0)

