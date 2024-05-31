# DeepLearning-Celebrity-Image-Processing
Deep Learning Project of Computer Vision with Classification+Style Transfer

## Project Overview

This project, CelebVision, is a comprehensive celebrity image processing system. The project focuses on two main tasks: image classification and style transfer using both customized and pretrained models. 

## Table of Contents
1. [Data Overview](#data-overview)
2. [Task 1: Image Classification](#task-1-image-classification)
   - Customized Model: CNN
   - Pretrained Model: InceptionV3
3. [Task 2: Style Transfer](#task-2-style-transfer)
   - Customized Model: CycleGAN
   - Pretrained Model: VGG-19
4. [Model Operations & Parameter Update](#model-operations--parameter-update)
5. [Findings](#findings)
6. [References](#references)

## Data Overview
The dataset used is the CelebA dataset, which includes 202,599 images of celebrities annotated with 40 facial attributes. The dataset has no missing values and is ideal for tasks requiring image classification and style transfer.

## Task 1: Image Classification
### Objective
Develop and evaluate a machine learning model capable of accurately classifying the gender of individuals in the CelebA dataset based on facial attributes.

### Customized Model: CNN
A custom deep convolutional neural network (CNN) designed specifically for the CelebA dataset. This model provides full control over the architecture, allowing detailed optimization and adaptation to the dataset's characteristics.

**Pros:**
- Tailored Architecture for better performance
- Full control over the model

**Cons:**
- Time-consuming and computationally intensive
- Risk of overfitting

### Pretrained Model: InceptionV3
InceptionV3 is a deep CNN designed by Google, known for its high accuracy and scalability.

**Pros:**
- High accuracy and excellent performance on various image classification tasks
- Capable of handling large-scale datasets

**Cons:**
- Complex architecture
- Harder to implement and tune


## Task 2: Style Transfer
### Objective
Train and evaluate models to apply specific artistic styles to content images, creating new images that blend the visual aesthetics of the style images with the structural elements of the content images.

### Customized Model: CycleGAN
CycleGAN is used for unpaired image-to-image translation, enabling style transfer without requiring paired training data.

**Pros:**
- Handles unpaired data
- Simplicity in architecture

**Cons:**
- Training instability and mode collapse
- Sensitive to hyperparameters
- Generated images may contain artifacts or appear blurry

### Pretrained Model: VGG-19
VGG-19 is a 19-layer deep CNN pretrained on the ImageNet dataset. It is used for extracting content and style features for style transfer.

**Pros:**
- High performance
- Easy to implement and computationally efficient

**Cons:**
- No model saved, requiring generation for each new input style/content image
- Hard to compare loss across different generation tasks

### Application
The models are deployed using Streamlit, allowing users to upload test images and apply style transfer in real-time.

## Model Operations & Parameter Update
The infrastructure is set up using AWS, with CloudWatch monitoring the application health. The models fetch new data from AWS S3 for retraining as needed.

## Findings
The customized CNN showed slightly higher accuracy compared to InceptionV3 for gender classification. For style transfer, CycleGAN and VGG-19 both demonstrated effective style applications, with VGG-19 providing more detailed style features.


## Authors
- Siyan Li
- Stella Wang
- Xinran Wang
- Yumin Zhang
