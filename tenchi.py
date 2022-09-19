from PIL import Image
from PIL import ImageOps

# 画像を開く
img = Image.open("6.png")

# 画像を回転する
img_rotate = img.rotate(270)

# 回転した画像の保存
img_rotate.save("rotated.png")

timg = Image.open("rotated.png")

img_mirror = ImageOps.mirror(timg)

img_mirror.save("replace.png")