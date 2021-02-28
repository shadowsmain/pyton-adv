import numpy as np
from PIL import Image

image_name = 'kit.jpg'
image = Image.open(image_name)

image_np = np.array(image)
print(image_np.size, image_np.shape)

image_np_conv = image_np
image_np_conv[:, :, :] += 20

new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'kitlightt.jpg'
new_image.save(save_name)