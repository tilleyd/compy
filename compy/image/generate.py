"""Contains simple image generation functions."""

import numpy as np


def random(shape: tuple, dtype: np.dtype = np.uint8) -> np.array:
    """Generates a random image of the desired shape."""
    image = np.random.uniform(low=0, high=1, size=shape)

    if dtype == np.uint8:
        image = image * 255
    image = image.astype(dtype)

    return image


def solid(shape: tuple, color: tuple, dtype: np.dtype = np.uint8) -> np.array:
    """Generates an image filled with a color.

    shape (tuple):
        (height, width, channels) of the image to generate.
    color (tuple):
        Fill color of length `channels` (last dimension of `shape`). Will
        be cast to the dtype of the image.
    dtype (np.dtype, optional):
        Target data type of the array.

    Returns:
        np.array: The generated image.
    """
    return np.full(shape, color, dtype=dtype)
