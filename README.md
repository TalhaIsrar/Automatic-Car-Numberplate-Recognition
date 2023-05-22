# BEE12B_ANPR_Talha_Israr

MEMBERS:

Talha Israr - 333633

Muhammad Hamza Javaid - 338928

Hafiz Rayan Ahmed - 332611


ABSTRACT:

This report presents an Automatic Number Plate Recognition (ANPR) system utilizing YOLOv7 for license plate detection, DSP techniques for image preprocessing, and Easy OCR for character recognition. The system aims to enhance traffic management, law enforcement, and parking management through real-time and accurate recognition of number plates. Image preprocessing techniques, such as grayscale conversion, filtering, sharpening, and enhancing frequency changes, are applied to cropped license plate images. Easy OCR extracts characters, and the recognized text is plotted back onto the original image. Experimental evaluations demonstrate the system's effectiveness in various scenarios, contributing to enhanced public safety and operational efficiency in traffic management, law enforcement, and parking management.


INSTRUCTIONS:

This code required weights to be run. File named best.pt can be downloaded from link given below and is to be pasted in the following directory runs\train\exp\weights

https://drive.google.com/drive/folders/15ITE1Ie5VSsD7TcrRyr1FMXfniuOYljj?usp=sharing

To download the dataset go to the following link and paste the folder license-1 in the same directory as this file:

https://drive.google.com/drive/folders/12-576bd4asdjo4WUkTXAgku3srg66FrB?usp=sharing

To run this place the images you want to test in a directory named test_im in the directory where this file is found and run the following command
python detect.py --weights runs/train/exp/weights/best.pt --conf 0.3 --source test_im
