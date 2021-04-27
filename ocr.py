import numpy as np
from matplotlib import pyplot as plt
import cv2
import imutils
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from pytesseract import Output

def build_tesseract_options(psm=7):
    # tell Tesseract to only OCR alphanumeric characters
    alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.!0123456789"
    options = "-c tessedit_char_whitelist={}".format(alphanumeric)
    # set the PSM mode
    #options += " --psm {}".format(psm)
    # return the built options string
    return options

def get_text(scr):
    img= cv2.imread(scr)
    img= imutils.resize(img, width= 700, height=50)
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    options = build_tesseract_options(1)
    results = pytesseract.image_to_data(rgb, output_type=Output.DICT, config= options)
    ##print(pytesseract.image_to_string(rgb, output_type=Output.DICT, config= options))
    print(results["text"],len(results["text"]))

    texts=""
    for i in range(0, len(results["text"])):

              if results["text"][i]!="":
                  print(results["text"][i])
                  texts= texts+results["text"][i]

    return texts

#image = cv2.imread("pic12.JPG")
#text= get_text(image)
#print(text,'text')
