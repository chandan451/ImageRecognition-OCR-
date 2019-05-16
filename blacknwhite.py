import numpy as np
import PIL.Image as Img
import matplotlib.pyplot as plot
import sys
def blacknwhite(imArr):
    rowAvgArr = []
    newarr= imArr

    for eachRow in imArr:                           #for each row of the array
        for eachPixel in eachRow:                           #for each column/pixel in the each row of the image array
            pixAv=sum(eachPixel[:3])/3
            rowAvgArr.append(pixAv)
            
           
    imAv = sum(rowAvgArr)/len(rowAvgArr)
    
    for eachRow in newarr:
        for eachPixel in eachRow:
            if sum(eachPixel[:3])/3 > imAv:
                    eachPixel[0] = 255
                    eachPixel[1] = 255
                    eachPixel[2] = 255
                    eachPixel[3] = 255
                    
            else :
                    eachPixel[0] = 0
                    eachPixel[1] = 0
                    eachPixel[2] = 0
                    eachPixel[3] = 255
                    

    return newarr


i= Img.open("images/sentdex.png")
iArr= np.array(i)
iArr_real= np.array(i)

i2= Img.open("images/numbers/y0.4.png")
iArr2= np.array(i2)
iArr2_real= np.array(i2)

blacknwhite(iArr)
blacknwhite(iArr2)


ax1= plot.subplot2grid((8,6), (0,0),rowspan= 4, colspan=4)
ax2= plot.subplot2grid((8,6), (4,0),rowspan= 4, colspan=4)
ax3= plot.subplot2grid((8,6), (0,4),rowspan= 4, colspan=4)
ax4= plot.subplot2grid((8,6), (4,4),rowspan= 4, colspan=4)

ax1.imshow(iArr)
ax2.imshow(iArr2)
ax3.imshow(iArr_real)
ax4.imshow(iArr2_real)
plot.show()
