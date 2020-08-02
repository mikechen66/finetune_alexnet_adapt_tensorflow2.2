# label_dataset_train.py

"""
Mike Chen  

To make users to easily understand how to label the train dataset, I add 
the new script to be integrated into the finetune. Please execute the 
command as similar as follows. 

cd /home/mike/Documents/finetune_alexnet_with_tf
$ python label_dataset_train.py
"""

import os

# Define the generate function
def generate(dir):
    # Return the list of the designated files
    files = os.listdir(dir) 
    # Sort the files
    files.sort()  
    # Create the file of val.txt and the parameter of 'a' means locating 
    # the end of the image content. 
    listText = open('train.txt', 'a') 
    # Iterate the file in files
    for file in files:  
        # The function of os.path.split() returns paths and related file 
        # name 
        fileType = file.split('.')
        # If the suffix is txt, it continues the iteration.
        if fileType[1] == '.txt':  
            continue
        # Label iamges if it is else. 
        else: 
            # dog is labeled with 0 
            if 'dog' in file:
                label=0
            # cat is labeled with 1
            elif 'cat' in file:
                label=1
            else:
                print("error")

        # Give the full path of any images
        name = outer_path + file + ' ' + str(int(label)) + '\n'
        listText.write(name)

    listText.close()

# Path of the val images
outer_path = '/home/mike/Documents/finetune_alexnet_with_tf/dogs_vs_cats/train/'

# Call the generate function  
generate(outer_path)
