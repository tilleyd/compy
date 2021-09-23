"""Contains custom exception classes."""

import numpy as np
from typing import Union, List, Optional


class ImageError(Exception):
    """Parent class of all image related errors."""

    def __init__(self, message):
        super().__init__(message)


class ImageDataTypeError(ImageError):
    """Error if image has incorrect data type."""

    def __init__(
        self,
        dtype_got: np.dtype,
        dtype_expected: Union[np.dtype, List[np.dtype]],
        message: Optional[str] = None,
    ):
        self.dtype_got = dtype_got
        self.dtype_expected = dtype_expected
        self.message = f"Incorrect image dtype {dtype_got} - expected {dtype_expected}"

        if message is not None:
            self.message += f"({message})"

        super().__init__(self.message)
