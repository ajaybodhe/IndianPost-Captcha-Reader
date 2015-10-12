from PIL import Image
import ImageEnhance
from pytesser import *
from urllib import urlretrieve
 
def get(link, name):
    urlretrieve(link, name)
       
get('http://www.indiapost.gov.in/captcha.aspx', './test/captcha.gif');
original = Image.open('./test/captcha.gif')
bg = original.resize((116, 56), Image.NEAREST)
ext = ".tif"
bg.save("./test/input-NEAREST" + ext)
image = Image.open('./test/input-NEAREST.tif')
print image_to_string(image)
