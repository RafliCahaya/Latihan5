import numpy as np
import imageio
import matplotlib.pyplot as plt
img = imageio.imread("gambar4.jpg")

img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

img_flip_horizontal = np.zeros(img.shape, img_type)
img_flip_vertical = np.zeros(img.shape, img_type)

for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_horizontal[y][x][c] = img[y][img_width-1-x][c]

  for y in range(0, img_height):
    for x in range(0, img_width):
        for c in range(0, img_channel):
            img_flip_vertical[y][x][c] = img[img_height-1-y][x][c]


plt.imshow(img_flip_horizontal)
plt.title("Flip Horizontal")
plt.show()
plt.imshow(img_flip_vertical)
plt.title("Flip Vertical")
plt.show()