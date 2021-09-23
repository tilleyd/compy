"""Contains image I/O functions."""

import numpy as np
from typing import List


def read(path: str, dtype: np.dtype = np.uint8) -> np.array:
    """Reads an image and returns it as a numpy array.

    Args:
        path (str):
            Path to the image file.
        dtype (np.dtype, optional):
            Desired data type. If not uint8, the image is normalized to [0, 1].
            Defaults to np.uint8.

    Returns:
        np.array: The image with shape (height, width, channels).
    """
    from PIL import Image

    image = np.array(Image.open(path))

    if dtype != np.uint8:
        image = image / dtype(255)

    return image


def write(path: str, image: np.array) -> None:
    """Writes an image to disk.

    Args:
        path (str):
            Path to the output file.
        image (np.array):
            Image of shape (height, width, channels) of any dtype.
    """
    from PIL import Image

    if image.dtype != np.uint8:
        image = (image * 255).astype(np.uint8)

    Image.fromarray(image).save(path)


def read_generator(paths: List[str], dtype: np.dtype = np.uint8):
    """Returns a generator function that reads images on demand."""

    def _generator():
        for path in paths:
            yield read(path, dtype)

    return _generator
