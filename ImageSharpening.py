import numpy as np
import PIL.Image as Img
import matplotlib.pyplot as plot

def imgsharpen(imArr):
    rowAvgArr = []
    newarr= imArr

    for eachRow in imArr:                           #for each row of the array
        for eachPixel in eachRow:                           #for each column/pixel in the each row of the image array
            pixAv=sum(eachPixel[:3])/3
            rowAvgArr.append(pixAv)


    imAv = sum(rowAvgArr)/len(rowAvgArr)

    for eachRow in newarr:
        for eachPixel in eachRow:
            for i in range(3):
                if eachPixel[i] >= imAv:
                    eachPixel[i]= 255
                else:
                    eachPixel[i]= 0
    return newarr


i= Img.open("images/testImage.png")
iArr= np.array(i)
iArr_real=np.array(i)

i2= Img.open("images/numbers/y0.4.png")
iArr2= np.array(i2)
iArr2_real= np.array(i2)

imgsharpen(iArr)
imgsharpen(iArr2)

ax1= plot.subplot2grid((9,9), (0,0),rowspan= 4, colspan=4)
ax2= plot.subplot2grid((9,9), (4,0),rowspan= 4, colspan=4)
ax3= plot.subplot2grid((9,9), (0,4),rowspan= 4, colspan=4)
ax4= plot.subplot2grid((9,9), (4,4),rowspan= 4, colspan=4)

ax1.imshow(iArr)
ax2.imshow(iArr2)
ax3.imshow(iArr_real)
ax4.imshow(iArr2_real)
plot.show()

