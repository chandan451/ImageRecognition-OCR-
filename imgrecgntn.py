import numpy as np
import matplotlib.pyplot as plot
import PIL.Image as Img
from collections import Counter 

def createDatabase ():
    numberArraysDB = open("numArDB.txt","a")
    numWeHave = range(0,10)
    verWeHave = range(1,10)

    for eachNum in numWeHave:
        for eachVer in verWeHave:
    
            numImg= Img.open("images/numbers/"+str(eachNum)+"."+str(eachVer)+".png")
            numImgArr= np.array(numImg)
            numImgList= numImgArr.tolist()

            numberArraysDB.write(str(eachNum)+" :: "+str(numImgList)+"\n")

#createDatabase is to be called explicitly if required.


def blacknwhite(imArr):                             #this function can be used convert an image into black and white image if the given image is not black and white
    rowAvgArr = []
    newArr= imArr

    for eachRow in imArr:                           #for each row of the array
        for eachPixel in eachRow:                           #for each column/pixel in the each row of the image array
            pixAv=sum(eachPixel[:3])/3
            rowAvgArr.append(pixAv)
            
           
    imAv = sum(rowAvgArr)/len(rowAvgArr)
    
    for eachRow in newArr:
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

    return newArr


def recognize(filePath):
    matchArr = []
    loadDatabase = open("numArDB.txt","r").read()
    loadDatabase = loadDatabase.split("\n")

    i = Img.open(filePath)
    imgarr = np.array(i)
    imgarr=blacknwhite(imgarr)
    imgarrlist= imgarr.tolist()

    givenImgArr = str(imgarrlist)
    
    for eachRecord in loadDatabase:
        if len(eachRecord) > 9:
            splitRec = eachRecord.split("::")
            currNum = splitRec[0]
            currArr = splitRec[1]

            ListOfeachPixel= currArr.split("],")                               #list of RGB values of each pixel
            ListOfeachPixelInGI = givenImgArr.split("],")                      #each pixel in given image
            x=0

            while x < len(ListOfeachPixelInGI):
                if ListOfeachPixel[x] == ListOfeachPixelInGI[x]:                   #list of each pixel in a record is compared to list of each pixel in given image.
                    matchArr.append(int(currNum))
                x+=1

    c = Counter(matchArr)
    print(c)

    graphx = []
    graphy = []
    
    for eachelmt in c :
        graphx.append(eachelmt)
        graphy.append(c[eachelmt])

    ax1 = plot.subplot2grid((4,4),(0,0), rowspan=1,colspan=4)
    ax2 = plot.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)

    ax1.imshow(imgarr)
    ax2.bar(graphx,graphy, align="center")                                  #plotting bar graph

    plot.ylim(400)

    xloc = plot.MaxNLocator(11)

    ax2.xaxis.set_major_locator(xloc)                                       #x-axis setup

    plot.show()
     

recognize("images/test2.png")
