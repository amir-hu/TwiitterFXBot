import cv2

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import urllib.request


def gen_labels():
        labels = {}
        with open("labels.txt", "r") as label:
            text = label.read()
            lines = text.split("\n")
            #print(lines) #print full list
            for line in lines[0:-1]:
                    hold = line.split(" ", 1)
                    labels[hold[0]] = hold[1]
        return labels

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def getpred(imagelink):
  model = tensorflow.keras.models.load_model('keras_model500.h5', compile=False)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first positioACn in the shape tuple, in this case 1.
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  
   
  request=urllib.request.Request(imagelink,None,hdr)
  url_response = urllib.request.urlopen(request)
  image = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)
  # img.show()
# Replace this with the path to your image
  print(type(image))
  # image = cv2.imread(img)
  
# center crop of image dimensions
  dim = image.shape[:2]#height then width
  yint = dim[0]/2 
  xint = dim[1]/2 
  xmin = int(np.floor(xint-yint)) 
  xmax = int(np.floor(xint+yint))
#print(dim[0], xmin, xmax)
  print("hellllllo")
# creating a center crop at the mid point of each image
  frame = image[0:dim[0],xmin:xmax]
#cv2.imshow('image',frame)#check image if cropped correctly

# resizing the image to be at least 224x224 and then cropping from the center
  size = (224, 224)
  image = cv2.resize(frame, size)
 
# turn the image into a numpy array
  image_array = image 

  print(type(image_array))

# Normalize the image
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
  data[0] = normalized_image_array

  
# run the inference
  prediction = model.predict(data)
  result = np.argmax(prediction[0])
  labels = gen_labels()

  print("hellllllo")

# prints the pokemon name
  

  return labels[str(result)]
