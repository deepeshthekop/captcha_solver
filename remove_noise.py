from PIL import Image
import os

if not os.path.exists("noise_reduced"):
    os.mkdir("noise_reduced")

for image in os.listdir("captchas"):
    im = Image.open(os.path.join("captchas", image)).convert('L') #grayscale conversion
    pix = im.load()

    # thresholding
    for column in range(0, im.height):
        for row in range(0, im.width):
            if pix[row, column] != 0:
                pix[row, column] = 255

    # stray line and pixel removal
    for column in range(1, im.height - 1):
        for row in range(1, im.width - 1):
            if pix[row, column] == 0 \
                    and pix[row, column - 1] == 255 and pix[row, column + 1] == 255:
                pix[row, column] = 255
            if pix[row, column] == 0 \
                    and pix[row - 1, column] == 255 and pix[row + 1, column] == 255:
                pix[row, column] = 255

    im.save(os.path.join("noise_reduced", image))