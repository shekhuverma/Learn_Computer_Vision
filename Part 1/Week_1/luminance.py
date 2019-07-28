try:
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
except:
    print ("please install the dependencies \n using command pip3 install requirements.txt")

image=cv2.imread("images/obama.jpg")  #reading the image into opencv

image_bw=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([image],[0],None,[256],[0,256]) #Calculating histogram of the image

cdf = hist.cumsum() #calculating the CDF of the histogram

plt.subplot(121) #to plot the histogram using matplotlib
plt.plot(hist)
plt.suptitle('Before and After histogram normalisation', fontsize=14) #histogram title


m=cdf.min()
d=(image_bw.shape[0]*image_bw.shape[1])-m
cdf_norm=((cdf-m)/d)*255
cdf_norm=cdf_norm.astype("uint8")

normalised_image=cdf_norm[image_bw] #mapping the ouput of cdf with the input image
#Calculating histogram of the nomalised image
hist = cv2.calcHist([normalised_image],[0],None,[256],[0,256])
cdf = hist.cumsum()

plt.subplot(122) #to plot the histogram using matplotlib
plt.plot(hist)
plt.show()


#histogram normalisation using opencv
normalised_image_2=cv2.equalizeHist(image_bw)

#brightness
new_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)  #converting the image to HSV and increasing only the Value part of the image (3rd channel) 
value=25 #brightness increment value
new_image[:,:,2]=np.where((255-new_image[:,:,2]) <value,255,new_image[:,:,2]+value)
new_image=cv2.cvtColor(new_image,cv2.COLOR_HSV2BGR)

#saturation
new_image2=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)  #converting the image to HSV and increasing only the Value part of the image (3rd channel) 
value=25 #saturation increment value
new_image2[:,:,1]=np.where((180-new_image2[:,:,1]) <value,180,new_image2[:,:,1]+value)
new_image2=cv2.cvtColor(new_image2,cv2.COLOR_HSV2BGR)

cv2.imshow("Black and White ,Histogram Normalised , Histogram Normalised using OpenCv",np.hstack((image_bw,normalised_image,normalised_image_2)))
cv2.imshow("orignal image , brightness increased image",np.hstack((image,new_image)))  #To show the ouput
cv2.imshow("orignal image , saturation increased image",np.hstack((image,new_image2)))  #To show the ouput
cv2.imshow("RGB image , HSV image",np.hstack((image,image_hsv)))

cv2.waitKey(0)   #to keep the ouput window to open
cv2.destroyAllWindows() #pressing anykey to close the ouput windows
