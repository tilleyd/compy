"""Contains image metrics."""

import numpy as np


def ssim(x: np.ndarray, y: np.ndarray) -> float:
    """Calculate the structural similarity metric (SSIM) between images.

    Note:
        This function requires skimage.
    """
    from skimage.metrics import structural_similarity

    assert x.dtype == y.dtype

    return structural_similarity(x, y, channel_axis=2, multichannel=True)


def psnr(x: np.ndarray, y: np.ndarray) -> float:
    """Takes two images, returns the peak signal-to-noise ratio."""
    assert x.dtype == y.dtype

    mserr = mse(x, y)
    max_i = 255 if x.dtype == np.uint8 else 1

    return 10 * np.log10((max_i * max_i) / mserr)


def mse(x: np.ndarray, y: np.ndarray) -> float:
    """Takes two images, returns the mean-squared-error."""
    assert x.dtype == y.dtype

    return np.mean(np.square(x - y))
