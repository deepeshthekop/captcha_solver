from PIL import Image
import os

ct = 0
if not os.path.exists("cropped_images"):
    os.mkdir("cropped_images")
for image in os.listdir("noise_reduced"):
    image_path = os.path.join("noise_reduced", image)
    img = Image.open(image_path)
    for j in range(30, 181, 30):
        ct += 1
        character_path = os.path.join("cropped_images", str(ct) + ".png")
        ch = img.crop((j-30, 12, j, 44))
        ch.save(character_path)