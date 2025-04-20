import os
from PIL import Image


def is_image_corrupted(img_path):
    is_corrupted = False
    try:
        img = Image.open(img_path)
        img.verify()
    except:
        is_corrupted = True
    return is_corrupted


def is_image_not_rgb(img_path):
    img = Image.open(img_path)
    return img.mode != 'RGB'


# your path do dataset (where dirs Cat and Dog)
path_to_dataset = r''


labels = ['Cat', 'Dog']
for label in labels:
    path_by_label = os.path.join(path_to_dataset, label)
    images = os.listdir(path_by_label)
    for image in images:
        path_to_image = os.path.join(path_by_label, image)

        # check if image corrupted or not in RGB        
        if is_image_corrupted(path_to_image) or is_image_not_rgb(path_to_image):
            os.remove(path_to_image)
            continue
