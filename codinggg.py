import qrcode
data="https://www.youtube.com/"
qr=qrcode.make(data)
qr.save("img.png")
qr.show()
