import pytesseract as pyt
import cv2
import re

img=cv2.imread("text.png")


text=pyt.image_to_string(img)

pattern='GSTINIUIN: \w{15}'
match=re.findall(pattern,text)
print(match)


mal='Total] = ([^\n]*)\)'
total=re.findall(mal,text)
print(total)
