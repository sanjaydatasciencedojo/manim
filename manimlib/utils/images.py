import os

import numpy as np
from manimlib.utils.file_ops import seek_full_path_from_defaults
from PIL import Image


def get_full_raster_image_path(image_file_name):
    return seek_full_path_from_defaults(
        image_file_name,
        default_dir=os.path.join("assets", "raster_images"),
        extensions=[".jpg", ".png", ".gif"]
    )


def drag_pixels(frames):
    curr = frames[0]
    new_frames = []
    for frame in frames:
        curr += (curr == 0) * np.array(frame)
        new_frames.append(np.array(curr))
    return new_frames


def invert_image(image):
    arr = np.array(image)
    arr = (255 * np.ones(arr.shape)).astype(arr.dtype) - arr
    return Image.fromarray(arr)
