import os
import img2pdf
#specify the name for pdf file
with open("converted.pdf", "wb") as f:
    #collect all the images in a single folder and specify its location
    f.write(img2pdf.convert([i for i in os.listdir(files\images) if i.endswith(".jpg")]))
