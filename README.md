![](https://zenodo.org/badge/DOI/10.5281/zenodo.1037359.svg)

Editor: Mike Chen

# Finetune AlextNet to Be Compatible with TensorFlow 2.2 

The editor has modified the lines of code to be compaible with the environment of TensorFlow 2.2, CUDA 11.0 and cuDNN 8.0.1 In addition, all the scripts including the modified and new created scripts, has completed the running on the Miniconda 4.8.3. It can show 10 epochs. However, the tensorboard need to be improved for visibility.

## Requirements

- Miniconda 4.8.3 (or related Ananconda version) 
- Python 3.7.7
- CUDA Driver 450.57 ppa
- CUDA 11.0
- cuDNN 8.0.1
- TensorFlow 2.0~2.2
- Keras 2.4.3
- Jupyter Notebook 6.0.3

## New Created Scripts

The original scripts do not inlcude both dataset-splitting and image-labelling functionalities. So it is not easy for fresh developers to understand and run the original scripts. Therefore, the editor writes both the scripts of dataset-splitting and image-labelling. It streamlines the finetune of the AlexNet model. 

## Example train.txt:

Please notice that dog is labeled with 0 and cat is labeled with 1. I am pleased to write the full list of images in order to make a explicit explaination to the users. It is quite different from the original format by the author.

/home/mike/Documents/finetune_alexnet_with_tf/dogs_vs_cats/train/dog.11001.jpg 0
/home/mike/Documents/finetune_alexnet_with_tf/dogs_vs_cats/train/dog.11002.jpg 0
/home/mike/Documents/finetune_alexnet_with_tf/dogs_vs_cats/train/cat.5276.jpg 1
/home/mike/Documents/finetune_alexnet_with_tf/dogs_vs_cats/train/cat.5278.jpg 1

## The Issue of CUPTI 

If users meet the error of CUPTI(Nvidia CUDA Profiling Tools Interface), the easiest method is to add "--cap-add=CAP_SYS_ADMIN" in the command. 

$ python finetune.py --cap-add=CAP_SYS_ADMIN

According to the current trace report from CUPTI, it is only the error reminding message. It reminds users of lacking super user privilege. At the present, it is hard to remove the reminding message. Please take the reference of the CUPTI as follows.

https://docs.nvidia.com/cupti/Cupti/index.html


## GPU Growth 

After upgrading the system to CUDA 11.0/cuDNN 8.0.1, Nvidia Truing GPU allows to initiate the GPU growth model, i.e., boosting Deep Learning applications as soon as possible with the growing GPU Memory. The avantage is that the training is much faster than ever before. But the dsiavantage is that the system does not automatically or slowly remove the used GPU memory sometimes. It incurs the phenomenan: CUDA_ERROR_OUT_OF_MEMORY:out of memory. Users either wait for the system removal of the GPU memory or end the completed process(such as exit from Juputer Notebook or restart the computer). 




# Finetune AlexNet with Tensorflow

**Update 15.06.2016**

I revised the entire code base to work with the new input pipeline coming with TensorFlow >= version 1.2rc0. You can find an explanation of the new input pipeline in a new [blog post](https://kratzert.github.io/2017/06/15/example-of-tensorflows-new-input-pipeline.html) You can use this code as before for finetuning AlexNet on your own dataset, only the dependency of OpenCV isn't necessary anymore. The old code can be found in [this past commit](https://github.com/kratzert/finetune_alexnet_with_tensorflow/tree/5d751d62eb4d7149f4e3fd465febf8f07d4cea9d).

This repository contains all the code needed to finetune [AlexNet](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) on any arbitrary dataset. Beside the comments in the code itself, I also wrote an article which you can find [here](https://kratzert.github.io/2017/02/24/finetuning-alexnet-with-tensorflow.html) with further explanation.

All you need are the pretrained weights, which you can find [here](http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/) or convert yourself from the caffe library using [caffe-to-tensorflow](https://github.com/ethereon/caffe-tensorflow).
If you convert them on your own, take a look on the structure of the `.npy` weights file (dict of dicts or dict of lists).

**Note**: I won't write to much of an explanation here, as I already wrote a long article about the entire code on my blog.

## Requirements

- Python 3
- TensorFlow >= 1.2rc0
- Numpy


## TensorBoard support

The code has TensorFlows summaries implemented so that you can follow the training progress in TensorBoard. (--logdir in the config section of `finetune.py`)

## Content

- `alexnet.py`: Class with the graph definition of the AlexNet.
- `finetune.py`: Script to run the finetuning process.
- `datagenerator.py`: Contains a wrapper class for the new input pipeline.
- `caffe_classes.py`: List of the 1000 class names of ImageNet (copied from [here](http://www.cs.toronto.edu/~guerzhoy/tf_alexnet/)).
- `validate_alexnet_on_imagenet.ipynb`: Notebook to test the correct implementation of AlexNet and the pretrained weights on some images from the ImageNet database.
- `images/*`: contains three example images, needed for the notebook.

## Usage

All you need to touch is the `finetune.py`, although I strongly recommend to take a look at the entire code of this repository. In the `finetune.py` script you will find a section of configuration settings you have to adapt on your problem.
If you do not want to touch the code any further than necessary you have to provide two `.txt` files to the script (`train.txt` and `val.txt`). Each of them list the complete path to your train/val images together with the class number in the following structure.

```
Example train.txt:
/path/to/train/image1.png 0
/path/to/train/image2.png 1
/path/to/train/image3.png 2
/path/to/train/image4.png 0
.
.
```
were the first column is the path and the second the class label.

The other option is that you bring your own method of loading images and providing batches of images and labels, but then you have to adapt the code on a few lines.
