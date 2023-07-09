import sys

from PIL import Image

images = []

# the [1:]  says starts from 1 until the end
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif",
    save_all = TRUE,
    append_images = [images[1]],
    duration = 200,
    loop = 0
)
