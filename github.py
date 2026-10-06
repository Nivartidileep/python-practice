#QRCode --> pip install PyQRCode
import pyqrcode
import png
link =  "https://github.com/Nivartidileep"
#now we create QR code for above link
qr = pyqrcode.create(link)
#print(qr)
#now we need to create an image for our code
#pip install pypng
qr.png("myqr.png",scale = 10)
