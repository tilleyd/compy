"""Contains image filters."""

import numpy as np


def gaussian_filter(image: np.array, sigma: float = 1) -> np.array:
    """Applies a Gaussian filter to an image.

    Args:
        image (np.array):
            Input image with shape (height, width, channels).
        sigma (float):
            Standard deviation of Gaussian distribution across both vertical and
            horizontal axes. Higher values will lead to more intense blurring.

    Returns:
        np.array: Output image after applying filter.
    """
    from scipy.ndimage import gaussian_filter

    sigmas = (sigma, sigma, 0)  # h, w, c

    return gaussian_filter(image, sigmas)
