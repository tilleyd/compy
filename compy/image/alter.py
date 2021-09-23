"""Contains image alterations."""

import numpy as np


def gaussian_noise(image: np.array, sigma: float = 0.3) -> np.array:
    """Adds Gaussian noise to an image.

    Args:
        image (np.array):
            Input image of any shape.
        sigma (float):
            Standard deviation of distribution from which noise is sampled.
            Larger is more intense noise. Default 0.3.

    Returns:
        np.array: Output image with added noise.
    """
    if image.dtype not in [np.float16, np.float32, np.float64]:
        from compy.image.errors import ImageDataTypeError

        raise ImageDataTypeError(image.dtype, [np.float16, np.float32, np.float64])

    noise = np.random.normal(loc=0, scale=sigma, size=image.shape).astype(image.dtype)
    return np.clip(image + noise, 0, 1)


def white_gaussian_noise(image: np.array, sigma: float = 0.3) -> np.array:
    """Adds white Gaussian noise to an image.

    Args:
        image (np.array):
            Input image of any shape in channels last format.
        sigma (float):
            Standard deviation of distribution from which noise is sampled.
            Larger is more intense noise. Default 0.3.

    Returns:
        np.array: Output image with added noise.
    """
    if image.dtype not in [np.float16, np.float32, np.float64]:
        from compy.image.errors import ImageDataTypeError

        raise ImageDataTypeError(image.dtype, [np.float16, np.float32, np.float64])

    noise_shape = image.shape[:-1] + (1,)
    noise = np.random.normal(loc=0, scale=sigma, size=noise_shape).astype(image.dtype)
    return np.clip(image + noise, 0, 1)


def gaussian_blur(image: np.array, sigma: float = 1) -> np.array:
    """Applies a Gaussian blurring filter to an image.

    Args:
        image (np.array):
            Input image with shape (height, width, channels).
        sigma (float):
            Standard deviation of Gaussian distribution across both vertical and
            horizontal axes. Higher values will lead to more intense blurring.

    Returns:
        np.array: Output image after applying filter.
    """
    from compy.image.filter import gaussian_filter

    return gaussian_filter(image, sigma)
