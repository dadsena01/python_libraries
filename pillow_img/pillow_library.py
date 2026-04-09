from PIL import Image ,ImageFilter

img = Image.open("python_libraries/pillow_img/img01.png")

# Resize and save

img_resized = img.resize((300, 300))
img_resized.save("image_resized.png")


# convert to grayscale and save

img_gray = img.convert("L")
img_gray.save("image_grayscale.jpg") 

# Contour filter and save

contoured_img = img.filter(ImageFilter.CONTOUR)
contoured_img.show()
contoured_img.save("image_contour.jpg")

# Rotate and save
rotated_img = img.rotate(45)
rotated_img.save("image_rotated.jpg")

# blurring and save
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.save("image_blurred.jpg")

