import imageTools as it
import numpy as np
import tensorflow as tf

image_in = "parthenon.JPG"
image_out = "parthenon_new.png"

pic = it.Picture(image_in)
width = pic.getWidth()
height = pic.getHeight()
newPic = it.Picture(width, height)


def tensor_flow_step(x, y, x_filter, y_filter, pic):
    x_avg = 0
    y_avg = 0
    for i in range(3):
        x_sum = 0
        y_sum = 0
        for j in range(3):
            if x + j == 0 or x + j + 1 > width:
                continue
            for k in range(3):
                if y + k == 0 or y + k + 1 > height:
                    continue
                x_sum += x_filter[j][k] * \
                    pic.getColor(x + j - 1, y + k - 1)[i]
                y_sum += y_filter[j][k] * \
                    pic.getColor(x + j - 1, y + k - 1)[i]
        x_avg += x_sum / 3
        y_avg += y_sum / 3

    return np.sqrt(x_avg**2 + y_avg**2)


def compute():
    x_filter = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    y_filter = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    with tf.device('/GPU:0'):
        for x in range(pic.getWidth()):
            for y in range(pic.getHeight()):
                G = tensor_flow_step(x, y, x_filter, y_filter, pic)
                newPic.setColor(x, y, (G, G, G))


print(tf.config.list_physical_devices())
compute()
newPic.show()
input("Press Enter to continue...")
# newPic.save(image_out)
