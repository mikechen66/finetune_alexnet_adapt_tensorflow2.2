
"""
Editor: Mike Chen 

Split the file of train.zip(after unzipping) into training, validation and test sets(70/15/15) and 
created .txt files for each subset containing the path to the image and the class label.

"""

import os
import numpy as np
import shutil
import random

# The source directory includes all the images. 
src = '/home/mic/Documents/finetune_alexnet_with_tf/total_images'
# Creating Train/Val/Test folders (One time use)
dst = '/home/mic/Documents/finetune_alexnet_with_tf/dogs_vs_cats'
# -classes_dir = ['total_images', 'train', 'val', 'test']

train_ratio = 0.75
val_ratio = 0.15
test_ratio = 0.15

os.makedirs(dst +'/train')
os.makedirs(dst +'/val')
os.makedirs(dst +'/test')

total_images = os.listdir(src)
np.random.shuffle(total_images)
train, val, test = np.split(np.array(total_images),
                            [int(len(total_images) * (1-(val_ratio+test_ratio))), 
                             int(len(total_images) * (1-test_ratio))])

train = [src+'/'+ name for name in train.tolist()]
val = [src+'/' + name for name in val.tolist()]
test = [src+'/' + name for name in test.tolist()]

print('Total: ', len(total_images))
print('Training: ', len(train))
print('Validation: ', len(val))
print('Testing: ', len(test))

# Copy-pasting images
for name in train:
    shutil.copy(name, dst +'/train')

for name in val:
    shutil.copy(name, dst +'/val')

for name in test:
    shutil.copy(name, dst +'/test')