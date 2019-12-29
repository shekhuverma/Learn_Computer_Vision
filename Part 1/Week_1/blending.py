##References



try:
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    from PIL import Image
except:
    print ("please install the dependencies \n using command pip3 install requirements.txt")

image=cv2.imread("images/obama.jpg")  #reading the image into opencv
image1=Image.open("images/trump.jpg")
#quantization




cv2.imshow("sad",image15)
cv2.waitKey(0)   #to keep the ouput window to open
cv2.destroyAllWindows() #pressing anykey to close the ouput windows
