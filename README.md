# Image-Classification
Create an Image Classification model to classify animal species using Python Tensorflow/Keras.

Training the model & determining model sufficiency:

1) Load in over 6000 images to use as training and validation data
2) Convert each image to array format through OpenCV
3) Resize each image to 170x170
4) Create target labels for the images by mapping each species name (cow, cat, crocodile, chameleon, dragonfly) to integer labels 0, 1, 2, 3, and 4
5) Randomly shuffle the data
6) Split the data into training and testing data
7) Use the training data to create a Deep Learning model in Tensorflow/Keras to predict species from an image
8) Visualize how the model's loss and accuracy changes throughout each epoch.
9) Determine the validation loss and accuracy.

Testing the model:

1) Create a function to extract an image from the internet
2) Ask the user to input the link to the image and the species of the image
3) Obtain and resize the image to 170x170
4) Load in the Image Classifcation model created in the training step.
5) Use the model to predict the species.
6) Display the image and whether the model predicted correctly or incorrectly.
7) Record the amount of times the model predicted correctly/incorrectly by appending the results to a TXT File.
