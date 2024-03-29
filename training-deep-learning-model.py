import glob
import cv2
import matplotlib.pyplot as plt
import os
import random
import statistics
import numpy as np
from tensorflow.keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D,Dropout
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
from keras.models import load_model
from keras.callbacks import EarlyStopping
import pandas as pd

# Import the images
croc_gator= glob.glob('animal-project-images/CrocGator/*.*')
croc_gator2= glob.glob('animal-project-images/CrocGator2/*.*')
croc_gator3= glob.glob('animal-project-images/CrocGator3/*.*')
croc_gator4= glob.glob('animal-project-images/CrocGator4/*.*')
croc_gator5= glob.glob('animal-project-images/CrocGator5/*.*')
croc_gator6= glob.glob('animal-project-images/CrocGator6/*.*')
croc_gator63= glob.glob('animal-project-images/CrocGator63/*.*')
cat= glob.glob('animal-project-images/Cat/*.*')
cat2= glob.glob('animal-project-images/Cat2/*.*')
cow= glob.glob('animal-project-images/Cow/*.*')
chameleon= glob.glob('animal-project-images/Chameleon/*.*')
chameleon2= glob.glob('animal-project-images/Chameleon2/*.*')
chameleon3= glob.glob('animal-project-images/Chameleon3/*.*')
dragonfly= glob.glob('animal-project-images/Dragonfly/*.*')
dragonfly2= glob.glob('animal-project-images/Dragonfly2/*.*')
dragonfly3= glob.glob('animal-project-images/Dragonfly3/*.*')
dragonfly4= glob.glob('animal-project-images/Dragonfly4/*.*')

# convert to image format
dragonfly_img=[]
for each in dragonfly:
    image= cv2.imread(each)
    dragonfly_img.append(image)
for each in dragonfly2:
    image= cv2.imread(each)
    dragonfly_img.append(image)
for each in dragonfly3:
    image= cv2.imread(each)
    dragonfly_img.append(image)
for each in dragonfly4:
    image= cv2.imread(each)
    dragonfly_img.append(image)

crocgator_img=[]
for each in croc_gator:
    image= cv2.imread(each)
    crocgator_img.append(image)
for each in croc_gator2:
    image= cv2.imread(each)
    crocgator_img.append(image)
for each in croc_gator3:
    image= cv2.imread(each)
    crocgator_img.append(image)
for each in croc_gator4:
    image= cv2.imread(each)
    crocgator_img.append(image)
for each in croc_gator5:
    image= cv2.imread(each)
    crocgator_img.append(image)
for each in croc_gator6:
    image= cv2.imread(each)
    crocgator_img.append(image)
for each in croc_gator63:
    image= cv2.imread(each)
    crocgator_img.append(image)

cat_img=[]
for each in cat:
    image= cv2.imread(each)
    cat_img.append(image) 
for each in cat2:
    image= cv2.imread(each)
    cat_img.append(image)
    
cow_img=[]  
for each in cow:
    image= cv2.imread(each)
    cow_img.append(image)

chameleon_img=[]
for each in chameleon:
    image= cv2.imread(each)
    chameleon_img.append(image)
for each in chameleon2:
    image= cv2.imread(each)
    chameleon_img.append(image)
for each in chameleon3:
    image= cv2.imread(each)
    chameleon_img.append(image)
    
 # Initiate function
def show_random_image(piclist): 
    """Display a random image from a list of images."""
    # Find random image
    n= len(piclist)-1
    random_number= random.sample(range(n),1)[0]
    image= piclist[random_number]
    # Plot
    plt.imshow(image)
    plt.axis('off')
    plt.title(f'Element: {random_number}')

# Display images from 3 species
show_random_image(cow_img)
show_random_image(cat_img)
show_random_image(chameleon_img)


# reshape all images to be 170x170 and append to a new list
cows=[] 
for image in cow_img:
    cows.append(cv2.resize(image, (170,170), interpolation=cv2.INTER_AREA))

cats= []
for image in cat_img:
    cats.append(cv2.resize(image, (170,170), interpolation=cv2.INTER_AREA))

crocs=[]
for image in crocgator_img:
    crocs.append(cv2.resize(image, (170,170), interpolation=cv2.INTER_AREA))

chameleons=[]
for image in chameleon_img:
    chameleons.append(cv2.resize(image, (170,170), interpolation=cv2.INTER_AREA))
    
dragonflies=[]
for image in dragonfly_img:
    dragonflies.append(cv2.resize(image, (170,170), interpolation=cv2.INTER_AREA))

# Assign all images to one variable
features= np.vstack([cows,cats,crocs,chameleons,dragonflies]) 

# map species labels to integer labels
class0= [0 for i in range(len(cows))]
class1= [1 for i in range(len(cats))] 
class3= [2 for i in range(len(crocs))]
class4= [3 for i in range(len(chameleons))]
class5= [4 for i in range(len(dragonflies))]
classes= np.concatenate([class0,class1,class3,class4,class5])

# randomly shuffle the data
features, classes= list(features), list(classes)
together= list(zip(features,classes))
random.shuffle(together)
features, classes= zip(*together)
features, classes= np.array(features), np.array(classes).reshape(-1,1)

# separate into training and testing data
X_train, X_test, y_train, y_test= train_test_split(features, classes, test_size=0.2, random_state=12)

# obtain the dimensions
rows, cols, channels = features.shape[1:]

# train images on Tensorflow/Keras Deep Learning Model and save the resulting model
adam= Adam(learning_rate=0.001) 
ES= EarlyStopping(monitor= 'val_loss', patience= 2, restore_best_weights=True )
model= Sequential()
model.add(Conv2D(50, kernel_size=3, activation='relu', input_shape=(rows,cols,channels), padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(rate=0.2))
model.add(Conv2D(25, kernel_size=3, activation='relu',padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(rate=0.2))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(25, activation='relu'))
model.add(Dense(5, activation='softmax'))
model.compile(optimizer=adam ,loss='sparse_categorical_crossentropy',metrics=['accuracy'])
history= model.fit(X_train, y_train, epochs=20, batch_size=100, validation_data=(X_test, y_test), callbacks= [ES])
model.save('imagemodelNEW.h5')

# Show a summary of the results
print(model.summary())

# visualize the loss and the validation loss throughout the training process
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

# visualize the accuracy and the validation accuracy throughout the training process
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])

# Create a DataFrame of the model history to view how the loss & accuracy changed over time
df= pd.DataFrame(history.history)
print(df)

# Obtain the overall loss and accuracy metrics on unseen testing data
print(model.evaluate(x=X_test, y= y_test))



