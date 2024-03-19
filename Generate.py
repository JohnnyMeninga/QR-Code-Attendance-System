from MyQR import myqr
from io import  BytesIO
from barcode import EAN13
from barcode.writer import ImageWriter
import barcode
import os

f = open('2024AcceptanceList.txt','r')
lines = f.read().split("\n")
print(lines)


for _ in range (0,len(lines)):
    data = lines[_]
    version,level,qr = myqr.run(
        str(data),
        level='H',
        version=1,
        picture="UNITECH-PNG.png",
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name = str(lines[_]+'.png'),
        save_dir= "data/qr_student"
        #save_dir=os.getcwd()
    )
 

"""
for _ in range (0,len(lines)):
    data = lines[_]
    
    GS1_FNC1_CHAR = u'\xf1'
    code_128_creator = barcode.get_barcode_class("ean13")
    gs1_128_code = code_128_creator(GS1_FNC1_CHAR + data)
    barcode_image = gs1_128_code.render()
    barcode_image.save("data/qr_student")

"""