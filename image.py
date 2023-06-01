#!usr/bin/env python3

import os
import sys

from PIL import Image

size = (128, 128)
for wrong_image_format in os.listdir():
    correct_image_format = os.path.splitext(wrong_image_format)[0]

    try:
        with Image.open(wrong_image_format).convert('RGB') as image:
            image.thumbnail(size)
            image.rotate(270).save("/opt/icons" + correct_image_format, "JPEG")
    except OSError:
        pass