# LUX

## Web application to adjust illumination of dark images.

LUX is a web application I created for my senior project senior project *Lightning up images with deep learning techniques*. It is programmed in Flask and it uses a Generative Adversarial Network (GAN) to fix the brightness of extremely dark PNG and JPEG images.

Input (dark image)     	|  Output (illuminated image)
:-------------------------:|:-------------------------:
![3000x2000-fuji-20095-x12](https://user-images.githubusercontent.com/24246102/234341235-a4f684e1-cd04-4694-af91-f438e3813821.png)  |  ![3000x2000-fuji-20095-x12 lux-output](https://user-images.githubusercontent.com/24246102/234341258-e3f41554-5d65-488d-aef2-b3ac532ad941.png)

## About LUX

## The GAN model

The encoder-decoder network that processes the image was trained with a GAN approach using the [Tensorflow](https://www.tensorflow.org/) package. The architecture is a modification of the well-known [pix2pix](https://phillipi.github.io/pix2pix) model, while the dataset has been obtained from the [Learning to See in the Dark](https://cchen156.github.io/SID.html) collection. All the details on the architecture of the model, the obtaining of the dataset and the training process can be found in the project memoir. Besides, the scripts and notebooks employed in the process are allocated in the [lux-model](https://github.com/dcabezas98/lux-model) repository.

## Google Cloud deployment

Originally, Lux was dockerized and deployed on Google Cloud (the details are in the memoir), but it ran only for a few months due to the financial cost.

![deployment](https://user-images.githubusercontent.com/24246102/234350117-7c0697dc-ca8a-4e3c-899e-88ce4d0b5b23.png)

## How to try

You can easily run the development version of LUX on your PC, although I've only tested it in Linux.

The trained GAN generator can be downloaded in the link below:

https://drive.google.com/drive/folders/1S7Oy1wJnjbZppYpfAtSQfBJThNbcxtzR?usp=sharing

It must be allocated inside the [static/models](https://github.com/dcabezas98/lux/tree/main/lux/static/models) folder. Then, the app (`main.py`) can be run with Python3 (the TensorFlow package must be installed). Three demo images can be found in the repository, but you can upload any dark PNG or JPEG image.

The quality of the output is not good for low resolution inputs.
