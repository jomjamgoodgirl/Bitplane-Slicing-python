import cv2 
import numpy as np
img = cv2.imread(r'images\lotus.jpg', 0) 
out = []

for k in range(0, 7):
    # create an image for each k bit plane
    plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
        
    # execute bitwise and operation
    res = cv2.bitwise_and(plane, img)
        
    # multiply ones (bit plane sliced) with 255 just for better visualization
    x = res * 255
    
    # append to the output list
    out.append(x)    
    cv2.imshow("bitplane_%dbit"%(k+1), x)    
    cv2.imwrite("outputimg/bitplane2_%d.png"%(k), x)
    cv2.waitKey(1000)



# cv2.imshow("bit plane", np.hstack(out))
cv2.waitKey()