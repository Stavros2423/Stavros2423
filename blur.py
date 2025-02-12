from PIL import Image, ImageFilter

before  = Image.open("bridge.bmp")
after = begore.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")
