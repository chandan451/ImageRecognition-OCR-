import PIL.Image as Image #can also be wirtten as "from PIL import Image" where PIL(python imaging library) is a library and Image is a module Image class and many genera functions like to load images ets.
import matplotlib.pyplot as pplt #can also be written as "from matplotlib import pyplot" where matplotlib is a plotting library and pyplot is a module containing several MATLAB like functions. 
import numpy 
i1 = Image.open("images/dotndot.png")
i2 = Image.open("images/dot.png")
imgarr1 = numpy.asarray(i1)
imgarr2 = numpy.asarray(i2)
print ("the array representation of a black dot of 8*8 pixel is : \n\n",imgarr1,"\n\nthe array representation of a black dot and a green dor is :\n",imgarr2)
pplt.imshow(imgarr1)
pplt.show()
pplt.imshow(imgarr2)
pplt.show()

