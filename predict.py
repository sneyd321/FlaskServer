'''
Using Bottleneck Features for Multi-Class Classification in Keras

We use this technique to build powerful (high accuracy without overfitting) Image Classification systems with small
amount of training data.

The full tutorial to get this code working can be found at the "Codes of Interest" Blog at the following link,
http://www.codesofinterest.com/2017/08/bottleneck-features-multi-class-classification-keras.html

Please go through the tutorial before attempting to run this code, as it explains how to setup your training data.

The code was tested on Python 3.5, with the following library versions,
Keras 2.0.6
TensorFlow 1.2.1
OpenCV 3.2.0

This should work with Theano as well, but untested.
'''
import tensorflow as tf
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras import applications
from keras.utils.np_utils import to_categorical
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import math
import cv2

# dimensions of our images.
img_width, img_height = 224, 224

top_model_weights_path = 'bottleneck_fc_model.h5'


def predict(path):
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config = config)
    
    # load the class_indices saved in the earlier step
    class_dictionary = np.load('class_indices.npy').item()

    num_classes = len(class_dictionary)

    # add the path to your test image below
    # image_path = 'oven.jpeg'
    image_path = path

    orig = cv2.imread(image_path)

    print("[INFO] loading and preprocessing image...")
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)

    # important! otherwise the predictions will be '0'
    image = image / 255

    image = np.expand_dims(image, axis=0)

    # build the VGG16 network
    model = applications.VGG16(include_top=False, weights='imagenet')

    # get the bottleneck prediction from the pre-trained VGG16 model
    bottleneck_prediction = model.predict(image)

    # build top model
    model = Sequential()
    model.add(Flatten(input_shape=bottleneck_prediction.shape[1:]))
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='sigmoid'))

    model.load_weights(top_model_weights_path)

    # use the bottleneck prediction on the top model to get the final
    # classification
    class_predicted = model.predict_classes(bottleneck_prediction)

    probabilities = model.predict_proba(bottleneck_prediction)

    inID = class_predicted[0]

    inv_map = {v: k for k, v in class_dictionary.items()}

    label = inv_map[inID]

    # get the prediction label
    print("Image ID: {}, Label: {}".format(inID, label))
    print("Probability: {}%".format(bottleneck_prediction[0][0][0][0]* 100))

    # display the predictions with the image
    # cv2.putText(orig, "Predicted: {}".format(label), (10, 30),
    #             cv2.FONT_HERSHEY_PLAIN, 1.5, (43, 99, 255), 2)

    # cv2.imshow("Classification", orig)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return label

# predict('dishwasher.jpeg')
