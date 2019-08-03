##References
##http://machinelearninguru.com/computer_vision/basics/convolution/image_convolution_1.html
##https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/

try:
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
except :
    print ("please install the dependencies \n using command pip3 install requirements.txt")
    
image=cv2.imread("images/obama.jpg")  #reading the image into opencv
image_bw=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


##linear filtering

kernal=1/9*(np.ones((3,3),dtype="float32"))    #bluring kernal
kernal2=1/25*(np.ones((5,5),dtype="float32")) #bluring kernal


def convolution(image,kernal):
    padding=int(kernal.shape[0]-1)
    pd=int(padding/2)

    ##Padding the image so that we can convolve the corners and edges
    image_padded = np.zeros((image.shape[0] + padding, image.shape[1] + padding),dtype="uint8")
    image_padded[pd:-pd, pd:-pd] = image
    image_out=np.zeros_like(image) #to store the convolution result
    for x in range(image_bw.shape[1]):
        for y in range(image_bw.shape[0]):
            roi=image_padded[x:x+padding+1,y:y+padding+1]
            image_out[x,y]=int(np.sum((roi*kernal)))
        
    return image_out

#Using OpenCv built in functions

#sharpening kernal
kernal3 = np.array([[-1,-1,-1], 
                   [-1, 9,-1],
                   [-1,-1,-1]])

sharpened = cv2.filter2D(image, -1, kernal3)

blur = cv2.GaussianBlur(image_bw,(5,5),0) #applying 5*5 blurring kernal

cv2.imshow("3x3 avg kernal ",convolution(image_bw,kernal))
cv2.imshow("5x5 avg kernal",convolution(image_bw,kernal2))
cv2.imshow("Opencv Blurr function",blur)
cv2.imshow("sharpned Image ",sharpened)
cv2.imshow("original Image ",image_bw)

cv2.waitKey(0)   #to keep the ouput window to open
cv2.destroyAllWindows() #pressing anykey to close the ouput windows
