import qrcode
img = qrcode.make("hello world")
img.save("new.png")