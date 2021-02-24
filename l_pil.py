from PIL import Image, ImageFilter

im = Image.open('images/girl.jpg')
im.getpixel((4, 4))
im.putpixel((4, 4), (255, 0, 0))
im.show()


# out = im.resize((128, 128))
# out = im.convert('1')
# out.show()
# box = (100, 100, 400, 400)
# region = im.crop(box)
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)
# im.show()


# imout = im.filter(ImageFilter.BLUR)
# print(imout.size)
# imout.show()

# enhancer = ImageEnhance.Brightness(im)
# im0 = enhancer.enhance(0.5)
# im0.show()


# draw = ImageDraw.Draw(im)
# draw.line((0, 0)+im.size, fill=128)
# draw.line((0, im.size[1], im.size[0], 0), fill=128)
# im.show()


# pil_im = Image.open('images/white.gif')
# new_img = Image.new('RGB', (640, 480), (255, 0, 0))

# pil_im = Image.open('images/white.gif').convert('L')
# pil_im.show()


# from PIL import ImageChops
# im = Image.open('images/rear.gif')
# im_dup = ImageChops.duplicate(im)
# print(im_dup.mode)
# im_diff = ImageChops.difference(im, im_dup)
# im_diff.show()
