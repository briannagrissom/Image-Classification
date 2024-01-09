from keras.models import load_model
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
import urllib.request

# Define function to retrieve an image from the internet
def get_image(url):
    request = urllib.request.urlopen(url)
    array = np.asarray(bytearray(request.read()), dtype=np.uint8)
    image = cv2.imdecode(array, -1)
    return image

link= input('Insert path to image: ')
species= input('Insert the species: ').upper()

# Obtain the image and resize it
img= get_image(f'{link}')
img= cv2.resize(img, (170, 170))

# load in the model
model= load_model('ml-models/imagemodelNEW.h5') 

# expand the dimensions
img_new = []
img_new.append(img)
img_new = np.array(img_new)

# use the model to predict what species the image is
prediction_array= model.predict(img_new)
predicted= np.argmax(prediction_array)

# map numerical values to species names
classes= {0:'COW', 1:'CAT', 2:'CROCODILE', 3:'CHAMELEON', 4:'DRAGONFLY'}

# specify whether the model predicted correctly or incorrectly and display the image
if classes[predicted] == species:
    print(f'Model CORRECTLY predicted the class of {classes[predicted]}')
if classes[predicted] != species:
    print(f'Model was INCORRECT. It predicted the class of {classes[predicted]}')
plt.imshow(img_new[0])

# record if the model was correct/incorrect to a TXT file
if classes[predicted] == species:
    with open('Predicted Correctly','a') as file:
        file.write(f'predicted correctly: {classes[predicted]}')
if classes[predicted] != species:
    with open('Predicted Incorrectly','a') as file:
        file.write(f'predicted: {classes[predicted]}, actual species: {species}\n')
    

        
        
        
        
        
        
        
