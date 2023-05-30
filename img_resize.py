from PIL import Image

img1 = Image.open("Profile2.jpeg")
img1_resize = img1.resize((450, 600))

img1_resize.show()

img1.close()


