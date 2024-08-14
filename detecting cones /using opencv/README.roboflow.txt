
Data Augmentaded - Cone dataset - v1 2022-11-13 7:00pm
==============================

This dataset was exported via roboflow.com on November 17, 2022 at 11:01 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 11161 images.
Cone are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x480 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random brigthness adjustment of between -20 and +20 percent
* Random exposure adjustment of between -20 and +20 percent
* Random Gaussian blur of between 0 and 4.75 pixels


