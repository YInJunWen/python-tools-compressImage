import os
import math

from glob import glob
from PIL import Image

source_dir = 'image'
target_dir = 'output'
filenames = glob('{}/*'.format(source_dir))
# print(filenames)

# 阀值 控制超出多少MB 开启压缩
threshold = 1*1024*1024


def resize_images(source_dir, target_dir, threshold):
    filenames = glob('{}/*'.format(source_dir))
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    for filename in filenames:
        filesize = os.path.getsize(filename)
        if filesize >= threshold:
            print(filename)
            with Image.open(filename) as im:
                width, height = im.size
                if width >= height:
                    new_width = int(math.sqrt(threshold/2))
                    new_height = int(new_width * height * 1.0 / width)
                else:
                    new_height = int(math.sqrt(threshold/2))
                    new_width = int(new_height * width * 1.0 / height)
                resized_im = im.resize((new_width, new_height))
                output_filename = filename.replace(source_dir, target_dir)
                resized_im.save(output_filename)


resize_images(source_dir, target_dir, threshold)
