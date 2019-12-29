##References
##https://stackoverflow.com/questions/46390779/automatic-white-balancing-with-grayworld-assumption
##https://pippin.gimp.org/image-processing/chapter-automaticadjustments.html

try:
    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
except:
    print ("please install the dependencies \n using command pip3 install requirements.txt")

image=cv2.imread("images/obama.jpg")  #reading the image into opencv

image_lab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)

##Using Grayworld Assumption

a=np.average(image_lab[:,:,1])
b=np.average(image_lab[:,:,2])
image_lab[:, :, 1] = image_lab[:, :, 1] - ((a - 128) * (image_lab[:, :, 0] / 255.0) * 1.1)
image_lab[:, :, 2] = image_lab[:, :, 2] - ((b - 128) * (image_lab[:, :, 0] / 255.0) * 1.1)
image_lab = cv2.cvtColor(image_lab, cv2.COLOR_LAB2BGR)

##cv2.imshow("LAB image",np.hstack((image,image_lab)))  #To show the ouput

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) #converting BGR to RGB to plot in matplotlib
plt.title("original ")
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(image_lab, cv2.COLOR_BGR2RGB))
plt.title("Colour corrected")
##plt.show()

def remap(v, mi, ma):
    return (v-mi)/(ma-mi)


def component_streching(image):
    #Calculating minimum and mazimum values of RGB channels
    image2=image
    b_min=image[:,:,0].min()
    b_max=image[:,:,0].max()
    g_min=image[:,:,1].min()
    g_max=image[:,:,1].max()
    r_min=image[:,:,2].min()
    r_max=image[:,:,2].max()

##    image2[:,:,0]=remap(image[:,:,0],b_min,b_max)
    image2[:,:,0]=(image[:,:,0]-b_min)/(b_max-b_min)
    image2[:,:,1]=remap(image[:,:,1],g_min,g_max)
    image2[:,:,2]=remap(image[:,:,2],r_min,r_max)
##    return image2
    print(image2[:,:,0])
temp=component_streching(image)

print(temp.dtype)
cv2.imshow("dasdas",temp)


cv2.waitKey(0)   #to keep the ouput window to open
cv2.destroyAllWindows() #pressing anykey to close the ouput windows
