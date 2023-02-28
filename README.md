# Image-Classification
Creating an Image Classification model to classify animal species using Python Tensorflow/Keras.

Training the Image Classification model involved:

1) Loading in over 6000 images to use as training and testing data.
2) Converting each image into array format utilizing OpenCV
3) Resizing each image to 170x170; images need to be the same dimension in order to be trained on a machine learning model
4) Assigning all images into one Python variable named "features"
5) Creating target labels for the images by mapping each species name (cow, cat, crocodile, chameleon, dragonfly) to integer labels 0, 1, 2, 3, and 4.
6) Randomly shuffling the data; unshuffled training data will not allow the model to perform well.
7) Splitting the data into training and testing data using the train_test_split() Sci-Kit Learn function.
8) Using the training data to create a Deep Learning model in Tensorflow/Keras with the goal of predicting the image's species.
9) Visualizing how the model's loss and accuracy changed over time through a Matplotlib plot.
10) Evaluating the overall loss and accuracy on the testing data.

Testing the Image Classification model involved:

1) Creating a function to extract an image from the internet
2) Asking the user to input the link to the image and the species of the image
3) Obtaining and resizing the image to be 170x170
4) Loading in the Image Classifcation model created in the training step.
5) Using the model to predict the image's species.
6) Displaying the image and whether the model predicted correctly or incorrectly.
7) Recording the amount of times the model predicted correctly/incorrectly by appending the results to a TXT File.
