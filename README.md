# ComPy

This package contains many functions that I commonly use in my work. It's mainly
used to speed up work that I do in interactive environments rather than for use
in production code.

## Installation

```
git clone https://github.com/tilleyd/compy
cd compy
python3 setup.py install
```

## Usage

The package contains a whole range of functions. The package is separated into
modules that work with specific types of data or produce specific outcomes,
e.g. `compy.image` to work with images and `compy.plot` to produce common plots.

If you are interested in using this library, have a look through the package.
It's mainly for personal use, so I'm not going to write a tutorial or anything.
The functions are at least documented as far as possible, so they should be
easy to understand and use.

For interest though, below is a snippet of how you can use the `image` module to
load an image, add white Gaussian noise, save the noisy image, and compare them
using SSIM and PSNR as metrics:

```python
import numpy as np
import compy.image as cim

image = cim.io.read("my-image.png", dtype=np.float32)
noisy_image = cim.alter.white_gaussian_noise(image, sigma=0.1)
cim.io.write("noisy-image.png", noisy_image)

ssim = cim.metrics.ssim(image, noisy_image)
psnr = cim.metrics.psnr(image, noisy_image)
print(f"SSIM: {ssim}, PSNR: {psnr}")
```

## License

Copyright &copy; 2021 Duncan Tilley.
See the [license notice](LICENSE.txt) for full details.
