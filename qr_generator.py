from datetime import datetime
import qrcode

link = ''

while link == '':
    link = input("Please Enter Link for QR Code: ")


qr = qrcode.QRCode(version=1, box_size=5, border=5)
qr.add_data(link)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')

name = input("Please Enter a Nmae for the QR Code: ")

if name != '':
    img.save(name + '.png')
else:
    img.save(str(datetime.now()) + '.png')
