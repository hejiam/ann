import imga as ia
from imgaug import augmenters as iaa
import numpy as np

seq = iaa.Sequential([
    iaa.Crop(px=(0,16)),
    iaa.Flip(0.5),
    iaa.GaussianBlur(sigma=(0,3.0))

])
for batch_idx in range(1000):
    images = load_batch(batch_idx)
    images_aug = seq.augment_image(images)
